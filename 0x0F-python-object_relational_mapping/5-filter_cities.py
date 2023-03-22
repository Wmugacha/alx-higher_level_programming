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
    state_name = argv[4]

    query = "SELECT cities.name \
             FROM cities INNER JOIN states \
             ON cities.state_id = states.id \
             WHERE states.name LIKE BINARY %s \
             ORDER BY cities.id ASC"

    args = (state_name,)

    db = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            port=3306
            )

    cur = db.cursor()
    cur.execute(query, args)
    rows = cur.fetchall()
    if rows is not None:
        print(", ".join([row[0] for row in rows]))

    cur.close()
    db.close()
