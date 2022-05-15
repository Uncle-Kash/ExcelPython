from tkinter import W
import openpyxl

wb = openpyxl.load_workbook('example.xlsx')

print(type(wb))

sheets = wb.sheetnames

print(sheets)