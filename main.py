from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class RootElement(BoxLayout):
	pass

class MyNavBar(BoxLayout):
	pass

class MyNavigator(ScreenManager):
	pass

class Home(Screen):
	pass

class Manual(Screen):
	pass

class Config(Screen):
	pass

class Reports(Screen):
	pass
	
class MainApp(App):
	def build(self):
		return RootElement()

MainApp().run()