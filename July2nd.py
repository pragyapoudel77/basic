import sqlite3

#Connect to a database(creates a new one if it doesn't exist)

conn = sqlite3.connect('database.db')

#Create a cursor object to execute SQL commands
cursor = conn.cursor()

# #Define table structure
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY,
#             username TEXT NOT NULL,
#             age INTEGER,
#             email text unique
#     )
# '''
# )

#insert a single record
#cursor.execute("INSERT INTO users(username,age,email) VALUES('Alice',30,'alice@example.com')")

# users = [
#     ('Bob',25,'bob@example.com'),
#     ('Charlie',35,'charlie@example.com')
# ]
# cursor.executemany("INSERT into users(username,age,email) VALUES(?,?,?)",users)

# cursor.execute("SELECT * FROM users")
# rows = cursor.fetchall()
# for row in rows:
#     print(row) rolll number


#Retrieve records with a condition(WHERE clause)
cursor.execute("SELECT * FROM users WHERE age>30")
filtered_rows = cursor.fetchall()
for row in filtered_rows:
     print(row)

cursor.execute("UPDATE users SET age = 31 WHERE username = 'Alice'")
filtered_rows = cursor.fetchall()
for row in filtered_rows:
     print(row)

cursor.execute("DELETE from users where username ='Bob'")
#Commit the transaction
conn.commit()

cursor.close()
cursor.close()





