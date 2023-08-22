#!/usr/bin/python3
"""queries by commandline arg"""

import MySQLdb
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    db = MySQLdb.connect(user=user, port=3306, passwd=passwd, db=db)
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE Name LIKE BINARY '{}' ORDER BY id ASC"
        .format(sys.argv[4]))
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
