
import pickle
import os
class Identification:


    def __init__(self):
        
        self.resous_db()
        b = 0
        self.stokaj = {}
        self.id = 10
        with open("bazdone", "rb") as file:
            pickler = pickle.Unpickler(file)
            try:
                b = pickler.load()
            except:
                print("baz done an vid pou moman sa")
            else:
                if s:
                    self.stokaj = b.stokaj
                    self.id = b.id
            
    def resous_db(self):
        if not os.path.exists("bazdone"):
            file = open("bazdone", "wb")
            file.close()

    def Save(self):
        with open("bazdone", "wb") as file:
            pickler = pickle.Pickler(file)
            pickler.dump(self)
        
    
    def ajoute(self):
        essai = 2
        vre = True
        while vre:
            nom = input("antre nomw svp:  ")
            prenom = input("antre prenom w svp:  ")

            self.stokaj[self.id] = [nom, prenom]
            self.id += 1
            essai -= 1
            if essai == 0:
                vre = False
                self.afiche()


    def afiche(self):
        for i in reversed(self.stokaj.keys()):
            y = self.stokaj[i]
            print(f"{i} \t {y[0]} \t {y[1]}")
    def view(self):
        h = input("wap gade yo :  ")
        if h == "vu":
            f = open("bazdone", "rb")
            hi = pickle.load(f)
            print(hi)
        
                
                
                
def meni():

    h = int(input("ki chwa w:  "))

    return h

me = Identification()
b = meni()
me.Save()
if b == 1:
    me.ajoute()
elif b == 2:
    me.view()
