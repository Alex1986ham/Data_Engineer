import psycopg2

# Create connection, get cursor, set autocommit
try:
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=passwd")
except psycopg2.Error as e:
    print("Error: Could not make connection to the Postgres database")
    print(e)

try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print("Error: Could not get curser to the Database")
    print(e)

conn.set_session(autocomit=True)


# Create TABLE
try:
    cur.execute("CREATE TABLE IF NOT EXISTS music_libary (album_id int, \
                                                        album_name varchar, artist_name varchar \
                                                        year int, songs text []);")

except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)

# Insert INTO
try:
    cur.execute("INSERT INTO music_libary (album_id, album_name, artist_name, year, songs) \
                VALUES (%s, %s, %s, %s, %s)", \
                (1, "Rubber Soul", "The Beatles", 1965, ["Let it be", "Accross the universe"]))
except psycopg2.Error as e:
    print("Error: Inserting rows")
    print(e)

# confirm the data got inserted
try:
    cur.execute("SELECT * FROM music_libary;")
except psycopg2.Error as e:
    print("Error: select *")
    print(e)

row = cur.fetchone()
while row:
    print(row)
    row = cur.fetchone
