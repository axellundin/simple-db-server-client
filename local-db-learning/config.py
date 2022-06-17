#!/usr/bin/python
from configparser import ConfigParser

class ConfigFileError(Exception):
    pass

def config(filename='database.ini', section='postgresql'):
    ''' 
    Read db conf from file.
    Raises exception ConfigFileError 
    '''
    try:  
        # create a parser
        parser = ConfigParser()
        # read config file
        parser.read(filename)
        
        # get section, default to postgresql
        db = {}
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    except:
        raise ConfigFileError('Missing data in config file')

    return db
