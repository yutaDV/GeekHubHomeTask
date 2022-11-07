import sqlite3



conn = sqlite3.connect('ATM.db')
cur = conn.cursor()
result = cur.execute("SELECT ID,NAME,PASSWORD,BALANCE,ADMIN_TOKEN from USERS").fetchmany()
print(result)

conn.close()