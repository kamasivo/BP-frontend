import psycopg2
from database.config import config


def insert(ip, os, name, vendor, osFamily, osGen, vulns, openPorts):
    """ insert a new device into the device table """
    sql = """INSERT INTO devices(ip_address, os, name, num_of_vulns, vendor, os_family, os_gen, open_ports)
             VALUES(%s, %s, %s, %s, %s, %s, %s, %s) RETURNING ip_address;"""
    conn = None
    id = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (ip, os, name, vulns, vendor, osFamily, osGen, openPorts, ))
        id = cur.fetchone()[0]
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return id


def insertPort(port, ip):
    """ insert a new port into the port table """
    sql = """INSERT INTO ports(port_number, ip_address)
             VALUES(%s, %s);"""
    conn = None
    id = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (port, ip, ))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return id