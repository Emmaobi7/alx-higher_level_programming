#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]

    conn = MySQLdb.connect(user=user, port=3306, passwd=passwd, db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities" +
                " INNER JOIN" +
                " states ON" +
                " cities.state_id = states.id" +
                " ORDER BY cities.id ASC")
    cities = cur.fetchall()
    for city in cities:
        print(city)
    conn.close()
