import sqlite3

with sqlite3.connect("new.db") as connection:

	cursor = connection.cursor()

	cursor.execute("INSERT INTO cars VALUES('FORD', 1952, 42)")
	cursor.execute("INSERT INTO cars VALUES('FORD', 1948, 43)")
	cursor.execute("INSERT INTO cars VALUES('FORD', 1976, 40)")
	cursor.execute("INSERT INTO cars VALUES('HONDA', 1952, 3)")
	cursor.execute("INSERT INTO cars VALUES('HONDA', 1980, 46)")

	cursor.execute("SELECT * FROM cars")

	rows = cursor.fetchall()

	for row in rows:

		print row[0], row[1], row[2]


