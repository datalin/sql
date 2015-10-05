import sqlite3
import random

with sqlite3.connect("newnum.db") as connection:
	cursor = connection.cursor()

	cursor.execute("DROP TABLE IF EXISTS numbers")

	cursor.execute("CREATE TABLE numbers(num INT)")

	for i in range(100):
		cursor.execute("INSERT INTO numbers VALUES(?)", (random.randint(0,100),))