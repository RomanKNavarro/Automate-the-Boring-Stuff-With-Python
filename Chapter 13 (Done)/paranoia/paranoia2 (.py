import os, sys, PyPDF2, send2trash

directory = r"C:\Coding Shit\myPrograms\Practice Projects\Chapter 13\paranoia (not done)\minutes" 
for folder, subfolders, files in os.walk(directory):
   print('searching in folder: ' + folder)
   for file in files:
      os.chdir(folder)
      if file.endswith('.pdf'):
         print(file)
         with open(os.path.abspath(file), 'rb') as pdf_file:
            try:
               pdf_reader = PyPDF2.PdfFileReader(pdf_file)
               pdf_writer = PyPDF2.PdfFileWriter()
               for page_number in range(pdf_reader.numPages):
                  pdf_writer.addPage(pdf_reader.getPage(page_number))
               pdf_writer.encrypt('warum')
               file_encrypted = file.rstrip('.pdf') + '_encrypted.pdf'
               with open(file_encrypted, 'wb') as pdf_file_encrypted:
                  pdf_writer.write(pdf_file_encrypted)
               print('new file - ' + file_encrypted)
            except PyPDF2.utils.PdfReadError:
               continue
      else:
         continue


 
for folder, subfolders, files in os.walk(directory): 
   for file in files:
      os.chdir(folder)
      if file.endswith('_encrypted.pdf'):
         pdfReader = PyPDF2.PdfFileReader(open(os.path.abspath(file), 'rb'))
         if pdfReader.decrypt('warum') == 1:
            continue
         else:
            print(file + ' has not been encrypted')
      else:
         send2trash.send2trash(file)
         

 
