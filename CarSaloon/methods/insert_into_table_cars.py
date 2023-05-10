import psycopg2

conn = psycopg2.connect(
    database='carsaloon',
    user='postgres',
    password='Besim123!',
    host='127.0.0.1',
    port='5432'
)

cur = conn.cursor()
table_name_cars = 'cars'
columns_cars = 'name, price, color, year, model, brand'
values_input_cars = input(f"Enter the values for {columns_cars}, separated by commas: ")
values_list_cars = values_input_cars.split(',')

values_formatted = f"('{values_list_cars[0]}', {values_list_cars[1]}, '{values_list_cars[2]}', {values_list_cars[3]}, '{values_list_cars[4]}', '{values_list_cars[5]}')"

def insert_into_table_cars(table_name, columns, values):
    cur.execute(f"INSERT INTO {table_name} ({columns}) VALUES {values};")
    conn.commit()


insert_into_table_cars(table_name_cars, columns_cars, values_formatted)

cur.close()
conn.close()


