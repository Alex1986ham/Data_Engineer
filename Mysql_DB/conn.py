
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


# Create TABLE
try:
    cur.execute("CREATE TABLE IF NOT EXISTS music_libary(album_id int(10) NOT NULL, album_name varchar(20) NULL, artist_name varchar(20) NULL, year int(5) NULL, songs text(30) NULL)")
    print("3. table created")
except Error as e:
    print("Error: Issue creating table")
    print(e)


# Insert INTO
try:
    cur.execute("INSERT INTO music_libary (album_id, album_name, artist_name, year, songs) \
                VALUES (%s, %s, %s, %s, %s)", \
                (1, "Rubber Soul", "The Beatles", 1965, "Let it be"))
    print("4. inserted")
except Error as e:
    print("Error: Inserting rows")
    print(e)



# confirm the data got inserted
try:
    cur.execute("SELECT * FROM music_libary;")
except Error as e:
    print("Error: select *")
    print(e)

row = cur.fetchone()
while row:
    print(row)
    #row = cur.fetchone
