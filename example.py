import sqlite3

# Establish a connection and a cursor.
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# Query all the Data based on a condition.
cursor.execute("SELECT*FROM data WHERE date='6.5.2088'")
rows = cursor.fetchall()
print(rows)

# Query band and date data based on a condition.
cursor.execute("SELECT band, date FROM data WHERE date='6.5.2088'")
rows = cursor.fetchall()
print(rows)

# Insert new columns based on a condition.
new_row = [('Hamaad Ullah event', 'Hamaad Ullah City', '27.9.2026')]
cursor.executemany("INSERT INTO data VALUES (?,?,?)", new_row)
connection.commit()

cursor.execute("SELECT*FROM data WHERE date='27.9.2026'")
rows = cursor.fetchall()
print(rows)
