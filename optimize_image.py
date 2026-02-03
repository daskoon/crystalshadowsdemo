from PIL import Image
import os

try:
    img = Image.open("space.png")
    # Resize if massive (optional, but good for 8MB files)
    if img.width > 1920:
        ratio = 1920 / img.width
        new_height = int(img.height * ratio)
        img = img.resize((1920, new_height), Image.Resampling.LANCZOS)
    
    img.save("space.webp", "WEBP", quality=80, optimize=True)
    print(f"Success! Optimized space.webp created.")
    print(f"Original size: {os.path.getsize('space.png') / 1024 / 1024:.2f} MB")
    print(f"New size: {os.path.getsize('space.webp') / 1024 / 1024:.2f} MB")
except Exception as e:
    print(f"Error: {e}")
