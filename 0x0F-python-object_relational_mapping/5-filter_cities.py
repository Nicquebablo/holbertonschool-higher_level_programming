#!/usr/bin/python3
'''
Lists all cities from the database hbtn_0e_4_usa.
'''

import MySQLdb
from sys import argv


conn = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                       user=argv[1], passwd=argv[2], db=argv[3])

cur = conn.cursor()
cur.execute("SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN\
            states ON cities.state_id = states.id WHERE states.name=%s\
            ORDER by cities.id ASC;",
            (argv[4], ))
query_rows = cur.fetchall()
print(', '.join([row[1] for row in query_rows]))
cur.close()
conn.close()