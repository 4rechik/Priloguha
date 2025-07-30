from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import *
from kivy.graphics.context_instructions import *

class Container(FloatLayout):
    pass

class MyApp(App):
    def build(self):

        return Container()

if __name__ == '__main__':
    MyApp().run()