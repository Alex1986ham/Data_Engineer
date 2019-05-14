import psycopg2

# Create a connection to the database
try:
  conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
except psycopg2.Error as e:
  print("Error: Could not make connection to the Pstgres database")
  print(e)

# Getting a cursor
try:
  cur = conn.cursor()
 except psycopg2.Error as e:
    print("Error: Could not get cursor to the Database")
    print(e)

conn.set_session(autocomit=True)

try;
  cur.execute("create database orders")
except psycopg2(Error as e:
  print(e)

try:
  conn.close()
except psycopg2.Error as e:
  print(e)

try:
  conn = psycopg2.connect("host=127.0.0.1 dbname=orders user=student password=student")
except psycopg2.Error as e:
  print("Error: Could not make connection to the Postgres dabase")
  print(e)


cur.execute("select * from test")


try:
  cur.execute("CREATE TABLE test (col1 int, col2 int, col3 int);")
except: psycopg2.Error as e:
  print("Error: Issue creating table")
  print(e)

varchar
test
