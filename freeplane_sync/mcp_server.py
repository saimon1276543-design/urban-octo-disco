from __future__ import annotations

import argparse
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

from .engine import Workspace


class Handler(BaseHTTPRequestHandler):
    ws: Workspace
    token: str

    def _send(self, value: dict, status: int = 200) -> None:
        raw = json.dumps(value).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def do_POST(self) -> None:  # noqa: N802
        if self.path != "/mcp":
            self._send({"error": "not found"}, 404)
            return
        if self.headers.get("Authorization", "") != f"Bearer {self.token}":
            self._send({"error": "unauthorized"}, 401)
            return
        try:
            body = json.loads(self.rfile.read(int(self.headers.get("Content-Length", "0"))))
            method = body.get("method")
            params = body.get("params", {})
            if method == "initialize":
                result = {"protocolVersion": "2024-11-05", "serverInfo": {"name": "freeplane-sync", "version": "0.1.0"}, "capabilities": {"tools": {}}}
            elif method == "tools/list":
                result = {"tools": [{"name": "workspace_status", "description": "Read workspace status", "inputSchema": {"type": "object"}}, {"name": "sync", "description": "Synchronize maps and workspace", "inputSchema": {"type": "object", "properties": {"direction": {"enum": ["import", "export", "auto"]}}}}, {"name": "create_checkpoint", "description": "Create a recoverable checkpoint", "inputSchema": {"type": "object"}}]}
            elif method == "tools/call":
                name = params.get("name")
                if name == "workspace_status":
                    result = {"content": [{"type": "text", "text": json.dumps({"workspace": str(self.ws.root), "maps": [p.name for p in self.ws.map_paths()]})}]}
                elif name == "sync":
                    direction = params.get("arguments", {}).get("direction", "auto")
                    result_obj = self.ws.import_maps() if direction == "import" else self.ws.export_maps() if direction == "export" else self.ws.import_maps()
                    result = {"content": [{"type": "text", "text": json.dumps(result_obj.__dict__)}]}
                elif name == "create_checkpoint":
                    result = {"content": [{"type": "text", "text": str(self.ws.checkpoint("mcp"))}]}
                else:
                    result = {"isError": True, "content": [{"type": "text", "text": "unknown tool"}]}
            else:
                result = {"error": f"unsupported method: {method}"}
            self._send({"jsonrpc": "2.0", "id": body.get("id"), "result": result})
        except Exception as exc:  # keep bridge alive and return diagnostic
            self._send({"jsonrpc": "2.0", "id": None, "error": {"code": -32000, "message": str(exc)}}, 500)

    def log_message(self, *_args) -> None:
        return


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", default=".")
    parser.add_argument("--port", type=int, default=6299)
    parser.add_argument("--token", required=True)
    args = parser.parse_args()
    ws = Workspace(Path(args.workspace).resolve())
    ws.init()
    Handler.ws = ws
    Handler.token = args.token
    print(f"MCP bridge listening on http://127.0.0.1:{args.port}/mcp")
    HTTPServer(("127.0.0.1", args.port), Handler).serve_forever()


if __name__ == "__main__":
    main()
