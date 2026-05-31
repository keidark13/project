"""Capture 1440x900 viewport thumbnails for the 24 TBW catalog samples."""
from pathlib import Path
from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
OUT = HERE / "thumbnails"
OUT.mkdir(exist_ok=True)

BASE = "http://localhost:8765/sample-site-catalog/samples"

SAMPLES = [
    ("tech-a", "sample-tech-a.html"),
    ("tech-b", "sample-tech-b.html"),
    ("tech-c", "sample-tech-c.html"),
    ("charity-a", "sample-charity-a.html"),
    ("charity-b", "sample-charity-b.html"),
    ("charity-c", "sample-charity-c.html"),
    ("moving-a", "sample-moving-a.html"),
    ("moving-b", "sample-moving-b.html"),
    ("moving-c", "sample-moving-c.html"),
    ("restaurant-a", "sample-restaurant-a.html"),
    ("restaurant-b", "sample-restaurant-b.html"),
    ("restaurant-c", "sample-restaurant-c.html"),
    ("portfolio-a", "sample-portfolio-a.html"),
    ("portfolio-b", "sample-portfolio-b.html"),
    ("portfolio-c", "sample-portfolio-c.html"),
    ("ai-tool-a", "sample-ai-tool-a.html"),
    ("ai-tool-b", "sample-ai-tool-b.html"),
    ("ai-tool-c", "sample-ai-tool-c.html"),
    ("fitness-a", "sample-fitness-a.html"),
    ("fitness-b", "sample-fitness-b.html"),
    ("fitness-c", "sample-fitness-c.html"),
    ("ecommerce-a", "sample-ecommerce-a.html"),
    ("ecommerce-b", "sample-ecommerce-b.html"),
    ("ecommerce-c", "sample-ecommerce-c.html"),
]


def capture(page, name, filename):
    url = f"{BASE}/{filename}"
    try:
        page.goto(url, wait_until="domcontentloaded", timeout=20000)
        try:
            page.wait_for_load_state("networkidle", timeout=1500)
        except Exception:
            pass
        out_path = OUT / f"{name}.png"
        page.screenshot(path=str(out_path), full_page=False, type="png")
        print(f"OK  {name} -> {out_path.name}")
        return True
    except Exception as e:
        print(f"FAIL {name}: {e}")
        return False


def main():
    failed = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1440, "height": 900}, device_scale_factor=1)
        page = context.new_page()
        for name, filename in SAMPLES:
            if not capture(page, name, filename):
                failed.append(name)
        browser.close()
    print(f"\nDone. {len(SAMPLES) - len(failed)}/{len(SAMPLES)} ok. Failed: {failed}")


if __name__ == "__main__":
    main()
