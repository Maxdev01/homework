import sqlite3


connection = sqlite3.connect("test.db")
c = connection.cursor()

def Create():
    global connection
    global c
    c.execute("""CREATE TABLE IF NOT EXISTS achiv(
            nom TEXT,
            prenom TEXT,
            salaire INTEGER
            )""")
    connection.commit()
def insc():
    global connection
    global c
    nom = input("antre nomw : ")
    prenom = input("antre prenom :  ")
    salaire = int(input("konbyn kob wap touche ?:  "))

    reket = "INSERT INTO achiv VALUES('{}', '{}', '{}')".format(nom ,prenom, salaire)
    print(reket)

def prend():
    global connection
    global c
    cursor = connection.execute("SELECT * FROM achiv")
    for row in cursor:
        print("Nom = ",row[0])
        print("prenom", row[1])
        print("salaire", row[2],"\n")
    
    connection.close()

def retiev():
    global c
    global connection
    salaire = int(input("mete kob lan:  "))
    requette = "SELECT * FROM achiv WHERE salaire = {}".format(salaire)
    print(requette)
    c.execute(requette)
    print(c.fetchall())
#z = Create()
#o= insc()
b = prend()
#m = retiev()  


    
