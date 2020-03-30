#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    c = db.cursor()
    like = argv[4]
    c.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY\
    id ASC", (like,))
    for rows in c.fetchall():
        if rows[1] == argv[4]:
            print(rows)

    c.close()
    db.close()
