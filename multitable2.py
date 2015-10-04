import sqlite3

with sqlite3.connect("new.db") as connection:
	cursor = connection.cursor()

	cursor.execute("""SELECT DISTINCT population.city, population.population, \
		regions.region FROM population, \
		regions WHERE population.city = regions.city ORDER BY population.city ASC""")

	rows = cursor.fetchall()

	for row in rows:

		print "City:" + row[0]
		print "Population:" + str(row[1])
		print "Region:" + row[2]
