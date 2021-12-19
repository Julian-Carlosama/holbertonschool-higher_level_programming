#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa:
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """ Values for the connect to the database """
    users = sys.argv[1]
    passw = sys.argv[2]
    datB = sys.argv[3]

    """ Configuration to the database """
    db = MySQLdb.connect(host="localhost", user=users, password=passw,
                         db="datB", port=3306, charset="utf8")

    """
    Class used to execute the database whit python,
    It gives us the ability to have multiple seperate working environments
    through the same connection to the database.
    """
    cur = db.cursor()

    """ Query used for execute records of the table """
    cur.execute("SELECT * FROM states ORDER BY states.id ASC;")

    """ Get all records from the cursor object"""
    states = cur.fetchall()

    """ Show the results find """
    for state in states:
        print(state)
    cur.close()
    db.close()
