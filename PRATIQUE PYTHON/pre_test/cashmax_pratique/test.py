import sqlite3

conn = sqlite3.connect("bzdone.db")
print("baz donne an kreye avek sikse")

def create():
    global conn
    conn.execute('''CREATE TABLE INFO(
                NAME TEXT NOT NULL,
                AGE INT NOT NULL,
                VILLE CHAR(50),
                PAYS TEXT NOT NULL
                )''')
    print("table lan kreye avek sikse")
    conn.close()

def insert():
    global conn
    nom = input("nomw:  ")
    laj = int(input("laj:  "))
    kote = input("kote an :  ")
    peyi = input("peyi:  ")
    conn.execute("INSERT INTO INFO VALUES(?,?,?,?)",(nom, laj,kote,peyi))
    conn.commit()
    print("mwen antre done yo ak sikse")
    #conn.close()

def afich():
    global conn
    cursor = conn.execute("SELECT name, age,ville, pays from INFO")
    for row in cursor:
        print("men liste tout done yo san manke")
        print("NAME = ", row[0])
        print("AGE = ", row[1])
        print("VILLE = ", row[2])
        print("PAYS = ", row[3])
    print("mwen we done mwen yo ak sikse")
    conn.close()

#create()
insert()
afich()
        
