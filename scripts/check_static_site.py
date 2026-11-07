#!/usr/bin/env python3
"""Small dependency-free smoke test for the local static site."""
from pathlib import Path
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parents[1] / "clients" / "web"
REQUIRED = [
    "index.html", "directory.html", "web.html", "safety.html",
    "deployment.html", "donate.html", "auth.html", "ai-promos.html", "favicon.svg", "site.css", "site.js",
]

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []
    def handle_starttag(self, tag, attrs):
        self.hrefs.extend(value for key, value in attrs if key == "href" and value)

for name in REQUIRED:
    path = ROOT / name
    if not path.is_file() or path.stat().st_size == 0:
        raise SystemExit(f"missing required file: {path}")

for page in ROOT.glob("*.html"):
    parser = Links()
    parser.feed(page.read_text(encoding="utf-8"))
    for href in parser.hrefs:
        if href.startswith(("https://", "http://", "mailto:", "#")):
            continue
        target = (page.parent / href.split("#", 1)[0]).resolve()
        if not target.exists():
            raise SystemExit(f"broken local link: {page.name} -> {href}")

print(f"static site OK: {len(list(ROOT.glob('*.html')))} HTML pages checked")
