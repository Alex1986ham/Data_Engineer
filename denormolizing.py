import psycopg2

# Connection, cursor, autocommit
try:
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=studet password=pass")
except psycopg2.Error as e:
    print("Print Error")
    print(e)
try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print("error")
    print(e)
conn.set_session(autocommit=True)


try:
    cur.execute("")
    
