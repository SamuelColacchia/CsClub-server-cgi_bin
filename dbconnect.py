#!/usr/bin/python

import pyodbc

def dbconnect(username,password,dbname):
    driver = 'Driver={mySQL}'
    server = 'SERVER=localhost'
    UID = 'UID=' + username
    PWD = 'PWD=' + password
    
    if dbname != '':
        DATABASE = 'DATABASE=' + dbname
        connectionstring = driver + ';' + server + ';' + UID + ';' + PWD + ';' + DATABASE + ";"
    else:
        connectionstring = driver + ';' + server + ';' + UID + ';' + PWD + ';'

    return pyodbc.connect(connectionstring)
