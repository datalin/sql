import sqlite3

with sqlite3.connect("new.db") as connection:
	cursor = connection.cursor()

	cursor.execute("UPDATE population SET population = 9000000 WHERE city = 'New York City' ")

	cursor.execute("DELETE FROM population WHERE city ='Boston' ")

	print "\n NEW DATA: \n"

	cursor.execute("SELECT * FROM population")

	rows = cursor.fetchall()

	for row in rows:
		print row[0], row[1], row[2]