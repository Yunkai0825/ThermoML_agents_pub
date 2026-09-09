#!/usr/bin/env python
"""Start the local ThermoML server and open it in the default web browser.

Run from any working directory:
    python launch_thermoml_browser.py
    python launch_thermoml_browser.py --port 5001

Keep this process running while using the app. Press Ctrl+C to stop it.
"""
from __future__ import annotations

import argparse
import contextlib
import io
import socket
import sys
import threading
import webbrowser
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parent
DEFAULT_PORT = 5000


def _make_local_server(app, port):
    from werkzeug.serving import ThreadedWSGIServer

    class LocalServer(ThreadedWSGIServer):
        # Windows permits two servers to bind the same port with SO_REUSEADDR.
        # An exclusive listener keeps an older browser from receiving our requests.
        allow_reuse_address = False

        def server_bind(self):
            if hasattr(socket, 'SO_EXCLUSIVEADDRUSE'):
                self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_EXCLUSIVEADDRUSE, 1)
            super().server_bind()

    return LocalServer('127.0.0.1', port, app)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int,
                        help='Local server port (default: 5000, or a free port if occupied; '
                             '0 chooses a free port)')
    parser.add_argument('--no-browser', action='store_true',
                        help='Start the server without opening a browser window')
    args = parser.parse_args(argv)
    if args.port is not None and not 0 <= args.port <= 65535:
        parser.error('--port must be between 0 and 65535')

    if str(WORKSPACE_ROOT) not in sys.path:
        sys.path.insert(0, str(WORKSPACE_ROOT))
    try:
        from ThermoML_database_browser.app import app
    except ModuleNotFoundError as exc:
        print(f'Missing dependency: {exc.name}. Install the runtime dependencies with:',
              file=sys.stderr)
        print(f'  "{sys.executable}" -m pip install -r '
              f'"{WORKSPACE_ROOT / "ThermoML_research_agent" / "requirements.txt"}"',
              file=sys.stderr)
        return 1

    # Binding completes before opening the page; all requests stay on localhost.
    requested_port = DEFAULT_PORT if args.port is None else args.port
    binding_errors = io.StringIO()
    try:
        with contextlib.redirect_stderr(binding_errors):
            server = _make_local_server(app, requested_port)
    except SystemExit:
        if args.port is not None:
            print(binding_errors.getvalue().rstrip(), file=sys.stderr)
            print('Choose another port or use --port 0.', file=sys.stderr)
            return 1
        print(f'Port {requested_port} is unavailable; selecting a free port.', flush=True)
        server = _make_local_server(app, 0)
    url = f'http://127.0.0.1:{server.server_port}/'
    worker = threading.Thread(target=server.serve_forever, name='thermoml-server', daemon=True)
    worker.start()
    print(f'ThermoML workspace: {WORKSPACE_ROOT}', flush=True)
    print(f'ThermoML browser: {url}', flush=True)
    print('Press Ctrl+C to stop the server.', flush=True)
    try:
        if not args.no_browser:
            try:
                if not webbrowser.open(url, new=2):
                    print(f'Open {url} in your browser.', flush=True)
            except webbrowser.Error:
                print(f'Open {url} in your browser.', flush=True)
        while worker.is_alive():
            worker.join(timeout=0.5)
    except KeyboardInterrupt:
        print('\nStopping ThermoML browser.', flush=True)
    finally:
        server.shutdown()
        server.server_close()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
