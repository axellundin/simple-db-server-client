import random 
from test_ldb import *
import datetime
import psycopg2

def gen_datapoint(mean, max, min):
    scaled_rnd = min + (random.random()*(max-min))
    data = mean + scaled_rnd
    return data

# measurements are generated

for data in range(0,20):
    v = gen_datapoint(500, 50, -50)
    i = gen_datapoint(600, 50, -50)
    t = datetime.datetime.now()

    try:
        add_data('battery_rdb', t, v, i)
        add_data('battery_ldb', t, v, i)
    except(psycopg2.errors.InvalidDatetimeFormat):
        # do something
        print('Invalid date')
    except(Exception):
        print('Something went wrong')

