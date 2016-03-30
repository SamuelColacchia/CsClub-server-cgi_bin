#!/usr/bin/python

from dbconnect import *

import json
import collections


connection = dbconnect('samuel.colacchia','gdi1985','csclub')

cursor = connection.cursor()

query = ('select * from leaders')

cursor.execute(query)

rows = cursor.fetchall()

object_list = []

for row in rows:
    d = collections.OrderedDict()
    d['leader_id'] = row.leader_id
    d['leader_name'] = row.leader_name
    d['leader_email'] = row.leader_email
    d['leader_pic'] = row.leader_pic
    d['leader_title'] = row.leader_title
    d['leader_class'] = row.leader_class
    object_list.append(d)

connection.close()

response = json.JSONEncoder().encode(object_list)

print 'Status: 200 OK'
print "Content-Type: text/plain;charset=utf-8"
print "Connection: close"
print

print response
