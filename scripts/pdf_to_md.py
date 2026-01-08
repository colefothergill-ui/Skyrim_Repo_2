"""pdf_to_md.py
Convert a PDF to a Markdown-ish text file.

Usage:
  python pdf_to_md.py "input.pdf" "output.md"

Notes:
- Best-effort extraction. Scanned PDFs will need OCR (not included here).
"""

import sys
import re
from pathlib import Path

# Compile regex patterns once for better performance
SPACE_PATTERN = re.compile(r"[ \t]+")
PUNCTUATION_PATTERN = re.compile(r"\s+([,.;:!?])")
NEWLINE_PATTERN = re.compile(r"\n{3,}")

def clean(t: str) -> str:
  t = t.replace("\r", "\n")
  t = SPACE_PATTERN.sub(" ", t)
  t = PUNCTUATION_PATTERN.sub(r"\1", t)
  t = NEWLINE_PATTERN.sub("\n\n", t)
  return t.strip()

def main():
  if len(sys.argv) != 3:
    print("Usage: python pdf_to_md.py input.pdf output.md")
    sys.exit(1)

  in_path = Path(sys.argv[1])
  out_path = Path(sys.argv[2])

  try:
    import PyPDF2
  except ImportError:
    print("PyPDF2 not installed. Run: pip install pypdf2")
    sys.exit(1)

  reader = PyPDF2.PdfReader(str(in_path))
  # Use list comprehension for better performance
  pages = [
    f"\n\n---\n\n## Page {i}\n\n{page.extract_text() or ''}"
    for i, page in enumerate(reader.pages, start=1)
  ]

  text = clean("".join(pages))
  out_path.write_text("# Converted PDF\n\n" + text + "\n", encoding="utf-8")
  print(f"Wrote: {out_path}")

if __name__ == "__main__":
  main()
