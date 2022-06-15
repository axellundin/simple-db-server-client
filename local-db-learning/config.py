from configparser import ConfigParser
import os
from xml.dom import NotFoundErr 

def get_config(filename='database.ini', section='postgresql'):
    cwd = os.path.dirname(os.path.realpath(__file__))
    
    parser = ConfigParser()
    # read config file
    parser.read(cwd + "/" + filename)

    db = dict()
    if parser.has_section(section):
        params = parser.items(section)
        for param in params: 
            db[param[0]] = param[1]
    else:
        raise NotFoundErr(f'Section {section} not found in the file {filename}')
    return db

if __name__=='__main__':print(get_config())
