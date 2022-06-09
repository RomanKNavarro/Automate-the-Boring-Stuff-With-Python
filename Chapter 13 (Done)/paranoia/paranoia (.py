import os, PyPDF2, sys


if len(sys.argv) < 2:
   print('paranoina.py - Encrypts all the pdf files in a given directory')    # If directory path not given in run menu

   
else:                                                                         
   for folder, subfolders, files in os.walk(sys.argv[1]):
      print('Searching in %s...' % (folder))
      

      for file in files:
         os.chdir(folder)
         if file.endswith('.pdf'):
            pdfFile = open(file, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            pdfWriter = PyPDF2.PdfFileWriter()                                # search for pdf file, open in rb, create reader and writer objects

            
            for pageNum in range(pdfReader.numPages):
               pdfWriter.addPage(pdfReader.getPage(pageNum))                  # add every page in the file to writer object


            pdfWriter.encrypt(sys.argv[2]) 
            resultPdf = open(newFileName, 'wb')
            pdfWriter.write(resultPdf)
            resultPdf.save(r"C:\Coding Shit\myPrograms\Practice Projects\Chapter 9\Ooga booga 2 encrypted (paranoia.py)")
            resultPdf.close()
            pdfFile.close()                                                   # encrypt writer object with password, create new file, write content
            
            
            
