from PIL import Image
import os


for folder, subfolders, filenames in os.walk(r"C:\Coding Shit\myPrograms\ATBS Chapter 17"):
   photoFiles = 0
   nonPhotoFiles = 0
   for filename in filenames:
      if not filename.endswith('.png') or not filename.endswith('.jpg'):
         nonPhotoFiles += 1
         continue

      
      imageFile = Image.open(filename)
      width, height = imagefile.siz
      if width and height < 500:
         photoFiles += 1
      else:
         nonPhotoFiles += 1
   if photoFiles > nonPhotoFiles:
      print(folder)
         
