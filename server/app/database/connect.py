# this method check id database is connected successfully
import psycopg2
from database.config import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        params = config()

        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		
        cur = conn.cursor()
    
        cur.execute('SELECT version()')

        db_version = cur.fetchone()
       
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection is successfull.')


if __name__ == '__main__':
    connect()