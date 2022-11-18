import sqlite3

conn = sqlite3.connect('ATM.db')
cursor = conn.cursor()
sum_id = 0
for row in cursor.execute("SELECT *FROM USERS"):
    sum_id += 1
#params = (sum_id + 1, self.username, self.user_password, self.user_balance, self.admin_token)
#cursor.execute("INSERT INTO USERS VALUES (?,?,?,?,?)", params)
conn.commit()
conn.close()
print('sum_id')
