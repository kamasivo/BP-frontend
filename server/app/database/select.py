import psycopg2
from database.config import config

# function to delete whole data from table
def select(table):
    sql = f"SELECT * FROM {table};"
    conn = None
    id = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the delete statement
        cur.execute(sql)
        # fetch data
        records = cur.fetchall()
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
        # return records
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        records = 'error'
    finally:
        if conn is not None:
            conn.close()
            
    
    return records