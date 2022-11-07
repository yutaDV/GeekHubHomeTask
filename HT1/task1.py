conn.execute('''CREATE TABLE USERS
        (ID INT PRIMARY KEY  NOT NULL,
        NAME TEXT NOT NULL,
        PASSWORD TEXT NOT NULL,
        BALANCE REAL,
        ADMIN_TOKEN TEXT);''')
conn.execute('''CREATE TABLE TRANSACTIONS
        (ID_USER INT  NOT NULL,
        TIME_DATE TEXT NOT NULL,
        ACTION TEXT NOT NULL,
        SUM REAL,
        NEW_BALANCE REAL );''')
conn.execute('''CREATE TABLE ATM_BALANCE
        (DENOMINATION TEXT NOT NULL,
        NUMBER_OF_BILLS INT,
        SUM REAL);''')


conn.execute("INSERT INTO USERS (ID,NAME,PASSWORD,BALANCE,ADMIN_TOKEN) \
    VALUES (1, 'hare', 'carrot54', 715, 'False')" )
conn.execute("INSERT INTO USERS (ID,NAME,PASSWORD,BALANCE,ADMIN_TOKEN) \
    VALUES (2, 'fox', 'hare4567', 1000, 'False')" )
conn.execute("INSERT INTO USERS (ID,NAME,PASSWORD,BALANCE,ADMIN_TOKEN) \
    VALUES (3, 'wolf', 'fox44fox', 2500, 'False')" )
conn.execute("INSERT INTO USERS (ID,NAME,PASSWORD,BALANCE,ADMIN_TOKEN) \
    VALUES (4, 'bear', 'honey1256l', 1599876.00, 'False')" )
conn.execute("INSERT INTO USERS (ID,NAME,PASSWORD,BALANCE,ADMIN_TOKEN) \
    VALUES (5, 'admim', 'admim', 0, 'True')" )

import sqlite3
import csv
import json
import datetime
import time


conn = sqlite3.connect('ATM.db')
conn.execute("INSERT INTO USERS (ID,NAME,PASSWORD,BALANCE,ADMIN_TOKEN) \
    VALUES (1, 'hare', 'carrot54', 715, 'False')" )
conn.execute("INSERT INTO USERS (ID,NAME,PASSWORD,BALANCE,ADMIN_TOKEN) \
    VALUES (2, 'fox', 'hare4567', 1000, 'False')" )
conn.execute("INSERT INTO USERS (ID,NAME,PASSWORD,BALANCE,ADMIN_TOKEN) \
    VALUES (3, 'wolf', 'fox44fox', 2500, 'False')" )
conn.execute("INSERT INTO USERS (ID,NAME,PASSWORD,BALANCE,ADMIN_TOKEN) \
    VALUES (4, 'bear', 'honey1256l', 1599876.00, 'False')" )
conn.execute("INSERT INTO USERS (ID,NAME,PASSWORD,BALANCE,ADMIN_TOKEN) \
    VALUES (5, 'admim', 'admim', 0, 'True')" )


conn = sqlite3.connect('ATM.db')
conn.execute("INSERT INTO USERS (ID,NAME,PASSWORD,BALANCE,ADMIN_TOKEN) \
    VALUES (1, 'hare', 'carrot54', 715, 'False')" )
conn.execute("INSERT INTO USERS (ID,NAME,PASSWORD,BALANCE,ADMIN_TOKEN) \
    VALUES (2, 'fox', 'hare4567', 1000, 'False')" )
conn.execute("INSERT INTO USERS (ID,NAME,PASSWORD,BALANCE,ADMIN_TOKEN) \
    VALUES (3, 'wolf', 'fox44fox', 2500, 'False')" )
conn.execute("INSERT INTO USERS (ID,NAME,PASSWORD,BALANCE,ADMIN_TOKEN) \
    VALUES (4, 'bear', 'honey1256l', 1599876.00, 'False')" )
conn.execute("INSERT INTO USERS (ID,NAME,PASSWORD,BALANCE,ADMIN_TOKEN) \
    VALUES (5, 'admim', 'admim', 0, 'True')" )

cursor = conn.execute("SELECT ID,NAME,PASSWORD,BALANCE,ADMIN_TOKEN from USERS")
for row in cursor:
    print("ID" , row [0])
    print("NAME" , row [1])
    print("PASSWORDEN" , row [2])
    print("IBALANCE" , row [3])
    print("ADMIN_TOKEN" , row [4], '--------------')