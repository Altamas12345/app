from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager

helper = """
ScreenManager:
	HomeScreen
	
<HomeScreen>:
	name: 'home'
	BoxLayout:
		orientation: 'vertical'
		MDToolbar:
			title: 'Gem Code Art'
			left_action_items: [['menu', lambda x : print("hello")]]
			right_action_items: [['bell', lambda y : print("world")]]
			
		MDBottomNavigation:

			MDBottomNavigationItem:
				name: 'homebar'
				icon: 'home'
				text: 'Home'
				MDLabel:
					text: 'Python is too op language'
					halign: 'center'
					
			MDBottomNavigationItem:
				name: 'following'
				icon: 'account'
				text: 'Subscribers'
				MDLabel:
					text: 'This is your subscribers page'
					halign: 'center'
					
			MDBottomNavigationItem:
				name: 'creator'
				icon: 'arrow-up-bold-circle-outline'
				text: 'Creator'
				MDLabel:
					text: 'This is your creator page'
					halign: 'center'
					
			MDBottomNavigationItem:
				name: 'order'
				icon: 'handshake'
				text: 'Order'
				MDLabel:
					text: 'This is your order page'
					halign: 'center'
					
			MDBottomNavigationItem:
				name: 'setting'
				icon: 'cogs'
				text: 'Setting'
				MDLabel:
					text: 'This is your setting page'
					halign: 'center'
						
"""
class HomeScreen(Screen):
	pass
	
sm = ScreenManager()
sm.add_widget(HomeScreen(name='home'))

class DemoApp(MDApp):
	
	def build(self):
		self.theme_cls.primary_palette = "Blue"
		screen = Builder.load_string(helper)
		return screen
		
DemoApp().run()