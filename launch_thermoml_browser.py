#!/usr/bin/env python3
"""Launch this checkout's ThermoML browser on an available local port."""
from __future__ import annotations

import argparse
from pathlib import Path
import socket
import sys
import threading
import webbrowser

from werkzeug.serving import ThreadedWSGIServer

_DEFAULT_PORT = 5000
_WORKSPACE = Path(__file__).resolve().parent
if str(_WORKSPACE) not in sys.path:
    sys.path.insert(0, str(_WORKSPACE))


class _LocalServer(ThreadedWSGIServer):
    # On Windows SO_REUSEADDR permits two servers to bind the same port.
    allow_reuse_address = False

    def server_bind(self):
        if hasattr(socket, "SO_EXCLUSIVEADDRUSE"):
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_EXCLUSIVEADDRUSE, 1)
        super().server_bind()


def _make_server(port: int):
    from ThermoML_results_browser.app import app
    return _LocalServer("127.0.0.1", port, app)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=None,
                        help="Explicit port, or 0 for any available port; defaults to 5000 with fallback")
    parser.add_argument("--no-browser", action="store_true",
                        help="Print the URL without opening a browser tab")
    args = parser.parse_args(argv)
    if args.port is not None and not 0 <= args.port <= 65535:
        parser.error("--port must be between 0 and 65535")

    try:
        server = _make_server(_DEFAULT_PORT if args.port is None else args.port)
    except (OSError, SystemExit) as exc:
        if args.port is not None:
            print(f"Cannot start on requested port {args.port}: {exc}", flush=True)
            return 1
        print(f"Port {_DEFAULT_PORT} is unavailable; selecting a free port.", flush=True)
        try:
            server = _make_server(0)
        except (OSError, SystemExit) as fallback_error:
            print(f"Cannot start local server: {fallback_error}", flush=True)
            return 1

    url = f"http://127.0.0.1:{server.server_port}"
    print(f"Workspace: {_WORKSPACE}", flush=True)
    print(f"ThermoML browser: {url}", flush=True)
    print("Press Ctrl+C to stop.", flush=True)
    opener = None
    if not args.no_browser:
        opener = threading.Timer(0.3, webbrowser.open, args=(url,))
        opener.daemon = True
        opener.start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        if opener is not None:
            opener.cancel()
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
