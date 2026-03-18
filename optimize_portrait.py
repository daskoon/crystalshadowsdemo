from PIL import Image
import os

try:
    img = Image.open("newphoto.png")
    # Resize if massive (optional)
    if img.width > 1920:
        ratio = 1920 / img.width
        new_height = int(img.height * ratio)
        img = img.resize((1920, new_height), Image.Resampling.LANCZOS)
    
    img.save("newphoto.webp", "WEBP", quality=85, optimize=True)
    print(f"Success! Optimized newphoto.webp created.")
    print(f"Original size: {os.path.getsize('newphoto.png') / 1024 / 1024:.2f} MB")
    print(f"New size: {os.path.getsize('newphoto.webp') / 1024 / 1024:.2f} MB")
except Exception as e:
    print(f"Error: {e}")
