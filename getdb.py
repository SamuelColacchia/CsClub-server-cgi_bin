#!/usr/bin/python

from dbconnect import *

import json
import collections



connection = dbconnect('samuel.colacchia','gdi1985','')

cursor = connection.cursor()

query = ("show databases")

cursor.execute(query)

rows = cursor.fetchall()


object_list = []
for row in rows:
    d = collections.OrderedDict()
    d['db_name'] = row.Database
    if row.Database in ["information_schema", "mysql", "performance_schema", "sys"]:
        continue
    else:
        object_list.append(d)


connection.close()

response = json.JSONEncoder().encode(object_list)


print 'Status: 200 OK'
print "Content-Type: text/plain;charset=utf-8"
print "Connection: close"
print

print response
