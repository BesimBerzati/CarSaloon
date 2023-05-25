import psycopg2


conn = psycopg2.connect(
    database='carsaloon',
    user='postgres',
    password='Besim123!',
    host='127.0.0.1',
    port='5432'
)


cur = conn.cursor()

Pick = int(input("Enter 1 to insert data into users table"
                 "\nEnter 2 to insert data into cars table"
                 "\nEnter 3 to insert data into maintenance table"
                 "\nEnter 4 to insert data into orders table"
                 "\nEnter 5 to show all data"
                 "\nEnter 6 to exit"
                 "\nEnter your choice: "))


#Fixed the picks
if Pick == 1:
    from insert_into_table_users import insert_into_table_users
    insert_into_table_users()
elif Pick == 2:
    from insert_into_table_cars import insert_into_table_cars
    insert_into_table_cars()
elif Pick == 3:
    from insert_into_table_maintenance import insert_into_table_maintenance
    insert_into_table_maintenance()
elif Pick == 4:
    from insert_into_table_orders import insert_into_table_orders
    insert_into_table_orders()
elif Pick == 5:
    from show_all_data import show_all_data
    show_all_data()
elif Pick == 6:
    print("Exiting...")
else:
    print("Please enter a valid number from 1 to 6.")

conn.commit()
cur.close()
conn.close()