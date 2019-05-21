
import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(host='192.168.178.22',
                                        database='test',
                                        user='aldudko2',
                                        password='Dudko010914')
    print("Woooorks")
except Error as e:
    print("Error while connection to mysql", e)


try:
    cur = conn.cursor()
except Error as e:
    print("Error: Could not get curser to the Database")
    print(e)



# Create TABLE
try:
    cur.execute("CREATE TABLE IF NOT EXISTS music_libary (album_id int, \
                                                        album_name varchar, artist_name varchar \
                                                        year int, songs text []);")    
except Error as e:
    print("Error: Issue creating table")
    print(e)

# Insert INTO
try:
    cur.execute("INSERT INTO music_libary (album_id, album_name, artist_name, year, songs) \
                VALUES (%s, %s, %s, %s, %s)", \
                (1, "Rubber Soul", "The Beatles", 1965, ["Let it be", "Accross the universe"]))
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
    row = cur.fetchone
