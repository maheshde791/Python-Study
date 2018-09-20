#!/usr/bin/python

import psycopg2

class Database:
    def __init__(self):
        self. params = {"database":"hitachi", "user":"postgres", "password":"mymac", "host":"127.0.0.1", "port":"5432"}


    def openConnection(self):
        """ Connect to the PostgreSQL database server """
        self.conn = None
        try:
            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            self.conn = psycopg2.connect(**self.params)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def executeQuery(self,sql):
        cur = self.conn.cursor()
        cur.execute(sql)
        return cur.fetchall()
        cur.close()

    def closeConnection(self):
        if self.conn is not None:
            self.conn.close()

