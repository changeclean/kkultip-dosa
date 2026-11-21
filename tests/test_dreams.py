#!/usr/bin/env python3
"""꿈해몽 300개 생성기 검증: GitHub Actions / 로컬 공용."""
import os
from pathlib import Path
from xml.etree import ElementTree

os.environ.setdefault("SITE_URL", "https://kkultip-dosa.netlify.app")

import build

assert len(build.DREAMS) == 300, f"Expected 300 dream articles, got {len(build.DREAMS)}"
assert len({x["slug"] for x in build.DREAMS}) == 300, "Duplicate dream article slugs"
assert len({x["title"] for x in build.DREAMS}) == 300, "Duplicate dream article titles"
assert len({x["category"] for x in build.DREAMS}) >= 12, "Missing topic groups"

build.build()
root = Path(__file__).resolve().parent.parent / "site"
pages = sorted((root / "dreams").glob("*/index.html"))
assert len(pages) == 300, f"Expected 300 detail pages, got {len(pages)}"

for entry in build.DREAMS:
    f = root / "dreams" / entry["slug"] / "index.html"
    assert f.exists(), f"Missing {f}"
    content = f.read_text(encoding="utf-8")
    assert entry["title"] in content, f"Missing title in {f}"
    assert "rel=\"canonical\"" in content, f"Missing canonical in {f}"
    assert "datePublished" in content, f"Missing article schema in {f}"

index = (root / "dreams" / "index.html").read_text(encoding="utf-8")
assert "총 300개의 글" in index, "Missing catalog count"
assert "cat-entering" in index, "Missing sample link"
search = (root / "search" / "index.html").read_text(encoding="utf-8")
assert "cat-entering" in search, "Missing site search record"

sitemap = root / "sitemap.xml"
assert sitemap.exists(), "Sitemap was not generated"
tree = ElementTree.parse(sitemap)
namespace = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
urls = [n.text for n in tree.findall(".//s:loc", namespace)]
assert len(urls) == len(set(urls)), "Duplicate sitemap entries"
assert sum("/dreams/" in u and not u.endswith("/dreams/") for u in urls) == 300
assert "https://kkultip-dosa.netlify.app/dreams/cat-entering/" in urls

print(f"[OK] {len(pages)} dream pages, {len(urls)} sitemap URLs, search and canonical checked")
