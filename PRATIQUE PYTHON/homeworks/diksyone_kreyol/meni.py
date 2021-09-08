from .main import Diksyone_pam


def meni():
    print("BYENVINI NAN DIKSYONE LAKAY")
    mm = "1- afiche tout mo yo \n 2- ajoute yon mo \n 3- efase yon mon\n 4-modifye " 
    print(mm)

    try:
        quest = int(input("ki chwa'w ?:  "))

    except:
        print("se yon chif  pouw antre")
    return quest

klas = Diksyone_pam()



def Funct_modif():
    avis = "1- modifye yon mo 2- modifye definsyon yon mo 3- modifye kategori yon mo"
    print(avis)
    try:
        choice = int(input("ki chwa'w ?:  "))
    except:
        print("ou pa dwe antre let nan pati sa")

    if choice == 1:
        print("bravo")



def sou_meni():
    #global fonk1
    b = meni()
    choice_user = Funct_modif()

    if b == 1:
        print(1)
    if b == 2:
        print("vinn mete")
        klas.Antre()
    if b == 1:
        print("gade non frem ")
        klas.Views()
    if b == 4:
        choice_user
        # wap gen pouw fel yon sel fwa 
        # koz ou paka kreye yon tab 2 fwa
    if b == 90:
        print("li bon")
        klas.kreyasyon()

fonk2 = sou_meni()

