from PIL import Image
import random

def corrupt_qr(image_path, output_path):
    # Open the image
    img = Image.open(image_path)
    img = img.convert("RGB")  # Ensure the image is in RGB mode
    
    pixels = img.load()  # Get pixel data
    
    # Iterate through every pixel
    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y]
            
            # Randomly change the pixel's color to corrupt the QR code
            if random.random() < 0.3:  # 30% of pixels will be altered
                # Change the pixel color to a random one (not black or white)
                pixels[x, y] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Save the corrupted image
    img.save(output_path)
    print(f"Corrupted QR saved as {output_path}")

# Example usage:
corrupt_qr("original_qr.png", "corrupted_qr_code.png")
