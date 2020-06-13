import os
import sqlite3
import pandas as pd

BASE_DIR = os.path.dirname(os.getcwd())
#db_path = os.path.join(BASE_DIR, "db.db")
db_path = 'E:\\TCS_Projects\\bank-rest-api\\restapi\\' + 'db.db'
print(db_path)
con = sqlite3.connect(db_path)
#cur = con.cursor()
df_match = pd.read_sql_query("SELECT * FROM login;", con)
print(df_match)
