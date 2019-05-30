import cassandra

#Create connection
from cassandra.cluster import cluster
try:
    cluster = cluster(['127.0.01'])
    session = cluster.connect()
except Exception as e:
    print(e)

#create keyspace
try:
    session.execute("""CREATE KEYSPACE IF NOT EXISTS udcity
                    WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 1 }"""
)
except Exception as e:
    print(e)

#connect to KEYSPACE
try:
    session.set_keyspace('udacity')
except Exception as e:
    print(e)



#creating tables
query = "CREATE TABLE IF NOT EXISTS music_libary "
query = query + "(year int, artist_name text, album_name text, PRIMARY KEY (year, artist_name))"
try:
    session.execute(query)
except Exception as e:
    print(e)

query = "CREATE TABLE IF NOT EXISTS album_library "
query = query + "(year int, artist_name text, album_name text, PRIMARY KEY (artist_name, year))"
try:
    session.execute(query)
except Exception as e:
    print(e)

#inserting data
query = "INSERT INTO music_libary (year, artist_name, album_name)"
query = query + "VALUES (%s, %s, %s)"

try:
    session.execute(query, (1970, "The Beatles", "Let it be"))
except Exception as e:
    print(e)


#Validate the data model
query = "select * from music_libary WHERE YEAR =1970"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)

for row in rows:
    print(row.year, row.artist_name, row.album_name)


#droping the tables
query = "drop table music_libary"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)
