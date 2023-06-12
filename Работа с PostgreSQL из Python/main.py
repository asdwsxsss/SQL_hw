import psycopg2

def create_db(conn):
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS customers(
        client_id INTEGER UNIQUE PRIMARY KEY,
        first_name VARCHAR(40),
        last_name VARCHAR(60),
        email VARCHAR(60));""")
    cur.execute("""CREATE TABLE IF NOT EXISTS phones(
        id SERIAL PRIMARY KEY,
        client_id INTEGER REFERENCES customers(client_id),
        phone VARCHAR(12));""")
    conn.commit()

def add_client(conn,client_id, first_name, last_name, email, phones=None):
    cur = conn.cursor()
    cur.execute("""
           INSERT INTO customers(client_id, first_name, last_name, email) VALUES(%s, %s, %s, %s);
           """, (client_id, first_name, last_name, email))
    conn.commit()
    cur.execute("""SELECT * FROM customers;""")
    print(cur.fetchall())

    cur.execute("""
           INSERT INTO phones(client_id, phone) VALUES(%s, %s);
           """, (client_id, phones))
    conn.commit()
    cur.execute("""SELECT * FROM phones;""")
    print(cur.fetchall())


def add_phone(conn, client_id, phone):
    cur = conn.cursor()
    cur.execute("""
    UPDATE phones SET phone=%s WHERE client_id=%s;
    """, (phone, client_id))
    conn.commit()


def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
    cur = conn.cursor()
    cur.execute("""
    UPDATE customers SET first_name=%s, last_name=%s, email=%s WHERE client_id=%s;
    """, (first_name, last_name, email, client_id))
    cur.execute("""SELECT * FROM customers;""")
    print(cur.fetchall())
    cur.execute("""
    UPDATE phones SET phone=%s WHERE client_id=%s;
    """, (phones, client_id))
    cur.execute("""SELECT * FROM phones;""")
    print(cur.fetchall())

def delete_phone(conn, client_id):
    cur = conn.cursor()
    cur.execute("""
        DELETE FROM phones WHERE client_id=%s;
        """, (client_id,))
    cur.execute("""SELECT * FROM phones;""")
    print(cur.fetchall())

def delete_client(conn, client_id):
    cur = conn.cursor()
    cur.execute("""
        DELETE FROM customers WHERE client_id=%s;
        """, (client_id,))
    cur.execute("""SELECT * FROM customers;""")
    print(cur.fetchall())
    cur.execute("""
        DELETE FROM phones WHERE client_id=%s;
        """, (client_id,))
    cur.execute("""SELECT * FROM phones;""")
    print(cur.fetchall())

def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM customers c JOIN phones p ON c.client_id WHERE first_name=%s OR last_name=%s OR email=%s OR p.phone=%s
        """, (first_name,last_name,email, phone))
    print(cur.fetchall())

with psycopg2.connect(database="postgres", user="postgres", password="Zxcvb425") as conn:
    create_db(conn)
    add_client(conn, 1, 'Nat', 'Ivanova', 'Iv.nat@mail.ru', '+79243152364')
    add_client(conn, 2, 'Max', 'Petrov', 'petrov@gmail.com')
    add_client(conn, 3, 'Alex', 'Lopuhin', 'LopAl@mail.ru', '+73542694456')
    add_client(conn, 4, 'Alexandra', 'Lopuhina', 'LopAlexandra@mail.ru', '+73542654456')
    add_phone(conn, 2, '+72362211236')
    change_client(conn, 1, 'Masha', 'Knayb', 'KnaybM.@gmail.com', '+79642366599')
    delete_phone(conn, 1)
    delete_client(conn, 4)
    find_client(conn, first_name='Nat')
    find_client(conn, email='petrov@gmail.com')

conn.close()