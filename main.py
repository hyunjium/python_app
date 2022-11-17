import random

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.screenmanager import ScreenManager, Screen

class MainWindow(Screen):
    pass
class CroWindow(Screen):
    def on_enter(self, *args):
        self.ids.resetColor1.background_color = (1, 1, 1, 0)
        self.ids.resetColor2.background_color = (1, 1, 1, 0)
        self.ids.resetColor3.background_color = (1, 1, 1, 0)
        self.ids.resetColor4.background_color = (1, 1, 1, 0)
        self.ids.resetColor5.background_color = (1, 1, 1, 0)
        self.ids.resetColor6.background_color = (1, 1, 1, 0)
        self.ids.resetColor7.background_color = (1, 1, 1, 0)
        self.ids.resetColor8.background_color = (1, 1, 1, 0)
        self.ids.resetColor9.background_color = (1, 1, 1, 0)
        self.ids.resetColor10.background_color = (1, 1, 1, 0)

    randomButton_pos = ObjectProperty(None)
    def _update_pos(self):
        self.randomButton_pos = self._random_pos()

    def _random_pos(self):
        pos = random.choice(({"x":0.07, "y":0.35},
                             {"x": 0.05, "y": 0.25},
                             {"x": 0.05, "y": 0.155},
                             {"x": 0.13, "y": 0.07},
                             {"x": 0.33, "y": 0.05},
                             {"x": 0.55, "y": 0.05},
                             {"x": 0.74, "y": 0.07},
                             {"x": 0.82, "y": 0.155},
                             {"x": 0.81, "y": 0.25},
                             {"x": 0.8, "y": 0.35}))
        return pos

class RandomButton(Button):
    def on_press(self):
        pass

class CrocWindow(Screen):
    pass
class LottoWindow(Screen):
    pass
class RouletteWindow(Screen):
    def generate_number(self):
        self.random_label.text = str(random.randint(0,10))
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