from kivymd.app import MDApp
from kivy.md.uix.screen import Screen 
from kivymd.uix.textfield import MDTextField 


class Login(MDApp):


	def build(self):

		ecran = Screen()
		username = MDTextField(text='Entrez votre nom svp ',
								post_hint={'center_x': 0.5,
								'center_y': 0.5})


		ecran.add_widget(username)

		return ecran

Login().run()