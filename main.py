from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
#from kivy.core.window import Window
import login
import faild
import Mobile
#import Content


Builder.load_file('login.kv'),Builder.load_file('faild.kv'),Builder.load_file('cont.kv'),Builder.load_file('mobile.kv')


sm = ScreenManager()

class Test(MDApp):
    def build(self):
        sm.add_widget(login.login(name="log"))
        sm.add_widget(faild.faild(name="faild"))
        sm.add_widget(Mobile.MobileView(name="logok"))

        return sm


Test().run()

