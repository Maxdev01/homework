# sistem sa lap tankou mon cash
# men lap rele max_payment
# pou komanse lap gen yon pati ladan pou w enskri

# ^^^^^^^^^^^^^^^^^^^^^^^^ se ak method CLASS m fel ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
import pickle
from anplaye import *
class Max_credit:
	


	def __init__(self):
		self.met_li = "MILIEN Maxime"
		self.solde_kont = 0
		self.solde_total = 0
		self.kod_sekre_kliyan = ""
		self.epsedo_kliyan = ""



	

	def bazdone(self):
		done_pam = {"epsedo": self.epsedo_kliyan, "kod sekre a": self.kod_sekre_kliyan}
		non_fichye = "baz_done_an.db"
		with open(non_fichye , "wb" ) as fichye:
			pickle.dump(done_pam, fichye)
	
	def inskripsyon(self):
		demare = True
		
		print("BYENVINI NAN SISTEM NOU AN ")
		while demare:
			non = input("antre nonw : ")
			siyatiw = input("Antre siyatiw :  ")
			try:
				kod = int(input("antre kod sekre'w svp :  "))
				konv = str(kod)
				konv1 = len(konv)


			except ValueError:
				print("ou dwe mete let ladan")
			if konv1 < 4:
				print("li pa dwe pi piti ke 4 chif ")
				demare = False

			elif konv == 4:
				print("kod sekre an valide")
				kod_sekre_kliyan += konv1

			epsedo = input("antre  yon epsedo' --username-- : ")
			print("0- Pou'w ka kite 3- Pou'w ka we info ki enpotan yo pouw ka sonje yo \n paskeu se avek yo wap gen pouw fe transaksyon ")
			self.epsedo_kliyan += epsedo
			kesyon2 = int(input("ki chwa'w ? : "))
			if kesyon2 == 0:
				demare = False
			elif kesyon2 == 3:
				done = {"epsedo": epsedo , "kod": konv}

				print("Ou enskri avek siske sou sistem nou an men Infomasyon ki enpotan wap gen pouw konnen yo")
				print(done)
				demare = False





	# pati sa se pou admin an li ye
	# lap ka we konbyn ki enskri
	# lap ka we konbyn anplaye li genyen kap travay pou li

	def Administrasyon(self):
		print("{} BYENVINI NAN SISTEM Administrasyon an".format(self.met_li))



############# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 	PATI SA SE LI KAP JERE DIREKSYON YO ^^^^^^^^^^^^^^^^^^^^^^^^^
# pati sa gen sipoze gen plusieurr fonksyon gen jere transaksyon ak direje meni an


# @@@@@@@ fonksyon sa ap la pou jere sekire admin an

def panel_akey():
	afich = "1- enskri \n 2- fe yon depot \n 3- fe yon retre "
	print(afich)

	kesyon = int(input("ki chwa'w ? :  "))

	return kesyon


mine = Max_credit()
first = panel_akey()


def Lock():
	global mine
	
	true_password = "lovejesus"
	avis = "bye"
	demare_one = True
	trying = 3
	while demare_one:
		mdp = input("antre modpas lan siw se admin an vre:  ")
		if mdp != true_password:
			trying -= 1
			print("li pa bon ou rete {} chans pouw eseye anko".format(trying))

			if trying == 0:
				print("se pa ou")
				demare_one = False
				panel_akey()
		elif mdp == true_password:
			mine.Administrasyon()
			demare_one = False



def jere_meni():
	global first

	if first == 1:
		mine.inskripsyon()
	elif first == 6:
		mine.bazdone()
	elif first == 9:
		Lock()
	elif first == 91:
		m = hi()
	else:
		print("nou pa konn opsyon sa")
	return "bye"

second = jere_meni()
