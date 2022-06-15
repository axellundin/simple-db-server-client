from os import times
import psycopg2
from config import get_config
from datetime import datetime
import time

def get_db_connection():
    """ Returns a psycopg connection to the database server.
    TODO: Error handling, documentation """
    conf = get_config()
    conn = psycopg2.connect(**conf)
    return conn 

def exec_command(command): 
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(command)
    conn.commit()
    cur.close()

def create_table(table_name):
    command = f"CREATE TABLE {table_name}(voltage FLOAT(5), current FLOAT(5), timestamp TIMESTAMP PRIMARY KEY)"
    exec_command(command)

def get_table(table_name):
    command = f"SELECT * FROM {table_name}"
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(command)
    table_data = cur.fetchall()
    cur.close()
    return table_data

def add_measurement(table_name, voltage, current, timestamp):
    """  """
    command = f"INSERT INTO {table_name} (voltage, current, timestamp) VALUES({voltage}, {current}, '{timestamp}')"
    exec_command(command)

def remove_measurement(table_name, timestamp):
    """  """
    command = f"DELETE FROM {table_name} WHERE timestamp = '{timestamp}'"
    exec_command(command)

if __name__=='__main__': 
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT timestamp FROM battery_data')
    timestamps = cur.fetchall()

    print(timestamps)
    for time in timestamps:
        remove_measurement('battery_data', str(time[0]))

    print(get_table('battery_data'))
    


