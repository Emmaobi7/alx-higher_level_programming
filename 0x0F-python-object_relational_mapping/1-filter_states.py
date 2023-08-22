#/usr/bin/python3
"""list all states starting with "N" in database"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys[1], passwd=sys[2], db=sys[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    print(cur.fetchall())
    db.close()
