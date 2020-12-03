# kreye yon sistem maket 
# wap ka we produi yo wap ka ht ak peye tou
# ak CLASS m panse lap pi bon 
import datetime
import os
import pickle

class Maket:
	nom = "MAX_MARKET"
	proprietaire = "MAXIME"

	def __init__(self):
		self.solde_taks = 0
		self.p_pen = 20 # goud
		self.p_corn_flake = 500 
		self.p_lait = 400
		self.p_fromaj = 150 
		self.p_jus = 180
		self.solde_market = 0
		self.solde_achat = 0



	def payment(self):
		arg = int(input("antre kob lan:  "))
		if arg < self.solde_achat:
			print("kob sa trop piti ou frem ")
		elif arg == self.solde_achat:
			print("achat a bien fet ak siske")


	def achat_one(self):
		start = True
		prices = 0
		sum_total = 0
		print("BONJOUR KLIYAN SISTEM SA AP MANDEW KISA WAP ACHTE \n SI TOUT FWA OU PAP ACHTE ANKO EKRI --non--") 
		while start:
			mande = input("kisa wap achte ? :  ")
			if mande == "non":
				start = False
				print("MESI PASKEU OU TE ITILIZE SEVIS NOU AN")
				print("\n")
				print("ou achte pou {} goud".format(sum_total))
				self.solde_achat += sum_total 
				p = self.payment()

			# kondisyon sa ap teste pwodui pou li tou bay prix an
			elif mande == "pen":
				prices = self.p_pen
				sum_total += prices
				print("sa ap koute {} goud".format(sum_total))

			elif mande == "let":
				prices = self.p_lait
				sum_total += prices
				print("sa ap koute {} goud".format(sum_total))




	def pwodwi(self):
		file_name = "price.txt"
		fichye_mwen = open(file_name, "r")
		gade = fichye_mwen.read()
		print(gade)
		fichye_mwen.close()


		
		# pati sa se pou met maket lan pou li ka gen kontrol bhy yo 
	def admin(self):
		print("BIENVINI NAN PATI ADMIN AN {}".format(self.proprietaire))
		print("\n")
		print("")



# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  pati sa se pou jere meni ak res program lan 		
def meni():
	text = "1- Pouw ka we Pwodwi yo ak tout pri yo \n 2- pouw achte "

	print(text)

	mande_one = int(input("Ki chwa'w ? :  "))
	return mande_one

def secure():
	global me
	vre = True 
	modpas = "maxdev01"
	essaie = 3
	while vre:
		mande = input("antre modpas lan siw se admin vre :  ")
		if mande != modpas:
			essaie -= 1
			print("modpas sa pa bon ou rete {} chans pou eseye anko".format(essaie))

			if essaie == 0:
				print("ou pa admin an vre ")
				vre = False
				redirect = meni()

		elif mande == modpas:
			vre = False
			me.admin()

		 

me = Maket()
user = meni()

def content():
	global user 
	if user == 1:
		me.pwodwi()

	elif user == 80:
		redirect = secure()


oui = content()

"""
if user == 1:
	me.pwodwi()
elif user == 80:
	m = secure()


elif user == 2:
	me.achat_one()
	"""
