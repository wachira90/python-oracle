#!python
import cx_Oracle
import pandas as pd
from pandas import DataFrame, read_csv

dataset = pd.read_csv("C:\\pathToFile\\denemedf.txt", delimiter=",")
con = cx_Oracle.connect('uname/pwd@serverName:port/instanceName')
cursor = con.cursor()

sql='insert into gnl.tbl_deneme values(:1,:2,:3,:4,:5,:6)'
df_list = dataset.values.tolist()
n = 0
for i in dataset.iterrows():
    cursor.execute(sql,df_list[n])
    n += 1

con.commit()
