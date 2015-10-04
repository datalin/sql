import sqlite3

with sqlite3.connect("new.db") as connection:

	cursor = connection.cursor()

	cursor.execute("UPDATE cars SET quantity = 2 WHERE model = '1952' ")
	cursor.execute("UPDATE cars SET quantity = 2 WHERE model = '1948' ")

	cursor.execute("SELECT * FROM cars WHERE make = 'FORD'")

	rows = cursor.fetchall()

	for row in rows:

		print row[0], row[1], row[2]

