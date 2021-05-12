#! /usr/bin/env python3
import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()
table = 'user' 

c.execute('SELECT * FROM '+table)
data = c.fetchall()
#print(data)

for row in data:
    print(row)
