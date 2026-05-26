"""Generate hero-viewport thumbnails for all 18 TBW case study samples."""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

HERE = Path(__file__).resolve().parent
SAMPLES = HERE / "samples"
THUMBS = HERE / "thumbnails"
THUMBS.mkdir(exist_ok=True)

CONCURRENCY = 3

async def shoot_one(file_path, browser, sem):
    async with sem:
        name = file_path.stem.replace("sample-", "")
        out = THUMBS / f"{name}.png"
        ctx = page = None
        try:
            ctx = await browser.new_context(viewport={"width": 1440, "height": 900}, device_scale_factor=1)
            page = await ctx.new_page()
            await page.goto(file_path.resolve().as_uri(), wait_until="networkidle", timeout=20000)
            await page.wait_for_timeout(800)
            await page.screenshot(path=str(out), full_page=False, type="jpeg", quality=82)
            print(f"  ok: {name}.png ({out.stat().st_size//1024}KB)", flush=True)
        except Exception as e:
            print(f"  FAIL: {name}: {e}", flush=True)
        finally:
            if page:
                try: await page.close()
                except: pass
            if ctx:
                try: await ctx.close()
                except: pass

async def main():
    files = sorted(SAMPLES.glob("sample-*.html"))
    print(f"Rendering {len(files)} thumbnails ({CONCURRENCY} parallel)...")
    sem = asyncio.Semaphore(CONCURRENCY)
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        try:
            await asyncio.gather(*[shoot_one(f, browser, sem) for f in files])
        finally:
            await browser.close()
    print(f"\nDone. Saved to {THUMBS}/")

if __name__ == "__main__":
    asyncio.run(main())
