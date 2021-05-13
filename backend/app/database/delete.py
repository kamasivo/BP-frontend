import psycopg2
from database.config import config

# function to delete whole data from table
def delete(table):
    sql = f"DELETE FROM {table} WHERE 1=1;"
    conn = None
    id = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return id