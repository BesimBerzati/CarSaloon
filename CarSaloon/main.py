import psycopg2

conn = psycopg2.connect(
    database='carsaloon',
    user='postgres',
    password='Besim123!',
    host='127.0.0.1',
    port='5432'
)


cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS cars (id serial PRIMARY KEY, name VARCHAR(255), price INT, color VARCHAR(255), year INT, model VARCHAR(255), brand VARCHAR(255));")
cur.execute("CREATE TABLE IF NOT EXISTS users (id serial PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), password VARCHAR(255));")
cur.execute("CREATE TABLE IF NOT EXISTS orders (id serial PRIMARY KEY, user_id INT, car_id INT, FOREIGN KEY (user_id) REFERENCES users (id), FOREIGN KEY (car_id) REFERENCES cars (id));")
cur.execute("CREATE TABLE IF NOT EXISTS maintenance (id serial PRIMARY KEY, car_id INT, FOREIGN KEY (car_id) REFERENCES cars (id));")

conn.commit()
cur.close()
conn.close()


