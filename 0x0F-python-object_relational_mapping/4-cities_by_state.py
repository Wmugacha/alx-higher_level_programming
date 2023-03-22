#!/usr/bin/python3
"""
script that lists states from
the database hbtn_0e_4_usa.

"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    """
    Access the database and get the states.
    """
    query = "SELECT cities.id, cities.name, states.name \
             FROM cities \
             INNER JOIN states ON \
             cities.state_id = states.id \
             ORDER BY cities.id ASC"

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
