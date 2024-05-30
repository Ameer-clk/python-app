import sqlite3

# Create a connection to an SQLite database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Vulnerable code: accepting user input without proper sanitization
username = input("Enter username: ")
password = input("Enter password: ")

# Vulnerable SQL query with potential for SQL injection
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
cursor.execute(query)

# Fetch the results and print them (for demonstration purposes)
results = cursor.fetchall()
for row in results:
    print(row)

# Close the connection
conn.close()



