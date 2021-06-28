#!python
import os, sys
import cx_Oracle

connection = cx_Oracle.connect("wachira", "At123456", "192.168.6.191/db001.example.com")

connection = cx_Oracle.connect("OT", "1234", "192.168.4.188/orcl.example.com")
cursor = connection.cursor()
cursor

cursor.execute("""SELECT * FROM OT.contacts""")
#cursor
for contact_id, last_name, first_name, address in cursor:
    print(">>> :",contact_id, last_name, first_name, address)
    
    
cursor = connection.cursor()
cursor.execute("""SELECT CUSTOMER_ID, NAME, ADDRESS FROM CUSTOMERS""")

for CUSTOMER_ID, NAME, ADDRESS in cursor:
    print("Values:", CUSTOMER_ID, NAME, ADDRESS)
