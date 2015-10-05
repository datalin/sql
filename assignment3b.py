import sqlite3

with sqlite3.connect("newnum.db") as connetion:
	cursor = connetion.cursor()


	prompt = """
			Select the operation that you want to perform [1-5]:
			1. Average
			2. Max
			3. Min
			4. Sum
			5. Exit
			"""

	while True:
		x = raw_input(prompt)

		if x in set(["1", "2", "3", "4"]):
			operation = {1:"avg", 2:"max", 3:"min", 4:"sum"}[int(x)]

			cursor.execute("SELECT {}(num) FROM numbers".format(operation))

			get = cursor.fetchone()

			print operation + ": %f" % get[0]

		elif x == "5":
			print "Exit"
			break

