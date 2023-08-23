#!/usr/bin/python3
"""lists on cities in state"""

import MySQLdb
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    db = MySQLdb.connect(user=user, passwd=passwd, db=db)
    cur = db.cursor()
    query = "SELECT cities.name FROM cities"
    query = query + " INNER JOIN states ON cities.state_id = states.id"
    query = query + "WHERE states.name = %s ORDER BY cities.id ASC"
    cur.execute(query, [sys.argv[4]])
    val = cur.fetchall()
    print(", ".join([row[0] for row in val]))
    cur.close()
    db.close()
