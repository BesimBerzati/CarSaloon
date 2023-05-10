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

values_list_cars[1] = int(values_list_cars[1])
values_list_cars[3] = int(values_list_cars[3])

values_formatted = f"('{values_list_cars[0]}', {values_list_cars[1]}, '{values_list_cars[2]}', {values_list_cars[3]}, '{values_list_cars[4]}', '{values_list_cars[5]}')"

def insert_into_table_cars(table_name, columns, values):
    cur.execute(f"INSERT INTO {table_name} ({columns}) VALUES {values};")
    conn.commit()


insert_into_table_cars(table_name_cars, columns_cars, values_formatted)

cur.close()
conn.close()



# INSERT INTO CARS
# insert_into_table('cars', 'name, price, color, year, model, brand', "'BMW', 40000, 'Black', 2018, 'X5', 'BMW'")
# insert_into_table('cars', 'name, price, color, year, model, brand', "'Mercedes', 30000, 'White', 2018, 'C300', 'Mercedes'")
# insert_into_table('cars', 'name, price, color, year, model, brand', "'Audi', 25000, 'Dark Grey', 2018, 'A4', 'Audi'")

#INSERT INTO USERS
def insert_into_table_users(table_name, columns, values):
    cur.execute(f"INSERT INTO {table_name} ({columns}) VALUES {values};")
    conn.commit()


# insert_into_table('users', 'name, email, password', "'Besim', 'besim.berzati96@gmail.com', 'Test123!'")
# insert_into_table('users', 'name, email, password', "'Marcin', 'Marcin.Gay@Testmail.com', 'Test1234!'")
# insert_into_table('users', 'name, email, password', "'Blaise', 'BlaiseTest@web.de', 'Test12345!'")

#INSERT INTO ORDERS

#INSERT INTO MAINTENANCE

