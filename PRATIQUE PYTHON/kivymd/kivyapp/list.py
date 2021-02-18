from kivymd.app import MDApp

from kivymd.uix.screen import Screen
from kivymd.uix.list import  OneLineListItem
from kivy.uix.scrollview import ScrollView 



class demo(MDApp):


	def buil(self):
		screen = Screen()
		item1 = OneLineListItem(text='Maxime')
		screen.add_widget(item1)
		return screen

demo().run()

