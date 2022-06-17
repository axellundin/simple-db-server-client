from config import config
import psycopg2
#import datetime

class TableError(Exception):
    pass

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    return conn, cur
    
def close_commit(conn, cur):
    """ Close cursor, commit the changes and close the connection """
    cur.close()
    conn.commit()
    conn.close()

def execute_query(query):
    """ Execute a query to the database """
    conn, cur = connect()
    cur.execute(query)
    close_commit(conn, cur)

def delete_data(table_name, t):
    """ Delete data from the table """
    delete_query = f"DELETE FROM {table_name} WHERE timestamp = '{t}' "
    execute_query(delete_query)

def add_data(table_name, t, v, i):
    """ Add data to table """
    add_query = f"INSERT INTO {table_name} (timestamp, voltage, current) VALUES ('{t}', {v}, {i})"
    execute_query(add_query)

def create_table(table_name):
    """ Create an empty table with columns voltage and current """
    try:
        create_table_query = f"CREATE TABLE {table_name} (timestamp TIMESTAMP, voltage NUMERIC, current NUMERIC)"
        execute_query(create_table_query)
    except: 
        raise TableError('Could not create table')


#t = datetime.datetime.now()
#add_data(t, 'batterydata', 500, 600)
#
