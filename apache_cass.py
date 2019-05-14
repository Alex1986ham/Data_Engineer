import cassandra

# Connection to the database
from cassandra.cluster import Cluster
try:'127.0.0.1'])
    cluster = Cluster(['127.0.0.1']) # if cassandra is locally installed
    session = cluster.connect()
except Exception as e:
    print(e)
    
try:
    session.execute("""select * from music_libary""")
except Exception as e:
    print(e)
    
# Creating Keyspace(database)
try:
    session.execute("""
    CREATE KEYSPACE IF NOT EXISTS udacity
    WITH REPLICATION =
    { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }"""
)
except Exception as e:
    print(e)
    
    
# Establish connection to keyspace
try:
    session.set_keyspace('udacity')
except Exception as e:
    print(e)
    

# Create table
query = "CREATE TABLE IF NOT EXISTS music_library "
query = query + "(year int, artist_name text, album_name text, PRIMARY KEY (year, artist_name))"
