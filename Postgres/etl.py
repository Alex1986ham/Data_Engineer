import os
import glob
import psycopg2
import pandas as pd


try:
    conn = psycopg2.connect("host=127.0.0.1 dbname=test user=postgres password=Dudko$010914")
    print("1. works")
except psycopg2.Error as e:
    print("Error")
    print(e)

try:
    cur = conn.cursor()
    print("2. cursor works")
except psycopg2.Error as e:
    print("Error")
    print(e)

conn.set_session(autocommit=True)

try:
    cur.execute("CREATE TABLE IF NOT EXISTS artists (artist_id text PRIMARY KEY, name text NOT NULL, location text, lattitude float8, longitude float8);")
except psycopg2.Error as e:
    print("Error")
    print(e)

def get_files(filepath):
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))
    return all_files

song_files = get_files('data')
print(song_files[1])

filepath = song_files[3]

df = pd.read_json(filepath, lines=True)
df.head()

# Auslesen einer Zeile aus der Json
song_data = df[['song_id', 'title', 'artist_id', 'year', 'duration']].values[0].tolist()
print(song_data)

artist_data = df[['artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude']].values
artist_data = artist_data[0].tolist()

print(artist_data)


artist_table_insert = ("""INSERT INTO artists (artist_id, name, location, lattitude, longitude) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (artist_id) DO NOTHING""")
cur.execute(artist_table_insert, artist_data)


conn.close()
