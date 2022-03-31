import pandas as pd
from datetime import datetime

localExcelFile = 'F:\Desktop\EmployeeMySQL.xlsx'

df = pd.read_excel(localExcelFile, sheet_name = 0)

dfNumberScrub = df[df['Mobile'].notna()]
dfColumnScrub = dfNumberScrub.filter(['Name', 'Mobile', 'Extension', 'email', 'Title'])
dfColumnScrub = dfColumnScrub.set_index('Name')

now = datetime.now()
currentDate = now.strftime('%b-%Y')

dfColumnScrub.to_csv('Contacts_' + currentDate + '.csv')