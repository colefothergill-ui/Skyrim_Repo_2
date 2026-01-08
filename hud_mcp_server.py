from __future__ import annotations

import fnmatch
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

from mcp.server.fastmcp import FastMCP

ROOT = Path(__file__).resolve().parent

mcp = FastMCP("GM Skyrim HUD", json_response=True)

def _safe(path: str) -> Path:
    p = (ROOT / path).resolve()
    if not str(p).startswith(str(ROOT.resolve())):
        raise ValueError("Unsafe path (outside repo).")
    return p

def _run(cmd: List[str], cwd: Optional[Path] = None) -> Dict[str, Any]:
    r = subprocess.run(
        cmd,
        cwd=str(cwd or ROOT),
        capture_output=True,
        text=True,
        errors="replace",
        shell=False,
    )
    return {
        "ok": r.returncode == 0,
        "returncode": r.returncode,
        "stdout": r.stdout,
        "stderr": r.stderr,
    }

@mcp.tool(description="List files under repo root (limited).")
def list_files(glob: str = "**/*", limit: int = 200) -> Dict[str, Any]:
    limit = max(1, min(int(limit), 2000))
    pattern = glob or "**/*"
    out: List[str] = []
    for p in ROOT.rglob("*"):
        if p.is_file():
            rel = p.relative_to(ROOT).as_posix()
            if fnmatch.fnmatch(rel, pattern):
                out.append(rel)
                if len(out) >= limit:
                    break
    return {"glob": pattern, "limit": limit, "count": len(out), "files": out}

@mcp.tool(description="Read a text file from the repo (safe-path).")
def read_text(path: str, max_chars: int = 20000) -> Dict[str, Any]:
    p = _safe(path)
    max_chars = max(1, min(int(max_chars), 200000))
    if not p.exists() or not p.is_file():
        return {"ok": False, "error": f"File not found: {path}"}
    try:
        txt = p.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        return {"ok": False, "error": f"Read failed: {e}"}
    return {"ok": True, "path": path, "truncated": len(txt) > max_chars, "text": txt[:max_chars]}

@mcp.tool(description="Naive text search across files matching glob.")
def search_text(query: str, glob: str = "**/*.md", limit: int = 50) -> Dict[str, Any]:
    q = query or ""
    limit = max(1, min(int(limit), 500))
    pattern = glob or "**/*"
    hits: List[Dict[str, Any]] = []
    if not q:
        return {"ok": False, "error": "query is empty"}
    rx = re.compile(re.escape(q), re.IGNORECASE)
    for p in ROOT.rglob("*"):
        if not p.is_file():
            continue
        rel = p.relative_to(ROOT).as_posix()
        if not fnmatch.fnmatch(rel, pattern):
            continue
        try:
            txt = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        for i, line in enumerate(txt.splitlines(), start=1):
            if rx.search(line):
                hits.append({"path": rel, "line": i, "text": line[:300]})
                if len(hits) >= limit:
                    return {"ok": True, "query": q, "glob": pattern, "limit": limit, "hits": hits}
    return {"ok": True, "query": q, "glob": pattern, "limit": limit, "hits": hits}

@mcp.tool(description="Return branch/commit + dirty status for the repo.")
def repo_status() -> Dict[str, Any]:
    branch = _run(["git", "rev-parse", "--abbrev-ref", "HEAD"])
    commit = _run(["git", "rev-parse", "HEAD"])
    dirty = _run(["git", "status", "--porcelain"])
    return {
        "ok": True,
        "branch": (branch["stdout"] or "").strip(),
        "commit": (commit["stdout"] or "").strip(),
        "dirty": bool((dirty["stdout"] or "").strip()),
        "porcelain": (dirty["stdout"] or "").splitlines()[:200],
    }

_ALLOWED = {
    "boot_banner": "scripts/first_run.py",
    "on_track": "scripts/on_track.py",
    "build_context": "scripts/build_context.py",
}

@mcp.tool(description="Run a whitelisted repo script and return its output. Allowed: boot_banner, on_track, build_context")
def run_module_script(name: str) -> Dict[str, Any]:
    if name not in _ALLOWED:
        return {"ok": False, "error": f"Not allowed: {name}", "allowed": sorted(_ALLOWED.keys())}
    script_rel = _ALLOWED[name]
    script_path = _safe(script_rel)
    if not script_path.exists():
        return {"ok": False, "error": f"Missing script: {script_rel}"}
    # Force console-safe behavior
    env = os.environ.copy()
    env["PYTHONUTF8"] = "1"
    r = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        errors="replace",
        env=env,
        shell=False,
    )
    return {"ok": r.returncode == 0, "returncode": r.returncode, "stdout": r.stdout, "stderr": r.stderr}

if __name__ == "__main__":
    # MCP Python SDK: streamable-http defaults to http://localhost:8000/mcp
    mcp.run(transport="streamable-http")
