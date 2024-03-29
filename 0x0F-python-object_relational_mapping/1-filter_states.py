#!/usr/bin/python3
# Lists all states with a name starting with N from the database hbtn_0e_0_usa.
# Usage: ./1-filter_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>

from sys import argv
import MySQLdb

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name)
    cur = db.cursor()
    cur.execute("SELECT states.id, name FROM states WHERE name "
                "COLLATE latin1_general_cs "
                "LIKE 'N%' "
                "ORDER BY states.id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
