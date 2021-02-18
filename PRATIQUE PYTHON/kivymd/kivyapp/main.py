from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon 


class demo(MDApp):

	def build(self):
		label = MDLabel(text= "Maxime MILIEN dit Maxdev01 ", halign='left', theme_text_color = 'Primary',
			   text_color = (1,10,1),
			   font_style = "H4")

		#icon_label = MDIcon(icon='language-python')
		#li = [label, icon_label]

		return label

runapp = demo().run()







''''
men ki propriete ou ka use sou halign lan
'left', 'center', 'right', 'justify', 'auto'


'''