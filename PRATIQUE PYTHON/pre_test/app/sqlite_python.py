import sqlite3

conn = sqlite3.connect("max.db")

print("mwen kreye baz done an ak siske")

# conn.execute('''CREATE TABLE BIZNIS(
# 			 NAME TEXT NOT NULL,
# 			 AGE INT NOT NULL,
# 			 ADDRESS CHAR(50),
# 			 SALARY REAL)''')
# print("mwen kreye tab lan ak siske")
# conn.close()

# conn.execute("INSERT INTO BIZNIS(NAME, AGE, ADDRESS, SALARY) VALUES('PAUL', 23,'JDJDJDJD',2000)")
# conn.commit()
# print("hhssh")
# conn.close()

cursor = conn.execute("SELECT name,address, salary from BIZNIS")
for row in cursor:
	print(row[0])
	print(row[1])
	print(row[2])
print("mwen we")
conn.close()



