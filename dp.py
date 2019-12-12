# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 22:26:07 2019

@author: Parth
"""

import psycopg2

conn = psycopg2.connect(database="tp", user = "postgres", password = "parth123n@#*", host = "127.0.0.1", port = "5432")

cur = conn.cursor()
cur.execute('''CREATE TABLE COMPANY
      (ID INT PRIMARY KEY     NOT NULL,
      NAME           TEXT    NOT NULL,
      AGE            INT     NOT NULL,
      ADDRESS        CHAR(50),
      SALARY         REAL);''')
print("Table created successfully")

conn.commit()
conn.close()