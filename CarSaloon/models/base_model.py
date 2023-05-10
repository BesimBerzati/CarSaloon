import psycopg2

class BaseModel():

    def conn_db(self):
        conn = psycopg2.connect(
        database='carsaloon',
        user='postgres', 
        password='Besim123!',
        host='127.0.0.1',
        port='5432'
        )
        return conn