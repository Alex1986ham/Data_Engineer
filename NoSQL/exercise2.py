import cassandra

try:
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
except Exception as e:
    print(e)


#create keyspace
try:
    session.execute("""CREATE KEYSPACE IF NOT EXISTS udacity
                    WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 1 }"""
                    )
except Exception as e:
    print(e)

#Connection
try:
    session.set_keyspace('udacity')
except Exception as e:
    print(e)

#creating table
query = "CREATE TABLE IF NOT EXISTS music_libary "
query = query + "(year int, artist_name text, album_name text, city text, PRIMARY KEY (year, album_name ))"
try:
    session.execute(query)
except Exception(query)
    print(e)

#insert data
query = "INSERT INTO music_libary (year, artist_name, album_name, city)"
query = query + " VALUES (%s, %s, %s, %s)"

try:
    session.execute(query, (1970, "The BEATLES", "Let it be", "Liverpool"))
except Exception as e:
    print(e)

#query
query = "select * from music_libary WHERE YEAR=1965"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)

for row in rows:
    print(row.year, row.artist_name, row.album_name, row.city)
