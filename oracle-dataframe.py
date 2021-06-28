import os
import sys
import cx_Oracle
import pandas as pd

connection = cx_Oracle.connect("OT", "1234", "192.168.4.188:1521/orcl.example.com")
connection

# query = """SELECT * FROM OT.contacts ORDER BY CONTACT_ID ASC"""
query = """SELECT * FROM contacts ORDER BY CONTACT_ID ASC"""

df_ora = pd.read_sql(query, con=connection)
df_ora
