from tkinter import W
import openpyxl

wb = openpyxl.load_workbook('example.xlsx')

print(type(wb))

sheets = wb.sheetnames

print(sheets)

sheet1 = wb['Sheet1']

myLocation = sheet1['A1']

print(myLocation.value)
print(myLocation.row)
print(myLocation.column)
print(myLocation.coordinates)