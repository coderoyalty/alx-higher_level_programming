#!/usr/bin/python3

"""
    this script list all states from
    a database.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    ''' the database user '''
    db_user = sys.argv[1]
    ''' the database password '''
    db_password = sys.argv[2]
    ''' the database name '''
    db_name = sys.argv[3]

    ''' connect to the database '''
    db = MySQLdb.connect(host="localhost", user=db_user,
                         passwd=db_password, db=db_name)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    outputs = cursor.fetchall()

    for output in outputs:
        print(output)
    cursor.close()
    db.close()
