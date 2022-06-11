#! python3
# resizeAndAddLogoEXT.py - On top of processing PNG and JPEG files, will also process Gif and BMP files as well. 
# Case-insensitive-friendly. Will only work on images that are at least twice the height/width of the logo

import os
from PIL import Image
 

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'gaylogo.png'
logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size
os.makedirs('withLogo', exist_ok=True)
extensions = ['.png', 'jpeg', '.gif', '.bmp']


for filename in os.listdir(r"C:\Coding Shit\myPrograms\Practice Projects\Chapter 17\resizeAndAddLogo"):
   if not filename[-4:].lower() in extensions or filename == LOGO_FILENAME:
      continue
   print(filename)
   im = Image.open(filename)
   width, height = im.size


   if width > logoWidth * 2 and height  > logoHeight * 2:
      if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
         if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE

         
         else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

            
         print('Resizing %s...' % (filename))
         im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
         im.save(os.path.join('withLogo', filename))
      
   else:
      print('width/length not bigger than logoWidth * 2')
