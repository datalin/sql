import sqlite3

with sqlite3.connect("new.db") as connection:
	cursor = connection.cursor()

	cursor.execute("SELECT firstname, lastname from employees")

	rows = cursor.fetchall()

	for r in rows:
		print r[0], r[1]