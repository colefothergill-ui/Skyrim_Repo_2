# scripts/sitecustomize.py
# Auto-loaded by Python's "site" module.
# Prevents UnicodeEncodeError on Windows consoles using cp1252.

import sys

def _fix_stream(stream):
    try:
        stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

_fix_stream(sys.stdout)
_fix_stream(sys.stderr)
