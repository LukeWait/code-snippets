from PIL import Image, ImageOps
import os

def add_border(input_image_path, output_image_path, border_size, color):
    img = Image.open(input_image_path)
    img_with_border = ImageOps.expand(img, border=border_size, fill=color)
    img_with_border.save(output_image_path)
    
base_path = "F:/IT Shit"  
add_border(base_path + '/messagebox3.png', base_path + '/messagebox3_border.png', 1, '#4a4a4a')

