
import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(host='192.168.178.22',
                                        database='test',
                                        user='aldudko2',
                                        password='Dudko010914')
    print("1. Woooorks")
except Error as e:
    print("Error while connection to mysql", e)



try:
    cur = conn.cursor()
    print("2. cursor ok")
except Error as e:
    print("Error: Could not get curser to the Database")
    print(e)

conn.autocommit=True


try:
    cur.execute("SELECT * FROM music_libary;")
except Error as e:
    print("Error: select *")
    print(e)

row = cur.fetchone()
for rows in row:
    print(row)
    #row = cur.fetchone()
#while row:
#    print(row)
    #row = cur.fetchone
