#!/usr/bin/python3
""" selecting with mysqldb """
import MySQLdb
import sys


if __name__ == "__main__":
    try:
        db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            port=3306,
            db=sys.argv[3]
        )
    except MySQLdb.Error:
        print("Error connecting")
    cur = db.cursor()
    try:
        cur.execute("SELECT * FROM states WHERE name LIKE BINARY %(name)s \
        ORDER BY states.id ASC", {'name': sys.argv[4]})
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error:
        print("Execution failed")
    cur.close()
    db.close()
