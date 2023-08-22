#!/usr/bin/python3
"""lists all states in database"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], port=3306,
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM  states ORDER BY id ASC")
    var = cur.fetchall()
    for index in var:
        print(index)
    cur.close()
    db.close()
