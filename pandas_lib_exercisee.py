import pandas as pd
df = pd.read_csv('example.csv')
df.to_csv('My_output' ,index=False)
pd.read_csv('My_output')

pd.read_excel('Excel_Sample.xlsx',sheet_name='Sheet1')
df.to_excel('Excel_Sample2.xlsx' ,sheet_name='newSheet')
data = pd.read_excel('https://www.fdic.gov/bank/individual/failed/banklist.html')
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:')
df.to_sql('My_table' ,engine)
sqldf = pd.read_sql('My_table',con=engine)