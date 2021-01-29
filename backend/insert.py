import psycopg2
from config import config


def insert(ip, os, name, vulns):
    """ insert a new vendor into the vendors table """
    sql = """INSERT INTO devices(ip_address, os, name, num_of_vulns)
             VALUES(%s, %s, %s, %s) RETURNING ip_address;"""
    conn = None
    id = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (ip, os, name, vulns,))
        # get the generated id back
        id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return id