from PIL import Image
import os

def optimize_images(image_files):
    for filename in image_files:
        if os.path.exists(filename):
            with Image.open(filename) as img:
                # Convert to WebP with a balance of quality and size
                webp_filename = os.path.splitext(filename)[0] + ".webp"
                img.save(webp_filename, "WEBP", quality=85)
                print(f"Optimized {filename} -> {webp_filename} ({os.path.getsize(webp_filename)} bytes)")

if __name__ == "__main__":
    assets = ["logo_banner.png", "business_card_candles.png", "business_card_astrology.png"]
    optimize_images(assets)
