import sqlite3

with sqlite3.connect("new.db") as connection:

	cursor = connection.cursor()

	cursor.execute("SELECT * FROM inventory")

	rows = cursor.fetchall()

	for row in rows:
		print "Make: " + row[0], "Model: " + row[1]
		print "Quantity: " + str(row[2])
		
		cursor.execute("SELECT count(order_date) FROM orders WHERE make = ?and model = ?", (row[0], row[1]))

		order_count = cursor.fetchone()[0]

		print order_count

