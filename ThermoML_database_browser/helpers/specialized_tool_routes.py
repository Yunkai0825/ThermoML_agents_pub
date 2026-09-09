"""Generic Flask routes for read-only specialized-tool browser plugins."""

from __future__ import annotations

from flask import Blueprint, abort, jsonify, render_template, request, send_file, url_for

from ..specialized_tool_plugins import build_default_registry


specialized_tools_bp = Blueprint("specialized_tools", __name__)
specialized_tool_plugins = build_default_registry()


def _plugin(plugin_id: str):
    try:
        return specialized_tool_plugins.get(plugin_id)
    except LookupError:
        abort(404)


@specialized_tools_bp.route("/specialized-tools")
def browser_page():
    embedded = request.args.get("embedded", "").strip().lower() in {
        "1", "true", "yes", "on"
    }
    return render_template(
        "specialized_tools.html",
        base_template=(
            "specialized_tools_embedded_base.html" if embedded else "base.html"
        ),
        embedded=embedded,
    )


@specialized_tools_bp.route("/api/specialized-tools/plugins")
def plugin_list():
    return jsonify(plugins=specialized_tool_plugins.manifests())


@specialized_tools_bp.route("/api/specialized-tools/<plugin_id>/runs")
def run_list(plugin_id: str):
    try:
        limit = int(request.args.get("limit", 200))
    except (TypeError, ValueError):
        return jsonify(error="limit must be an integer"), 400
    try:
        runs = _plugin(plugin_id).list_runs(limit=limit)
    except (OSError, TypeError, ValueError) as exc:
        return jsonify(error=f"{type(exc).__name__}: {exc}"), 500
    return jsonify(plugin_id=plugin_id, runs=runs)


@specialized_tools_bp.route(
    "/api/specialized-tools/<plugin_id>/runs/<run_key>"
)
def run_detail(plugin_id: str, run_key: str):
    try:
        data = _plugin(plugin_id).get_run(run_key)
    except (FileNotFoundError, LookupError):
        abort(404)
    except (OSError, PermissionError, TypeError, ValueError) as exc:
        return jsonify(error=f"{type(exc).__name__}: {exc}"), 400
    for artifact in data.get("artifacts", []):
        artifact["download_url"] = url_for(
            "specialized_tools.artifact_download",
            plugin_id=plugin_id,
            run_key=run_key,
            artifact_id=artifact["artifact_id"],
        )
    for table in data.get("tables", []):
        table["data_url"] = url_for(
            "specialized_tools.table_data",
            plugin_id=plugin_id,
            run_key=run_key,
            table_id=table["table_id"],
        )
    return jsonify(data)


@specialized_tools_bp.route(
    "/api/specialized-tools/<plugin_id>/runs/<run_key>/tables/<table_id>"
)
def table_data(plugin_id: str, run_key: str, table_id: str):
    try:
        max_rows = int(request.args.get("max_rows", 10_000))
    except (TypeError, ValueError):
        return jsonify(error="max_rows must be an integer"), 400
    try:
        data = _plugin(plugin_id).read_table(
            run_key, table_id, max_rows=max_rows
        )
    except (FileNotFoundError, LookupError):
        abort(404)
    except (OSError, PermissionError, TypeError, ValueError) as exc:
        return jsonify(error=f"{type(exc).__name__}: {exc}"), 400
    return jsonify(data)


@specialized_tools_bp.route(
    "/api/specialized-tools/<plugin_id>/runs/<run_key>/artifacts/<artifact_id>"
)
def artifact_download(plugin_id: str, run_key: str, artifact_id: str):
    try:
        path = _plugin(plugin_id).artifact_path(run_key, artifact_id)
    except (FileNotFoundError, LookupError):
        abort(404)
    except (OSError, PermissionError, TypeError, ValueError):
        abort(403)
    return send_file(path, as_attachment=True, download_name=path.name)
