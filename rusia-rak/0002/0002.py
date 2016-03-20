#!/usr/bin/env python3
#This script takes a list of codes from file result.txt and store it in a local database(name = codesdb) under  table(name = codes).

import mysql.connector

conn = mysql.connector.connect(user='root', password='password', database='codesdb')
cur = conn.cursor()
query = "CREATE TABLE codes(id INT PRIMARY KEY AUTO_INCREMENT, code INT)"
cur.execute(query)
f = open("result.txt", 'r')
for code in f:
	query = "INSERT INTO codes(code) VALUES({})".format(code.strip())
	cur.execute(query)

conn.commit()
cur.close()
conn.close()

	

