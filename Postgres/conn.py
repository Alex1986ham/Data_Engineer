import psycopg2
from flask import Flask, render_template, json, request

app = Flask(__name__)

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
    cur.execute("CREATE TABLE IF NOT EXISTS name_form (id serial, vorname text, nachname text, alter int, mw boolean);")
except psycopg2.Error as e:
    print("Error")
    print(e)




@app.route('/', methods=['GET'])
def main():
    try:
        cur.execute("SELECT * FROM name_form;")
    except psycopg2.Error as e:
        print("Error: select *")
        print(e)

    #data = cursor.fetchall()
    row = cur.fetchall()
    return render_template('index.html', value=row)



@app.route('/', methods=['GET', 'POST'])
def my_form_post():
    vorname = request.form['vorname']
    nachname = request.form['nachname']
    alter = request.form['alter']
    mw = request.form['mw']

    cur.execute("INSERT INTO name_form (vorname, nachname, alter, mw) \
    VALUES (%s, %s, %s, %s)", \
    (vorname, nachname, alter, mw))

    #vorname = Vorname
    #nachname = nachname
    #alter = alter
    try:
        cur.execute("SELECT * FROM name_form;")
    except psycopg2.Error as e:
        print("Error: select *")
        print(e)

    #data = cursor.fetchall()
    row = cur.fetchall()

    idToDelete = request.form['delete_row']

    try:
        cur.execute("DELETE FROM name_form WHERE id = %s", (idToDelete))
    except psycopg2.Error as e:
        print("delte Error")
        print(e)

    return render_template('index.html', vorname=vorname, nachname=nachname, alter=alter, value=row, idToDelete=delete_row)

"""
@app.route('/', methods=['POST'])
def deleteCategory(delete_row):
    categoryToDelete = session.query(name_form).filter_by(id=delete_row).one()
    if request.method == 'POST':
        session.delete(categoryToDelete)
        return redirect(url_for('index.html', delete_row=delete_row))
    else:
        return render_template('index.html', delte_row=delete_row)


    try:
        _customer_id = request.form['customer_id']

        cur.execute("INSERT INTO customer (customer_id, name, rewards) \
        VALUES (%s, %s, %s)", \
        (_customer_id, 'testname', True))
    except psycopg2.Error as e:
        print("error")
        print(e)

    return render_template('index.html', row=row)





#while row:
#    print(row)
#    row = cur.fetchone


# Creating the fact table
try:
    cur.execute("CREATE TABLE IF NOT EXISTS customer_transactions (customer_id int, store_id int, spent numeric);")
    print("3. created table")
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
    cur.execute("CREATE TABLE IF NOT EXISTS store (store_id int, state varchar);")
except psycopg2.Error as e:
    print("Error")
    print(e)
try:
    cur.execute("INSERT INTO store (store_id, state) \
                VALUES (%s, %s)", \
                (1, "CA"))
except psycopg2.Error as e:
    print("Error")
    print(e)
try:
    cur.execute("INSERT INTO store (store_id, state) \
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
                VALUES (%s, %s, %s)", \
                (1, "Amanda", True))
except psycopg2.Error as e:
    print("Error")
    print(e)
try:
    cur.execute("INSERT INTO customer (customer_id, name, rewards) \
                VALUES (%s, %s, %s)", \
                (2, "Toby", False))
except psycopg2.Error as e:
    print("Error")
    print(e)



# Query 1:
try:
    cur.execute("SELECT name, item_name, rewards FROM ((customer_transactions \
                JOIN customer ON customer.customer_id=customer_transactions.customer_id) \
                JOIN items_purchased ON \
                customer_transactions.customer_id=items_purchased.customer_id)\
                WHERE spent > 30 ;")
except psycopg2.Error as e:
    print("Error")
    print(e)

# Query 2:
try:
    cur.execute("SELECT store_id, SUM(spent) FROM customer_transactions GROUP BY store_id;")
except psycopg2.Error as e:
    print("error")
    print(e)

# Delete talbes
try:
    cur.execute("DROP TABLE customer_transactions")
except psycopg2.Error as e:
    print("Error")
    print(e)

# Close cursor and connection



"""

#cur.close()
#conn.close()

if __name__ == "__main__":
    app.run(port=5002)
