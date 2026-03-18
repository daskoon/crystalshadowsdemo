from PIL import Image

def get_image_info(image_path):
    with Image.open(image_path) as img:
        print(f"Format: {img.format}")
        print(f"Size: {img.size}")
        print(f"Mode: {img.mode}")
        
        # We can also detect rough bounding boxes by looking for non-white areas
        # but for now let's just output the size so I can calculate coordinates.
        # The scan is likely 300dpi or 600dpi.
        width, height = img.size
        print(f"Width: {width}, Height: {height}")

if __name__ == "__main__":
    get_image_info(r"c:\Users\transmacsual\projects\crystal\Scan_20260317 (2).png")
