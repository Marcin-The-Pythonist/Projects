"""
How to use:
Enter two arguments into the terminal:
1. The folder with the JPG files you'd like to convert.
2. Folder name in which converted files are going to be written.
"""
from PIL import Image, ImageFilter
import os 
import sys

img_folder = sys.argv[1]
new_folder = sys.argv[2]
jpg = '.jpg'

if not os.path.exists(new_folder):
    os.makedirs(new_folder)

for file in os.listdir(img_folder):
    img = Image.open(f'./{img_folder}/{file}')
    img.save(f'./{new_folder}/{os.path.splitext(file)[0]}.png')


