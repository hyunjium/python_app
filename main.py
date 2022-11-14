import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.gridlayout import GridLayout

Builder.load_file('round_buttons.kv')

class MyLayout(Widget):
    pass


class HelloApp(App):
    def build(self):
        Window.size = (350, 670)
        Window.clearcolor = get_color_from_hex('#d0fc5c')
        return MyLayout()

if __name__ == '__main__':
    HelloApp().run()

        #mylayout = BoxLayout(orientation="vertical")
        #mylabel = Label(text="Hello!", font_size = 40)
        #mybutton = Button(text="Start", font_size = 30)
        #mylayout.add_widget(mylabel)
        #mylayout.add_widget(mybutton)
        #mybutton.bind(on_press=lambda a: print(mylabel.text))
        #return mylayout
        #return mylabel





