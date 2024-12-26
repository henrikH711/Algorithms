from PIL import Image

# ASCII 
G_SCALE = "@%#*+=-:. "  #   (light -> dark)

def image_to_ascii(image_path, cols=80):
   
    image = Image.open(image_path).convert('L')  # 'L' = Grayscale

    
    W, H = image.size
    aspect_ratio = H / W
    rows = int(cols * aspect_ratio * 0.55) 

    
    image = image.resize((cols, rows))

    # ASCII image 
    ascii_image = ""
    for y in range(rows):
        for x in range(cols):
            pixel_value = image.getpixel((x, y))
            ascii_char = G_SCALE[pixel_value * (len(G_SCALE) - 1) // 255]  # Pixel -> ASCII
            ascii_image += ascii_char

    return ascii_image

image_path = "your_image.jpg" 
ascii_art = image_to_ascii(image_path, cols=100)  
print(ascii_art)
