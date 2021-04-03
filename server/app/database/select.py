import psycopg2
from database.config import config

def select(table):
    sql = f"SELECT * FROM {table};"
    conn = None
    id = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql)
        records = cur.fetchall()
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        records = 'error'
    finally:
        if conn is not None:
            conn.close()
    return records

