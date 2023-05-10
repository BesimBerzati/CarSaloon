# SHOW WHAT IS INSIDE EACH TABLE

import psycopg2

conn = psycopg2.connect(
    database='carsaloon',
    user='postgres',
    password='Besim123!',
    host='127.0.0.1',
    port='5432'
)

cur = conn.cursor()

# SHOW WHOLE DATABASE

cars_storage = "Cars Storage"
users_storage = "Users Storage"
orders_storage = "Orders Storage"
maintenance_storage = "Maintenance Storage"
def show_all_data():
    print(cars_storage)
    cur.execute("SELECT * FROM cars;")
    print(cur.fetchall())
    print(users_storage)
    cur.execute("SELECT * FROM users;")
    print(cur.fetchall())
    print(orders_storage)
    cur.execute("SELECT * FROM orders;")
    print(cur.fetchall())
    print(maintenance_storage)
    cur.execute("SELECT * FROM maintenance;")
    print(cur.fetchall())

show_all_data()
