#!/usr/bin/env python3
"""Rewrites the generated blocks of README.md from their sources.

TOOLS     simonvedder.com/tools/tools.json, the catalogue the tools site renders from
RELEASES  the newest GitHub release of each own public repository
UPSTREAM  pull requests by simon-vedder in repositories he does not own
BLOG      the WordPress REST API of simonvedder.com

Each block sits between <!-- NAME:START --> and <!-- NAME:END --> markers; everything outside
the markers is written by hand. Runs on Mondays from .github/workflows/refresh-readme.yml and by
hand with `python3 .github/scripts/refresh_readme.py` (GITHUB_TOKEN is optional and only raises
the rate limit; on a Mac the python.org build has no CA bundle, /usr/bin/python3 does). Any fetch
that fails aborts the run before the file is touched, so a broken source never empties a block.
"""
import html
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

USER = "simon-vedder"
SITE = "https://simonvedder.com"
TOOLS_JSON = f"{SITE}/tools/tools.json"
POSTS_API = f"{SITE}/wp-json/wp/v2/posts?per_page=3&_fields=title,link,date"
API = "https://api.github.com"
README = Path(__file__).resolve().parents[2] / "README.md"

TIER_LABEL = {
    "automation": "Automation",
    "scanner": "Audit",
    "free": "Web app",
    "blueprint": "Blueprint",
    "product": "Product",
}
# What a tool ships as when the catalogue carries no technology tag for it.
TIER_SHIPS = {"free": "Browser"}


def fetch_json(url):
    headers = {"Accept": "application/json", "User-Agent": f"{USER}-profile-readme"}
    token = os.environ.get("GITHUB_TOKEN")
    if token and url.startswith(API):
        headers["Authorization"] = f"Bearer {token}"
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30) as r:
        return json.load(r)


def cell(text):
    return text.replace("|", "\\|").replace("\n", " ").strip()


def tools_block():
    data = fetch_json(TOOLS_JSON)
    rows = ["| Tool | Kind | What it does | Ships as |", "|---|---|---|---|"]
    for t in data["tools"]:
        # The profile lists what has source. The hosted product has its own site.
        if not t.get("repo"):
            continue
        ships = [t.get("tag") or TIER_SHIPS.get(t["tier"], TIER_LABEL.get(t["tier"], t["tier"]))]
        if t.get("status") == "preview":
            ships[0] += " (preview)"
        if t.get("hasPage"):
            ships.append(f"[page]({urllib.parse.urljoin(SITE, t['url'])})")
        if t.get("gallery"):
            ships.append(f"[Gallery]({t['gallery']})")
        rows.append(
            f"| **[{cell(t['name'])}]({t['repo']})** | {TIER_LABEL.get(t['tier'], t['tier'])} "
            f"| {cell(t['summary'])} | {' · '.join(ships)} |"
        )
    skills = data.get("skills") or {}
    if skills.get("names"):
        rows += ["", f"Claude Code skills in **[skills]({skills['repo']})**: " + " · ".join(f"`{n}`" for n in skills["names"])]
    return "\n".join(rows)


def releases_block(limit=5):
    repos = fetch_json(f"{API}/users/{USER}/repos?per_page=100&type=owner&sort=pushed")
    found = []
    for repo in repos:
        if repo["fork"] or repo["archived"] or repo["private"]:
            continue
        latest = fetch_json(f"{API}/repos/{repo['full_name']}/releases?per_page=1")
        if latest and not latest[0]["draft"]:
            found.append((latest[0]["published_at"], repo, latest[0]))
    found.sort(key=lambda x: x[0], reverse=True)
    lines = []
    for published, repo, rel in found[:limit]:
        # Module releases are named ("AzureInPlaceUpgrade 0.3.1-preview"); a bare tag gets the repo in front.
        name = rel["name"] if rel["name"] and rel["name"] != rel["tag_name"] else f"{repo['name']} {rel['tag_name']}"
        lines.append(f"- [{cell(name)}]({rel['html_url']}) · [{repo['name']}]({repo['html_url']}) · {published[:10]}")
    return "\n".join(lines) if lines else "- Nothing tagged yet."


def upstream_block(limit=8):
    q = urllib.parse.quote(f"is:pr author:{USER} -user:{USER}")
    items = fetch_json(f"{API}/search/issues?q={q}&sort=created&order=desc&per_page=30")["items"]
    lines = []
    for pr in items:
        merged = bool((pr.get("pull_request") or {}).get("merged_at"))
        if pr["state"] != "open" and not merged:
            continue  # closed without merge is nobody's showcase
        repo = pr["repository_url"].removeprefix(f"{API}/repos/")
        state = "merged" if merged else "open"
        lines.append(f"- [{repo} #{pr['number']}]({pr['html_url']}): {cell(pr['title'])} · {state}")
        if len(lines) == limit:
            break
    return "\n".join(lines) if lines else "- No upstream pull requests at the moment."


def blog_block():
    posts = fetch_json(POSTS_API)
    return "\n".join(
        f"- [{cell(html.unescape(p['title']['rendered']))}]({p['link']}) · {p['date'][:10]}" for p in posts
    )


def replace_block(text, name, body):
    pattern = re.compile(rf"<!-- {name}:START -->.*?<!-- {name}:END -->", re.S)
    if not pattern.search(text):
        sys.exit(f"README has no {name} block")
    return pattern.sub(lambda _: f"<!-- {name}:START -->\n{body}\n<!-- {name}:END -->", text)


def main():
    blocks = {
        "TOOLS": tools_block(),
        "RELEASES": releases_block(),
        "UPSTREAM": upstream_block(),
        "BLOG": blog_block(),
    }
    original = README.read_text(encoding="utf-8")
    text = original
    for name, body in blocks.items():
        text = replace_block(text, name, body)
    if text == original:
        print("README already current.")
        return
    README.write_text(text, encoding="utf-8")
    print("README updated: " + ", ".join(blocks))


if __name__ == "__main__":
    main()
