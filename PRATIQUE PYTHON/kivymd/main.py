from kivymd.app import MDApp
from kivymd.uix.screen import Screen 
from kivymd.uix.list  import ThreeLineListItem , MDList
from kivy.uix.scrollview import ScrollView 


class DemoApp(MDApp):
	def build(self):
		m = input("mete nom w :" )
		screen = Screen()
		scroll = ScrollView()
		list_view = MDList()
		scroll.add_widget(list_view)

		for i in range(20):
			items = ThreeLineListItem(text= "je suis la"  + str(i),secondary_text='je suis la',
				tertiary_text='Mon app va fonctionner normalment')
			list_view.add_widget(items)


		screen.add_widget(scroll)

		return screen

DemoApp().run()
