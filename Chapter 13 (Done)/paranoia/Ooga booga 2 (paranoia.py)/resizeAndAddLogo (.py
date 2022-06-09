#! python3
# resizeAndAddLogo.py - Resizes all images in current working directory to fit
# in a 300X300 square, and adds catlogo.png to the lower-right corner.

import os
from PIL import Image


os.chdir(r"C:\Coding Shit\myPrograms\ATBS Chapter 17\resizeAndAddLogo")


SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

   
os.makedirs('widthLogo', exist_ok= True)
# Loop over all files in the working directory.
for filename in os.listdir('.'):
   if not (filename.endswith('.png') or filename.endswith('.jpg')) \
      or filename == LOGO_FILENAME:
       continue    # skip non-image files and the logo file itself


   im = Image.open(filename)
   width, height = im.size


   # Check if image needs to be resized.
   if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
       # Calculate the new width and height to resize to.
       if width > height:
           height = int((SQUARE_FIT_SIZE / width) * height)
           width = SQUARE_FIT_SIZE
       else:
           width = int((SQUARE_FIT_SIZE / height) * width)
           height = SQUARE_FIT_SIZE
         
         
       print('Resizing %s...' % (filename))
       im = im.resize((width, height))

   
   # Add the logo.
   print('Adding logo to %s...' % (filename))
   im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)         # problem adding logo


   # Save changes
   im.save(os.path.join(r"widthLogo", filename))
