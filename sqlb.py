import sqlite3

conn = sqlite3.connect("new.db")

cursor = conn.cursor()

try:

	cursor.execute("""
		INSERT INTO poulation VALUES('New York City', 'NY', 8200000 )""")

	cursor.execute("""
		INSERT INTO poplation VALUES('San Francisco', 'CA', 800000 )""")

	conn.commit()

except sqlite3.OperationalError:
	print "OOps, something went wrong pelase try again!"

conn.close()





