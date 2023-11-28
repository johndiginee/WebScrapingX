import gspread

# Connect Google credentials
google_credentials = gspread.service_account(filename='credentials.json')

# Connect Google Sheet
google_sheet = google_credentials.open('webscrapingx').sheet1

# Update sheet
# google_sheet.update('A1', 'Test update')

# Add rows
google_sheet.append_row(['first', 'second', 'third'])