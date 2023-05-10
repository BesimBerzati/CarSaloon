import psycopg2

conn = psycopg2.connect(
    database='carsaloon',
    user='postgres',
    password='Besim123!',
    host='127.0.0.1',
    port='5432'
)

cur = conn.cursor()

table_name = 'maintenance'
columns = 'car_id'
values_input = input(f"Enter the values for {columns}, separated by commas: ")
values_list = values_input.split(',')
values_formatted = f"('{values_list[0]}')"

def insert_into_table_maintenance(table_name, columns, values):
    cur.execute(f"INSERT INTO {table_name} ({columns}) VALUES {values};")
    conn.commit()

insert_into_table_maintenance(table_name, columns, values_formatted)