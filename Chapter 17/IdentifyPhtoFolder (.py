#! python3
# TODO: Import modules and write comments to describe this program
from PIL import Image
import os

for foldername, subfolders, filenames in os.walk('C:\\'):
   numPhotoFiles = 0
   numNonPhotoFiles = 0


   os.chdir(foldername)

   for filename in filenames:
      # TODO: Check if file extension isn't .png or .jpg.
      if not (filename.endswith('.png') or filename.endswith('.jpg')):
         numNonPhotoFiles += 1
         continue    # skip to next filename

      
      
      # TODO: Open image file using Pillow.
      
      #fullPath = os.path.join(foldername, filename)
      #print(fullPath)
      # im = Image.open(os.path.basename(fullPath))
      #im = Image.open(os.path.abspath(fullPath))
      im = Image.open(filename)
      width, height = im.size


      # TODO: Check if width & height are larger than 500.
      if width > 500 and height > 500:
         # TODO: Image is large enough to be considered a photo.
         numPhotoFiles += 1
      else:
         # Image is too small to be a photo.
         numNonPhotoFiles += 1
         

   # TODO: If more than half of files were photos, print the absolute path of the folder.
   if numPhotoFiles > (numPhotoFiles + numNonPhotoFiles) / 2:
      print(os.path.abspath(foldername))
