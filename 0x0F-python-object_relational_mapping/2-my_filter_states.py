#!/usr/bin/python3
"""
script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument

"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    """
    Access the database and get the states.
    """
    try:
        db = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            port=3306,
            passwd=argv[2],
            db=argv[3]
        )
    except MySQLdb.Error:
        print("error connecting")
    cur = db.cursor()
    try:
        cur.execute("SELECT * FROM states WHERE name = %s ORDER BY \
                    states.id", (argv[4],))
        rows = cur.fetchall()

        for row in rows:
            print(row)
    except MySQL.Error:
        print("Execuction failed")

        cur.close()
        db.close()
