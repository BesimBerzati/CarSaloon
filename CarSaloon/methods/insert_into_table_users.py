import psycopg2

conn = psycopg2.connect(
    database='carsaloon',
    user='postgres',
    password='Besim123!',
    host='127.0.0.1',
    port='5432'
)

cur = conn.cursor()
table_name = 'users'
columns = 'name, email, password'
values_input = input(f"Enter the values for {columns}, separated by commas: ")
values_list = values_input.split(',')
values_formatted = f"('{values_list[0]}', '{values_list[1]}', '{values_list[2]}')"

# INSERT INTO USERS
def insert_into_table_users(table_name, columns, values):
    cur.execute(f"INSERT INTO {table_name} ({columns}) VALUES {values};")
    conn.commit()


insert_into_table_users(table_name, columns, values_formatted)


# insert_into_table('users', 'name, email, password', "'Besim', 'besim.berzati96@gmail.com', 'Test123!'")
# insert_into_table('users', 'name, email, password', "'Marcin', 'Marcin.Gay@Testmail.com', 'Test1234!'")
# insert_into_table('users', 'name, email, password', "'Blaise', 'BlaiseTest@web.de', 'Test12345!'")