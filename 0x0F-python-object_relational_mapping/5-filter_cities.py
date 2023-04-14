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

    state_name = sys.argv[4]

    ''' connect to the database '''
    db = MySQLdb.connect(host="localhost", user=db_user,
                         passwd=db_password, db=db_name)

    query = '''
        SELECT cities.name FROM cities
        LEFT JOIN states
        ON states.id = cities.state_id
        WHERE states.name LIKE %s
    '''

    cursor = db.cursor()
    cursor.execute(query, (state_name, ))

    count = 0
    buffer = ''
    for output in cursor:
        if count > 0:
            buffer += ", "
        buffer += str(output[0])
        count += 1
    print(buffer)
    cursor.close()
    db.close()
