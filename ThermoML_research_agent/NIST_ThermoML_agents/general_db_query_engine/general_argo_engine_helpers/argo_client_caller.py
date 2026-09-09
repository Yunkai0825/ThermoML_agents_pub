"""
ArgoClient — dataclass-based LLM caller for the Argo API.
==========================================================

Uses the Argo ``/chat/`` turn-based endpoint with ``requests.post()``.
Provides both synchronous ``call()`` and asynchronous ``acall()``
methods.  The async variant uses ``asyncio.to_thread()`` to wrap the
synchronous call, keeping the implementation simple and testable.

Factory constructors
--------------------
- ``ArgoClient.with_tier(tier, **overrides)`` — generic tier label.
- ``ArgoClient.for_verdict()``  — post-job quality review client.
- ``ArgoClient.for_compactor()`` — LLM compaction sub-agent client.
- ``ArgoClient.for_planner()``  — strategy-planning client.

Per-agent tier constructors (``for_l0``, ``for_l1``, ``for_l2``) live
in each agent's ``argo_engine_subagent_helpers/argo_client.py`` as
``QueryClient`` / ``AnalysisClient`` subclasses.

Usage
-----
::

    from argo_engine_helpers import ArgoClient

    # Direct construction with overrides
    client = ArgoClient(model="gpt5", temperature=0.1)

    # Synchronous (blocking)
    response = client.call(prompt, system_prompt)

    # Asynchronous (for parallel L2 dispatch)
    response = await client.acall(prompt, system_prompt)

    # Via factory method — reads active EngineConfig
    verdict_client = ArgoClient.for_verdict()
"""

from __future__ import annotations

import asyncio
import logging
import time
from dataclasses import dataclass, field
from typing import Any, Callable

import requests

from .engine_config import get_config
from ..general_hooks_management_helpers.general_context_hooks.stats_references_tracking_hooks import (
    get_active_recorder as _get_stats_recorder,
)
from ..general_hooks_management_helpers.general_context_hooks.history_tracking_hooks import (
    get_active_history_recorder as _get_history_recorder,
)
from ..general_text_context_marker_catalog import MARKERS

log = logging.getLogger("ArgoClient")

# ── Explicit token tally bridge to an embedding runtime (optional) ──────
_master_token_recorder: Callable[..., None] | None = None


def set_master_token_recorder(callback: Callable[..., None]) -> None:
    """Register the embedding runtime's exact token-recording callback."""
    global _master_token_recorder
    if not callable(callback):
        raise TypeError("callback must be callable")
    _master_token_recorder = callback


def clear_master_token_recorder() -> None:
    """Disable embedding-runtime token recording explicitly."""
    global _master_token_recorder
    _master_token_recorder = None


def _record_master_tokens(agent: str, body: dict, *, input_chars: int, output_chars: int) -> None:
    """Forward usage to the explicitly registered embedding callback."""
    if _master_token_recorder is None:
        return
    usage = body["usage"] if "usage" in body else None
    pt = ct = tt = None
    if isinstance(usage, dict):
        pt = usage["prompt_tokens"] if "prompt_tokens" in usage else None
        ct = usage["completion_tokens"] if "completion_tokens" in usage else None
        tt = usage["total_tokens"] if "total_tokens" in usage else None
    _master_token_recorder(
        agent, prompt_tokens=pt, completion_tokens=ct, total_tokens=tt,
        input_chars=input_chars, output_chars=output_chars,
    )


@dataclass
class ArgoClient:
    """Dataclass wrapping a single LLM caller configuration.

    Each agent layer (L0 orchestrator, L1 worker, L2 evaluator, verdict)
    creates its own ``ArgoClient`` with the appropriate model, temperature,
    and token budget.
    """

    model: str = field(default_factory=lambda: get_config().MODEL)
    temperature: float = field(default_factory=lambda: get_config().TEMPERATURE)
    top_p: float = field(default_factory=lambda: get_config().TOP_P)
    max_tokens: int = field(default_factory=lambda: get_config().MAX_TOKENS)
    stop: list[str] = field(default_factory=lambda: [MARKERS.tool_call.close])
    max_retries: int = 5
    retry_backoff: float = 2.0
    http_timeout: int = field(default_factory=lambda: get_config().HTTP_TIMEOUT)
    api_url: str = field(default_factory=lambda: get_config().API_URL)
    api_user: str = field(default_factory=lambda: get_config().API_USER)
    _tier: str = ""   # stats-only label (e.g. "L0-main", "L1-subagent")

    def __post_init__(self) -> None:
        if not isinstance(self.model, str) or not self.model:
            raise TypeError("model must be a non-empty string")
        if isinstance(self.max_tokens, bool) or not isinstance(self.max_tokens, int) or self.max_tokens <= 0:
            raise TypeError("max_tokens must be a positive integer")
        if isinstance(self.max_retries, bool) or not isinstance(self.max_retries, int) or self.max_retries <= 0:
            raise TypeError("max_retries must be a positive integer")
        if isinstance(self.retry_backoff, bool) or not isinstance(self.retry_backoff, (int, float)) or self.retry_backoff < 0:
            raise TypeError("retry_backoff must be a non-negative number")
        if isinstance(self.http_timeout, bool) or not isinstance(self.http_timeout, int) or self.http_timeout <= 0:
            raise TypeError("http_timeout must be a positive integer")
        if not isinstance(self.api_url, str) or not self.api_url:
            raise TypeError("api_url must be a non-empty string")
        if not isinstance(self.api_user, str) or not self.api_user:
            raise TypeError("api_user must be a non-empty string")
        if not isinstance(self.stop, list) or not all(isinstance(item, str) for item in self.stop):
            raise TypeError("stop must be a list of strings")

    # ── payload builder ──────────────────────────────────────

    def _build_payload(
        self,
        prompt: str,
        system: str,
        *,
        max_tokens: int | None = None,
        stop: list[str] | None = None,
        model: str | None = None,
    ) -> dict[str, Any]:
        if not isinstance(prompt, str) or not isinstance(system, str):
            raise TypeError("prompt and system must be strings")
        _model = self.model if model is None else model
        _stop = stop if stop is not None else self.stop
        _max_tokens = self.max_tokens if max_tokens is None else max_tokens
        if not isinstance(_model, str) or not _model:
            raise TypeError("model must be a non-empty string")
        if not isinstance(_stop, list) or not all(isinstance(item, str) for item in _stop):
            raise TypeError("stop must be a list of strings")
        if isinstance(_max_tokens, bool) or not isinstance(_max_tokens, int) or _max_tokens <= 0:
            raise TypeError("max_tokens must be a positive integer")

        payload: dict[str, Any] = {
            "user":        self.api_user,
            "model":       _model,
            "system":      system,
            "prompt":      [prompt],
            "stop":        _stop,
            "temperature": self.temperature,
            "max_tokens":  _max_tokens,
        }
        if not get_config().is_claude_model(_model):
            payload["top_p"] = self.top_p
        return payload

    @staticmethod
    def _fix_stop_token(text: str) -> str:
        """Re-append </tool_call> if it was stripped by the stop sequence."""
        if MARKERS.tool_call.open in text and MARKERS.tool_call.close not in text:
            text += MARKERS.tool_call.close
        return text

    # ── synchronous call (turn-based) ────────────────────────

    def call(
        self,
        prompt: str,
        system: str,
        *,
        max_tokens: int | None = None,
        stop: list[str] | None = None,
        model: str | None = None,
        event_kind: str = "",
    ) -> str:
        """Send a prompt to the Argo API and return the full response.

        Parameters
        ----------
        prompt : str
            The full user/conversation prompt.
        system : str
            System message.
        max_tokens, stop, model : optional
            Per-call overrides.
        event_kind : optional
            Label kind for the run-history session event log (e.g.
            ``"ReAct"``); defaults to the client tier.

        Returns
        -------
        str
            The model's complete text response.

        Raises
        ------
        RuntimeError
            If all retry attempts are exhausted.
        """
        payload = self._build_payload(
            prompt, system, max_tokens=max_tokens, stop=stop, model=model,
        )
        stats_recorder = _get_stats_recorder() if self._tier else None
        _model = payload["model"]
        prompt_len = sum(len(p) for p in payload["prompt"]) if isinstance(payload["prompt"], list) else len(payload["prompt"])
        log.info(
            ">> Argo request: model=%s, system=%d chars, prompt=%d chars, max_tokens=%d",
            _model, len(system), prompt_len, payload["max_tokens"],
        )

        # Real-time session event log — the pending request row hits the
        # run history before the HTTP call returns (never fatal).
        _hist = None
        _argo_ev = None
        try:
            _hist = _get_history_recorder()
            _argo_ev = _hist.begin_argo_event(
                tier=self._tier, model=_model,
                system_chars=len(system), prompt_chars=prompt_len,
                kind=event_kind,
            )
        except Exception:
            _hist, _argo_ev = None, None

        def _finish_event(status: str, *, response_chars: int = 0,
                          elapsed_s: float = -1.0, attempts: int = 0,
                          response_text: str = "", error: str = "") -> None:
            if _hist is None or _argo_ev is None:
                return
            try:
                _hist.end_argo_event(
                    _argo_ev, response_chars=response_chars,
                    elapsed_s=elapsed_s, attempts=attempts, status=status,
                    response_text=response_text, error=error)
            except Exception:
                pass

        last_err: str | None = None
        for attempt in range(1, self.max_retries + 1):
            t0 = time.time()
            try:
                r = requests.post(
                    self.api_url,
                    headers=get_config().HEADERS,
                    json=payload,
                    timeout=self.http_timeout,
                )
                elapsed = time.time() - t0

                if r.status_code == 500:
                    log.warning(
                        "[!] API 500 (attempt %d/%d, %.1fs): %s",
                        attempt, self.max_retries, elapsed, r.text[:200],
                    )
                    last_err = f"500: {r.text[:200]}"
                    time.sleep(self.retry_backoff * attempt)
                    continue

                if r.status_code == 429:
                    wait = self.retry_backoff * (2 ** attempt)
                    log.warning(
                        "[!] 429 rate-limited (attempt %d/%d, %.1fs); "
                        "backing off %.0fs",
                        attempt, self.max_retries, elapsed, wait,
                    )
                    last_err = f"429: {r.text[:200]}"
                    time.sleep(wait)
                    continue

                # Authentication / authorization failures are NOT transient —
                # retrying the same credentials cannot succeed. Fail fast with
                # an actionable message instead of burning every retry.
                if r.status_code in (401, 403):
                    _auth_msg = (
                        f"Argo authentication failed (HTTP {r.status_code}). The ANL argoapi "
                        f"rejected the request for user '{self.api_user}' / model '{_model}' at "
                        f"{self.api_url}. This is an upstream credential/endpoint issue, not a "
                        f"problem with the prompt. Check that the ANL username is correct, you are "
                        f"on the ANL network/VPN, and the endpoint/model are available (override "
                        f"the endpoint with the ARGO_API_URL env var if the dev endpoint is down). "
                        f"Server said: {r.text[:300]}"
                    )
                    _finish_event("error", elapsed_s=round(elapsed, 1),
                                  attempts=attempt, error=_auth_msg)
                    raise RuntimeError(_auth_msg)

                r.raise_for_status()

                body = r.json()
                if not isinstance(body, dict) or "response" not in body:
                    _finish_event("error", elapsed_s=round(elapsed, 1),
                                  attempts=attempt,
                                  error="Argo response must be an object containing 'response'")
                    raise RuntimeError("Argo response must be an object containing 'response'")
                text = body["response"]
                if not isinstance(text, str):
                    _finish_event("error", elapsed_s=round(elapsed, 1),
                                  attempts=attempt,
                                  error="Argo response.response must be a string")
                    raise RuntimeError("Argo response.response must be a string")
                text = self._fix_stop_token(text)

                # Detect upstream 429 relayed as 200 body text
                if text.lstrip().startswith("Error:") and "429" in text[:300]:
                    log.warning(
                        "[!] Upstream 429 in body (attempt %d/%d): %s",
                        attempt, self.max_retries, text[:200],
                    )
                    last_err = f"Upstream 429: {text[:200]}"
                    time.sleep(self.retry_backoff * attempt * 2)
                    continue

                log.info(
                    "<< Argo responded in %.1fs (%d chars)",
                    elapsed, len(text),
                )
                # Optional embedding callback is registered explicitly.
                _record_master_tokens(
                    self._tier or "ThermoML", body,
                    input_chars=len(system) + prompt_len,
                    output_chars=len(text) if isinstance(text, str) else 0,
                )
                # Agent calls are hard-recorded in their explicitly active run.
                if stats_recorder is not None:
                    stats_recorder.log_argo_call(
                        tier=self._tier,
                        model=_model,
                        system_chars=len(system),
                        prompt_chars=prompt_len,
                        response_chars=len(text),
                        elapsed_s=round(elapsed, 1),
                    )
                _finish_event("ok", response_chars=len(text),
                              elapsed_s=round(elapsed, 1), attempts=attempt,
                              response_text=text)
                return text

            except requests.ReadTimeout:
                elapsed = time.time() - t0
                log.error(
                    "[!] TIMEOUT after %.1fs (attempt %d/%d)",
                    elapsed, attempt, self.max_retries,
                )
                last_err = f"Timeout after {elapsed:.0f}s"
                time.sleep(self.retry_backoff * attempt)

            except requests.ConnectionError as e:
                elapsed = time.time() - t0
                log.error(
                    "[!] Connection error after %.1fs (attempt %d/%d): %s",
                    elapsed, attempt, self.max_retries, e,
                )
                last_err = str(e)
                time.sleep(self.retry_backoff * attempt)

            except requests.RequestException as e:
                elapsed = time.time() - t0
                log.warning(
                    "[!] Request failed after %.1fs (attempt %d/%d): %s",
                    elapsed, attempt, self.max_retries, e,
                )
                last_err = str(e)
                time.sleep(self.retry_backoff * attempt)

        _finish_event("error", attempts=self.max_retries,
                      error=str(last_err or "exhausted retries"))
        raise RuntimeError(
            f"Argo API failed after {self.max_retries} attempts: {last_err}"
        )

    # ── asynchronous call (wraps sync via asyncio.to_thread) ─

    async def acall(
        self,
        prompt: str,
        system: str,
        *,
        max_tokens: int | None = None,
        stop: list[str] | None = None,
        model: str | None = None,
        event_kind: str = "",
    ) -> str:
        """Async version of call() for use with asyncio.gather().

        Uses asyncio.to_thread() to avoid blocking the event loop
        while keeping the implementation simple and tested.
        """
        return await asyncio.to_thread(
            self.call,
            prompt,
            system,
            max_tokens=max_tokens,
            stop=stop,
            model=model,
            event_kind=event_kind,
        )

    # ── convenience constructors ─────────────────────────────
    # Agent-specific factory methods (for_l0, for_l1, etc.) live in
    # each agent's argo_engine_subagent_helpers package.  Only the
    # base constructor is provided here.

    @classmethod
    def with_tier(cls, tier: str, **overrides) -> ArgoClient:
        """Create an ArgoClient with a stats-only tier label + overrides."""
        return cls(_tier=tier, **overrides)

    @classmethod
    def for_verdict(cls) -> ArgoClient:
        """Create an ArgoClient configured for the post-job verdict agent."""
        _cfg = get_config()
        return cls(
            model=_cfg.VERDICT_MODEL,
            temperature=_cfg.VERDICT_TEMPERATURE,
            max_tokens=_cfg.VERDICT_MAX_TOKENS,
            _tier="verdict",
        )

    @classmethod
    def for_compactor(cls) -> ArgoClient:
        """Create an ArgoClient for compression sub-agent calls."""
        _cfg = get_config()
        return cls(temperature=_cfg.COMPACTOR_TEMPERATURE, max_tokens=_cfg.COMPACTOR_MAX_TOKENS, stop=[], _tier="compactor")

    @classmethod
    def for_planner(cls) -> ArgoClient:
        """Create an ArgoClient for strategy planning calls."""
        _cfg = get_config()
        return cls(model=_cfg.PLANNER_MODEL, temperature=_cfg.PLANNER_TEMPERATURE, max_tokens=_cfg.PLANNER_MAX_TOKENS, _tier="planner")
