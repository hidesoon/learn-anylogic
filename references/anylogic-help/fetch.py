#!/usr/bin/env python3
"""Download an AnyLogic Help section and convert it to clean Markdown.

Mirrors the page tree under a given site section (default: /advanced/) into this
folder as `.md` files, stripping the sidebar nav, scripts, styles and feedback
widget. Internal links to other downloaded pages are rewritten to relative `.md`
links; everything else (cross-section links, images) is rewritten to absolute
https URLs so it still resolves when reading the Markdown.

Usage:
    python3 fetch.py [section]      # section defaults to "advanced"

Requires: beautifulsoup4, markdownify  (pip install beautifulsoup4 markdownify)
Re-running is cheap: raw HTML is cached under .cache/ and reused.
"""
import os
import re
import sys
import time
import urllib.request
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor

from bs4 import BeautifulSoup
from markdownify import markdownify as md

SITE = "https://anylogic.help"
HERE = os.path.dirname(os.path.abspath(__file__))
UA = {"User-Agent": "Mozilla/5.0 (docs-mirror; research use)"}


def fetch(url, dest):
    """Download url to dest (cached). Returns the HTML text."""
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        return open(dest, encoding="utf-8", errors="replace").read()
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers=UA)
            html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with open(dest, "w", encoding="utf-8") as f:
                f.write(html)
            return html
        except Exception as e:  # noqa: BLE001
            if attempt == 3:
                print(f"  !! failed {url}: {e}")
                return None
            time.sleep(1.5 * (attempt + 1))


def page_set(index_html, section):
    """All page paths like /<section>/.../foo.html referenced by the index."""
    soup = BeautifulSoup(index_html, "html.parser")
    pages = set()
    for a in soup.find_all("a", href=True):
        resolved = urljoin(f"{SITE}/{section}/index.html", a["href"])
        path = urlparse(resolved).path
        if path.startswith(f"/{section}/") and path.endswith(".html"):
            pages.add(path)
    return pages


def to_md_path(site_path, section):
    """/<section>/code/classes.html -> code/classes.md (relative to this folder)."""
    return re.sub(r"\.html$", ".md", site_path[len(f"/{section}/"):])


def convert(html, site_path, pages, section):
    soup = BeautifulSoup(html, "html.parser")
    content = soup.find(class_="page-content") or soup.find("main")
    if content is None:
        return None
    # drop non-content elements
    for t in content.find_all(["script", "style", "nav", "header", "footer", "noscript"]):
        t.decompose()
    for cls in ["breadcrumb", "table-of-contents", "page-nav", "prev-next"]:
        for e in content.find_all(class_=lambda c, k=cls: c and k in (c if isinstance(c, list) else [c])):
            e.decompose()
    # the "How can we improve this article?" feedback widget. Match by text, but
    # cap the size so we strip the small widget and never the article wrapper
    # (which also contains the phrase). A class-based strip is unsafe: API and
    # function pages use the same dl.params for real parameter lists.
    total_len = len(content.get_text(strip=True))
    cap = min(600, max(1, total_len // 4))
    fb = [e for e in content.find_all(["dl", "div", "form", "section", "aside"])
          if "improve this article" in e.get_text(" ", strip=True).lower()
          and len(e.get_text(" ", strip=True)) <= cap]
    if fb:
        # the largest qualifying element is the widget root; it contains the rest
        max(fb, key=lambda e: len(e.get_text(" ", strip=True))).decompose()

    # Javadoc (API reference) pages are huge: keep the class description + the
    # field/constructor/method *summary* tables, drop the per-member *details*
    # section (~2/3 of the page) and the noisy "inherited from" link lists. This
    # only fires on Javadoc pages; prose guides have no <section class="summary">.
    if content.find("section", class_="summary") or content.find("section", class_="details"):
        det = content.find("section", class_="details")
        if det:
            det.decompose()
        for cls in ("content-nav", "inherited-list"):
            for e in content.find_all(class_=lambda c, k=cls: c and k in (c if isinstance(c, list) else [c])):
                e.decompose()

    base = SITE + site_path
    cur_md = to_md_path(site_path, section)
    cur_dir = os.path.dirname(cur_md)

    for a in content.find_all("a", href=True):
        href = a["href"]
        if href.startswith("#"):
            continue
        resolved = urljoin(base, href)
        path = urlparse(resolved).path
        if path in pages:
            target_md = to_md_path(path, section)
            rel = os.path.relpath(target_md, cur_dir or ".")
            a["href"] = rel + (("#" + urlparse(resolved).fragment) if urlparse(resolved).fragment else "")
        else:
            a["href"] = resolved
    for img in content.find_all("img"):
        src = img.get("data-src") or img.get("src")
        if src:
            img["src"] = urljoin(base, src)
            img.attrs.pop("data-src", None)

    out = md(str(content), heading_style="ATX")
    out = "\n".join(line.rstrip() for line in out.splitlines())
    out = re.sub(r"\n{3,}", "\n\n", out).strip()
    return f"*来源 (Source): <{base}>*\n\n---\n\n{out}\n"


def main():
    section = sys.argv[1] if len(sys.argv) > 1 else "advanced"
    cache = os.path.join(HERE, ".cache")
    index_url = f"{SITE}/{section}/index.html"
    index_html = fetch(index_url, os.path.join(cache, section, "index.html"))
    pages = sorted(page_set(index_html, section))
    print(f"{len(pages)} pages under /{section}/")

    # download (politely parallel)
    def dl(p):
        return p, fetch(SITE + p, os.path.join(cache, p.lstrip("/")))

    htmls = {}
    with ThreadPoolExecutor(max_workers=6) as ex:
        for p, h in ex.map(dl, pages):
            htmls[p] = h

    pages_set = set(pages)
    ok = skipped = 0
    for p in pages:
        h = htmls.get(p)
        if not h:
            skipped += 1
            continue
        md_text = convert(h, p, pages_set, section)
        if md_text is None or "Page not found" in md_text[:300]:
            skipped += 1
            print(f"  skip (no content/404): {p}")
            continue
        dest = os.path.join(HERE, section, to_md_path(p, section))
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w", encoding="utf-8") as f:
            f.write(md_text)
        ok += 1
    print(f"wrote {ok} markdown files, skipped {skipped}")


if __name__ == "__main__":
    main()
