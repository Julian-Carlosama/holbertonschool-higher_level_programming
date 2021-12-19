#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """ Values for the connect to the database """
    users = sys.argv[1]
    passw = sys.argv[2]
    datB = sys.argv[3]
    """Connecting to the database"""
    db = MySQLdb.connect(host="localhost", user=users,
                         password=passw, db=datB, port=3306, charset="utf8")

    """The cursor gives us the ability to have multiple seperate
    working environments through the same connection to the database"""
    cur = db.cursor()

    """Executing the query"""
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'ORDER BY id ASC;")

    states = cur.fetchall()

    """ Show the results find """
    for state in states:
        print(state)
    cur.close()
    """Closing the connection to the database"""
    db.close()
