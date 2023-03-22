#!/usr/bin/python3
"""
script that lists states from
the database hbtn_0e_0_usa.

"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    """
    Access the database and get the states.
    """
    state_name = argv[4]
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' \
            ORDER BY id ASC".format(state_name)

    db = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            port=3306
            )

    cur = db.cursor()
    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
