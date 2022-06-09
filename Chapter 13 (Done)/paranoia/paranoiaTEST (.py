import os, PyPDF2, sys


directory =  "C:\Coding Shit\myPrograms\Practice Projects\Chapter 13\paranoia (not done)\Ooga booga 2 (paranoia.py)"


for folder, subfolders, files in os.walk(directory):
      print('Searching in %s...' % (folder))
      

      for file in files:
         os.chdir(folder)
         if file.endswith('.pdf'):
            pdfFile = open(file, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            pdfWriter = PyPDF2.PdfFileWriter()

            pdfReader.encrypt()
            pdfFile.close()

            

