import sqlite3

with sqlite3.connect("new.db") as connection:
	cursor = connection.cursor()

	#cursor.execute("CREATE TABLE orders(make TEXT, model TEXT, order_date TEXT)")

	orders = [("FORD", 1952, 1962-12-12),
			("FORD", 1952, 1972-12-12),
			("FORD", 1952, 1954-2-3),
			("FORD", 1948, 1948-2-3),
			("FORD", 1948,1952-2-3),
			("FORD", 1948, 1962-2-3),
			("FORD", 1976,1976-2-3),
			("FORD", 1976, 1976-4-5),
			("FORD", 1976, 1978-5-4),
			("HONDA", 1952, 1952-2-21),
			("HONDA", 1952, 1952-4-5),
			("HONDA", 1952, 1953-5-3),
			("HONDA", 1980, 1980-9-9),
			("HONDA", 1980, 1982-9-9),
			("HONDA", 1980, 1982-10-11)]

	cursor.executemany("INSERT INTO orders VALUES (?,?,?)", orders)



	cursor.execute("SELECT DISTINCT orders.make, orders.model, inventory.quantity, orders.order_date\
	 FROM orders, inventory WHERE inventory.make = orders.make and inventory.model = orders.model")

	rows = cursor.fetchall()

	for row in rows:
		print "Make "+row[0], "Model " + row[1]
		print "Quantity: " + str(row[2])
		print "Order Date: "+ row[3]

