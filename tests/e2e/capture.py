"""@brief Take one screenshot per lecture step with a headless browser.

@details Runs inside a container, never on the host desktop; see capture.sh.
"""

import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

API_URL = "https://potterapi-fedeperin.vercel.app/en/characters"

STEPS: list[tuple[str, str]] = [
    ("step-1-choose-api.png", API_URL),
    ("step-2-all-characters.png", "http://hp-online:5000/"),
    ("step-3-house-filter.png", "http://hp-online:5000/house/gryffindor"),
    ("step-4-character-page.png", "http://hp-online:5000/character/0"),
    ("step-5-api-unavailable.png", "http://hp-offline:5000/"),
]


def main(out_dir: str) -> None:
    """@brief Capture every step into `out_dir`.

    @param out_dir Folder that receives the PNG files.
    """
    target = Path(out_dir)
    target.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page(viewport={"width": 1100, "height": 700})
        for name, url in STEPS:
            page.goto(url, wait_until="domcontentloaded", timeout=90000)
            page.wait_for_timeout(5000)
            page.screenshot(path=str(target / name))
        browser.close()


if __name__ == "__main__":
    main(sys.argv[1])
