import requests
import openpyxl

# Fetch the country list from the API
response = requests.get("https://country-list-1150.azurewebsites.net/api/country")
data = response.json()

# Create a new Excel workbook
workbook = openpyxl.Workbook()
sheet = workbook.active

# Write the headers
sheet["A1"] = "Country Name"
sheet["B1"] = "Capital City"

# Iterate through the country list and write to the spreadsheet
row_num = 2  # Start writing from row 2 (since row 1 has headers)
for country in data:
    try:
        country_name = country["name"]
        capital_city = country["capital"]
        sheet["A" + str(row_num)] = country_name
        sheet["B" + str(row_num)] = capital_city
        row_num += 1
    except KeyError:
        print(f"Missing data for country: {country}")

# Save the spreadsheet
workbook.save("countries_and_capitals.xlsx")

print("Spreadsheet created successfully!")
