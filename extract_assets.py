from PIL import Image
import os

def extract_assets(input_path):
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found.")
        return

    with Image.open(input_path) as img:
        # 1. Logo Banner (Top) - Refined to purple box
        logo_box = (255, 40, 1895, 1415)
        logo_img = img.crop(logo_box)
        logo_img.save("logo_banner.png")
        print(f"Saved logo_banner.png: {logo_img.size}")

        # 2. Candle Business Card (Bottom Left) - Moved up to include text
        candle_box = (70, 1640, 1280, 2730)
        candle_img = img.crop(candle_box)
        candle_img.save("business_card_candles.png")
        print(f"Saved business_card_candles.png: {candle_img.size}")

        # 3. Astrology Business Card (Bottom Right) - Moved up to include text
        astrology_box = (1380, 1640, 2500, 2750)
        astrology_img = img.crop(astrology_box)
        astrology_img.save("business_card_astrology.png")
        print(f"Saved business_card_astrology.png: {astrology_img.size}")

        # 4. Hero Circle (Just the hands and light)
        # Based on the logo box (255, 40, 1895, 1415)
        # The circle is roughly in the middle
        circle_box = (610, 310, 1430, 1130)
        circle_img = img.crop(circle_box)
        # Convert to WebP immediately for hero use
        circle_img.save("hero_circle.webp", "WEBP", quality=90)
        print(f"Saved hero_circle.webp: {circle_img.size}")

if __name__ == "__main__":
    scan_path = r"c:\Users\transmacsual\projects\crystal\Scan_20260317 (2).png"
    extract_assets(scan_path)
