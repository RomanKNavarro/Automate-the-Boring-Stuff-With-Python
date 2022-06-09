# passwordBreaker.py - Goes through a dictionary and attempts to use every word to try to dycrypt a file

import PyPDF2, os, sys

os.chdir(r"C:\Coding Shit\myPrograms\ATBS Chapter 13\Password Breaker Project")

dictionary = open(r"C:\Coding Shit\myPrograms\ATBS Chapter 13\Password Breaker Project\dictionary.txt")
words = dictionary.read()
words = words.split('\n')


pdfReader = PyPDF2.PdfFileReader(open(r"C:\Coding Shit\myPrograms\ATBS Chapter 13\Password Breaker Project\encrypted.pdf", 'rb'))

for word in words[3200:]:
   word = word.lower()
   if pdfReader.decrypt(word) != 1: 
      print(word)
   else:
      print(word, 'is the password.')
      sys.exit()
   
for word in words[3200:]:
   if pdfReader.decrypt(word) != 1: 
      print(word)
   else:
      print(word, 'is the password.')
      break


