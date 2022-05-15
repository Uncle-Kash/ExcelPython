import openpyxl, pprint

wb = openpyxl.load_workbook('censuspopdata.xlsx')

sheet = wb['Population by Census Tract']
countyData = {}

# TODO: Fill in countyData with each county's population and tracts.

print('Reading rows....')

for row in range(2, sheet.max_row + 1):
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

with open('censusdata.txt', 'a') as file:
    file.write(f"{state},{county},{pop}")