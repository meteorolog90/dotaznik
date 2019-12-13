#!/usr/bin/python
# -*- coding: utf-8 -*-



#SQLite connect to database and query data

# import sqlite3 as lite
# import sys


# con = lite.connect('user.db')

# with con:    
    
#     cur = con.cursor()    
#     cur.execute("SELECT * FROM Users")

#     rows = cur.fetchall()

#     for row in rows:
#         print (row)




#postgreSQL

import sqlalchemy as db

class Database():
    # replace the user, password, hostname and database according to your configuration according to your information
    engine = db.create_engine('postgresql://postgres:energia@localhost/spotrebaee')
    def __init__(self):
        self.connection = self.engine.connect()
        print("DB Instance created")


def fetchByQyery(self, query):
    fetchQuery = self.connection.execute(f"SELECT * FROM {query}")
        
    for data in fetchQuery.fetchall():
        print(data)
