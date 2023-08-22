#!/usr/bin/python3
"""safe from sql injections"""

import sys
import MySQLdb

if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = MySQLdb.connect(user=user, port=3306, passwd=passwd, db=sys.argv[3])
    cur = db.cursor()
    query = "SELECT * FROM states WHERE Name = %s ORDER BY id"
    cur.execute(query, [sys.argv[4]])
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close
