#! python3
# Tabulates population and number of census tracts per county

import openpyxl, pprint

print("Opening workbook..")
wb = openpyxl.load_workbook("../automate_online-materials/censuspopdata.xlsx")
sheet = wb.get_sheet_by_name("Population by Census Tract")
countyData = {}

# Collect data
for row in range(2, sheet.max_row + 1):
    state = sheet["B" + str(row)].value
    county = sheet["C" + str(row)].value
    pop = sheet["D" + str(row)].value

    # Set default values: setdefault() will do nothing if a value has been previously set
    countyData.setdefault(state, {})
    countyData[state].setdefault(county, {"tracts": 0, "pop": 0})

    # Increment tract count by 1
    countyData[state][county]["tracts"] += 1
    # Add population
    countyData[state][county]["pop"] += int(pop)

# Write results to a text file
print("Writing results")
resultFile = open("census2010.py", "w")
resultFile.write("allData = " + pprint.pformat(countyData))
resultFile.close()
print("Done")
