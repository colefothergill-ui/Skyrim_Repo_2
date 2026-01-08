# sitecustomize.py
# Auto-loaded by Python's "site" module (unless you run Python with -S).
# Goal: prevent UnicodeEncodeError on Windows consoles using cp1252.

import sys

def _fix_stream(stream):
    try:
        # Force UTF-8 and never crash on characters the console can't display.
        stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        # If reconfigure isn't available or stream isn't configurable, do nothing.
        pass

_fix_stream(sys.stdout)
_fix_stream(sys.stderr)
