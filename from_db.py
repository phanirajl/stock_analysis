# -*- coding: utf-8 -*-

# from_db.py

import MySQLdb as mdb # MySQL server and database storage

# obtain a database connection to the MySQL instance
db_host = 'hostname'
db_user = 'username'
db_pass = 'password'
db_name = 'database'
con = mdb.connect(db_host, db_user, db_pass, db_name)

def ticker_pull():
    """obtains a list of the ticker symbols in the database"""
    with con: 
        cur = con.cursor()
        cur.execute("SELECT id, ticker FROM symbol")
        data = cur.fetchall()
        return [(d[1]) for d in data]

symbols = ticker_pull()
