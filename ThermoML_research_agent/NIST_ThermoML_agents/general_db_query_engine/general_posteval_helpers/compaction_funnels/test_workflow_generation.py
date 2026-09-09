"""Post-run workflow artifacts are generated for every root session."""
from unittest.mock import Mock

import pytest

from . import api


@pytest.mark.parametrize("kind", ["main", "query", "analysis"])
def test_root_session_generates_workflow(tmp_path, monkeypatch, kind):
    session = tmp_path / kind / "run_example"
    expected = api.WorkflowReport(session, kind, "example", session / "workflow")
    generate = Mock(return_value=expected)
    monkeypatch.setattr(api, "generate_workflow", generate)

    assert api.maybe_generate_workflow(session, kind=kind) is expected
    generate.assert_called_once_with(session, kind=kind)


@pytest.mark.parametrize("child_folder", ["query_runs", "analysis_runs"])
def test_child_workflow_is_included_in_root(tmp_path, monkeypatch, child_folder):
    generate = Mock()
    monkeypatch.setattr(api, "generate_workflow", generate)

    assert api.maybe_generate_workflow(tmp_path / child_folder / "run_1") is None
    generate.assert_not_called()


def test_generation_failure_is_reported_without_failing_agent(tmp_path, monkeypatch):
    session = tmp_path / "run_example"
    monkeypatch.setattr(api, "generate_workflow", Mock(side_effect=RuntimeError("render unavailable")))

    result = api.maybe_generate_workflow(session, kind="main")

    assert result.error == "render unavailable"
    assert result.out_dir == session / "workflow"
    assert not result.ok
