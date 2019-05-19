import psycopg2

try:
    conn = psycopg2.connect("dbname=udacity")
except psycopg2.Error as e:
    print("Error")
    print(e)

try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print("Error")
    print(e)

conn.set_session(autocommit=True)

# Creating the fact table
try:
    cur.execute("CREATE TABLE IF NOT EXISTS customer_transactions (customer_id int, store_id int, spent numerict);")
except psycopg2.Error as e:
    print("Error")
    print(e)

# Inserting
try:
    cur.execute("INSERT INTO customer_transactions (customer_id, store_id, spent) \
    VALUES (%s, %s, %s)", \
    (1, 1, 20.50))
except psycopg2.Error as e:
    print("error")
    print(e)
try:
    cur.execute("INSERT INTO customer_transactions (customer_id, store_id, spent) \
    VALUES (%s, %s, %s)", \
    (2, 1, 35.21))
except psycopg2.Error as e:
    print("error")
    print(e)


# Creating dimension TABLE
try:
    cur.execute("CREATE TABLE IF NOT EXISTS items_purchased (customer_id int, item_number int, item_name varchar);")
except psycopg2.Error as e:
    print("Error")
    print(e)
try:
    cur.execute("INSERT INTO items_purchased (customer_id, item_number, item_name) \
                VALUES (%s, %s, %s)", \
                (1, 1, "!Rubber Soul"))
except psycopg2.Error as e:
    print("Error")
    print(e)
try:
    cur.execute("INSERT INTO items_purchased (customer_id, item_number, item_name) \
                VALUES (%s, %s, %s)", \
                (2, 3, "Let it be"))
except psycopg2.Error as e:
    print("Error")
    print(e)

# Create 2nd dimension TABLE
try:
    cur.execute("CREATE TABLE IF NOT EXISTS store (sotre_id int, stat varchar);")
except psycopg2.Error as e:
    print("Error")
    print(e)
try:
    cur.execxute("INSERT INTO store (store_id, state) \
                VALUES (%s, %s)", \
                (1, "CA"))
except psycopg2.Error as e:
    print("Error")
    print(e)
try:
    cur.execxute("INSERT INTO store (store_id, state) \
                VALUES (%s, %s)", \
                (2, "WA"))
except psycopg2.Error as e:
    print("Error")
    print(e)

# Creating 3rd dimension TABLE
try:
    cur.execute("CREATE TABLE IF NOT EXISTS customer (customer_id int, name varchar, rewards boolean);")
except psycopg2.Error as e:
    print("Error")
    print(e)
try:
    cur.execute("INSERT INTO customer (customer_id, name, rewards) \
                VALUES (%s, %s, %s, )", \
                (1, "Amanda", True))
except psycopg2.Error as e:
    print("Error")
    print(e)
try:
    cur.execute("INSERT INTO customer (customer_id, name, rewards) \
                VALUES (%s, %s, %s, )", \
                (2, "Toby", False))
except psycopg2.Error as e:
    print("Error")
    print(e)

# Query 1:
try:
    cur.execute("SELECT name, item_name, rewads FROM ((customer_transactions \
                JOIN customer ON customer.customer_id=customer_transactions.customer_id) \
                JOIN items_purchased ON \
                customer_transactions.customer_id=items_purchased.customer_id)\
                WHERE spent > 30 ;")
except psycopg2.Error as e:
    print("Error")
    print(e)

row= cur.fetchone()
while row:
    print(row)
    row = cur.fetchone()

# Query 2:
try:
    cur.execxute("SELECT store_id, SUM(spent) FROM customer_transactions GROUP BY store_id;")
except psycopg2.Error as e:
    print("error")
    print(e)

row = cur.fetchone()
while row:
    print(row)
    row = cur.fetchone()

# Delete talbes
try:
    cur.execute("DROP TABLE customer_transactions")
except psycopg2.Error as e:
    print("Error")
    print(e)

# Close cursor and connection
cur.close()
conn.close()
