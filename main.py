from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.screenmanager import ScreenManager, Screen

class MainWindow(Screen):
    pass
class CroWindow(Screen):
    pass

class CrocWindow(Screen):
    pass
class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('Window.kv')


class HelloApp(App):
    def build(self):
        Window.size = (350, 670)
        Window.clearcolor = get_color_from_hex('#d0fc5c')
        return kv

if __name__ == '__main__':
    HelloApp().run()





