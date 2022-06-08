# Spreadsheet is read, and every column's cells are written to a seperate text file

import os, openpyxl
os.chdir(r"C:\Coding Shit\myPrograms\Practice Projects\Chapter 12\spreadsheetToTextFiles\New Files")
wb = openpyxl.load_workbook(r"C:\Coding Shit\myPrograms\Practice Projects\Chapter 12\spreadsheetToTextFiles\censuspopdata.xlsx")
sheet = wb.get_sheet_by_name('Population by Census Tract')
for column in range(2, sheet.max_column + 1):
   textFile = open('%s%s.txt' % ('textFile', column - 1), 'w+')
   for row in range(1, sheet.max_row + 1):
      textFile.write(str(sheet.cell(row=row, column=column).value) + ', ')
   textFile.close()
