import gspread

# -----------------Google Sheets API Credentials--------------------------#

sheets_acc = gspread.service_account(filename='filename.json')  # filename='client_secret.json'
sheet_id = sheets_acc.open_by_key('1x1sjE6k1bZRS77fQ-8B-LzYdssf_UaGeRyKMrFZYceY')
worksheet = sheet_id.worksheet('Sheet')
