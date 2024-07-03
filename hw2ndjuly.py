import sqlite3

#Connect to a database(creates a new one if it doesn't exist)

conn = sqlite3.connect('database.db')

#Create a cursor object to execute SQL commands
cursor = conn.cursor()



# #insert a single record
# cursor.execute("INSERT INTO users_table(username,age,email) VALUES('Alice',30,'alice@example.com')")


#List of user records to insert
users_table = [
    ('Bob', 25, 'bob@example.com'),
    ('Charlie', 35, 'charlie@example.com')
]

# Insert multiple records into the users_table table
cursor.executemany("INSERT INTO users_table(username, age, email) VALUES (?, ?, ?)",users_table)

# cursor.execute("SELECT * FROM users")
# rows = cursor.fetchall()
# for row in rows:
#     print(row) rolll number


#Retrieve records with a condition(WHERE clause)
# cursor.execute("SELECT * FROM users WHERE age>30")
# filtered_rows = cursor.fetchall()
# for row in filtered_rows:
#      print(row)

# cursor.execute("UPDATE users SET age = 31 WHERE username = 'Alice'")
# filtered_rows = cursor.fetchall()
# for row in filtered_rows:
#      print(row)

# cursor.execute("DELETE from users where username ='Bob'")
#Commit the transaction
# conn.commit()
# cursor.execute("SELECT * FROM users_table")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

#git config --global core.autocrlf true/input----IMPORTANT

cursor.execute("UPDATE users_table SET age = 31 WHERE username = 'Alice'")
filtered_rows = cursor.fetchall()
for row in filtered_rows:
     print(row)


cursor.close()





