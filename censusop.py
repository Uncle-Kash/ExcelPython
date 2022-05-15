import openpyxl, pprint

wb = openpyxl.load_workbook('censuspopdata.xlsx')

sheet = wb['Population by Census Tract']
countyData = {}

# TODO: Fill in countyData with each county's population and tracts.

