"""@brief Take one screenshot per lecture step with a headless browser.

@details Runs inside a container, never on the host desktop; see capture.sh.
"""

import sys
from pathlib import Path

from playwright.sync_api import Page, sync_playwright
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

NAVIGATION_TIMEOUT_MS = 90000
IMAGES_TIMEOUT_MS = 60000
SETTLE_MS = 1000
API_URL = "https://potterapi-fedeperin.vercel.app/en/characters"

STEPS: list[tuple[str, str]] = [
    ("step-1-choose-api.png", API_URL),
    ("step-2-all-characters.png", "http://hp-online:5000/"),
    ("step-3-house-filter.png", "http://hp-online:5000/house/gryffindor"),
    ("step-4-character-page.png", "http://hp-online:5000/character/0"),
    ("step-5-api-unavailable.png", "http://hp-offline:5000/"),
]


def wait_for_images(page: Page) -> None:
    """@brief Wait until every image of the page has finished loading.

    @details A timeout is tolerated, so a missing picture does not abort the run.

    @param page The page that was just opened.
    """
    try:
        page.wait_for_function(
            "Array.from(document.images).every(i => i.complete)",
            timeout=IMAGES_TIMEOUT_MS,
        )
    except PlaywrightTimeoutError:
        pass
    page.wait_for_timeout(SETTLE_MS)


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
            page.goto(url, wait_until="domcontentloaded", timeout=NAVIGATION_TIMEOUT_MS)
            wait_for_images(page)
            page.screenshot(path=str(target / name))
        browser.close()


if __name__ == "__main__":
    main(sys.argv[1])
