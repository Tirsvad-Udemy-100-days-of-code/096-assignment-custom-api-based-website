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

VISIBLE_ORIGIN = "http://127.0.0.1:5000"
URL_BAR_HEIGHT_PX = 32
URL_BAR_SCRIPT = """
([text, height]) => {
    const bar = document.createElement("div");
    bar.textContent = text;
    bar.style.cssText = [
        "position:fixed", "top:0", "left:0", "right:0",
        `height:${height}px`, `line-height:${height}px`,
        "padding:0 12px", "background:#e8e8e8",
        "border-bottom:1px solid #bbb", "color:#333",
        "font:14px monospace", "z-index:2147483647",
    ].join(";");
    document.body.appendChild(bar);
    document.body.style.paddingTop = `${height}px`;
}
"""

# (file name, URL to open, whether to draw an address-bar strip with the page path)
STEPS: list[tuple[str, str, bool]] = [
    ("step-1-choose-api.png", API_URL, False),
    ("step-2-all-characters.png", "http://hp-online:5000/", False),
    ("step-3-house-filter.png", "http://hp-online:5000/house/gryffindor", True),
    ("step-4-character-page.png", "http://hp-online:5000/character/0", False),
    ("step-5-api-unavailable.png", "http://hp-offline:5000/", False),
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


def show_url(page: Page) -> None:
    """@brief Draw an address-bar strip at the top of the page.

    @details A headless screenshot has no address bar, so the visible form of
    the address (host 127.0.0.1:5000) is injected and the content pushed down.

    @param page The page that is about to be captured.
    """
    path = page.evaluate("location.pathname")
    page.evaluate(URL_BAR_SCRIPT, [VISIBLE_ORIGIN + path, URL_BAR_HEIGHT_PX])


def main(out_dir: str) -> None:
    """@brief Capture every step into `out_dir`.

    @param out_dir Folder that receives the PNG files.
    """
    target = Path(out_dir)
    target.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page(viewport={"width": 1100, "height": 700})
        for name, url, with_url in STEPS:
            page.goto(url, wait_until="domcontentloaded", timeout=NAVIGATION_TIMEOUT_MS)
            wait_for_images(page)
            if with_url:
                show_url(page)
            page.screenshot(path=str(target / name))
        browser.close()


if __name__ == "__main__":
    main(sys.argv[1])
