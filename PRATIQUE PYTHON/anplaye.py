# Pati sa vre impotan nap komnse kreye yon pati admin
# Paskeu se yon moun ki impotan nan antreprise la kap ka antre nom moun sou sistem lan 




def akey():
	mesaj = "1- Anrejistre anplwaye \n 2- Gade konbyen anplwaye ou genyn 3- chache yon anplwaye 4- modifye yon done"

	print(mesaj)

	akey_kesyon = int(input("ki chwa'w ? :  "))

	return akey_kesyon

pa_defo = akey()

def kontrol_akey():
	global pa_defo

	if pa_defo == 1:
		print("oui")