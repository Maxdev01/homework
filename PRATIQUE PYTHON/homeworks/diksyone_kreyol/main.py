'''
diksyone sa ap bezwen yon meni 
yon class kap gen ladan plizye metod kap pemet li mache pi byen
fok mwen import sqlite3 avek datetime kom modil

'''
import sqlite3
from datetime import datetime


class Diksyone_pam:
    non_an = "Diksyone lakay"


    # N'ap kontrikte an an mwen ouve baz done an 
    def __init__(self):
        self.conn = sqlite3.connect("stokaj.db")
        self.cu = self.conn.cursor()

    # metod sa se pou li ka kreye tab lan sa vle di plas pou mete done yo 
    # san li proje an pap komanse 

    def kreyasyon(self):
        mesaj = "tab lan kreye ak sikse Bravo"

        try:
            self.cu.execute(''' CREATE TABLE resous(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            datee VARCHAR(20) NOT NULL,
                            word TEXT NOT NULL,
                            category TEXT NOT NULL,
                            definisyon TEXT NOT NULL)''')
            print(mesaj)
        except:
            pass 


        # metod sa se poum ka antre done yo 
    def Antre(self):
        mesaj2 = "Done ou yo mete avek sikse Bravo"
        mo = input("Ki ou vle mete an: ")
        kateg = input(f"ki kategori mo sa {mo}:  ")
        defi = input(f"Ki definisyon mo sa {mo}: ")
        da = datetime.now()

        self.cu.execute(" INSERT INTO resous(datee, word, category, definisyon) VALUES(?,?,?,?)", (da, mo, kateg, defi,))
        self.conn.commit()
        print(mesaj2)

    # method sa ap pemet ou we done ou sot mete yo 
    # ki donk fok mwen bien afiche yo

    def Views(self):
        we = self.conn.execute(" SELECT * FROM resous ")

        for i in we:
            print("ID: ", i[0],"\t", "DAT: ", i[1],"\t", "MO:", i[2],"\t", "KATEGORI: ", i[3],"\t", "DEFISYON: ", i[4] , "\n\n")
        self.conn.close()



'''
lap gen meni kap la poum ka jere
aplikasyon an ladan wap jwenn
1- afiche 2- antre done 3- efase yon done avek yon id 3- modifye yon done 
3-1 lew finn antre nan modifye kounya wap jwenn yon lot opsyon kap mandew si 
1 - si se mo 2- kategori an 3- defisyon an 
 
'''

def meni():
    print("BYENVINI NAN DIKSYONE LAKAY")
    mm = "1- afiche tout mo yo \n 2- ajoute yon mo \n 3- efase yon mo"
    print(mm)

    try:
        quest = int(input("ki chwa'w ?:  "))

    except:
        print("se yon chif  pouw antre")
    return quest

klas = Diksyone_pam()

def sou_meni():
    #global fonk1
    b = meni()

    if b == 1:
        print(1)
    if b == 2:
        print("vinn mete")
        klas.Antre()
    if b == 1:
        print("gade non frem ")
        klas.Views()
        # wap gen pouw fel yon sel fwa 
        # koz ou paka kreye yon tab 2 fwa
    if b == 90:
        print("li bon")
        klas.kreyasyon()

fonk2 = sou_meni()
