import random
import re

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
    def generate_number(self):
        prior = self.lotto_number.text
        line = prior.splitlines()
        linelen = len(line)
        if len(line) == 1:
            for i in range(10):
                number = str(random.randint(1, 45))
                if prior == '_':
                    self.random_label.text = number
                    if int(number) <= 9:
                        self.lotto_number.text = f'{0}{number}'
                    else:
                        self.lotto_number.text = f'{number}'
                    break
                elif number in re.findall(r'\b\d+\b', prior):
                    continue
                elif len(re.findall(r'\b\d+\b', prior)) == 7:
                    self.random_label.text = "You got all numbers!"
                    break
                else:
                    self.random_label.text = number
                    if int(number) <= 9:
                        self.lotto_number.text = f'{prior}{" "}{0}{number}'
                    else:
                        self.lotto_number.text = f'{prior}{" "}{number}'
                    break
        elif linelen >= 2:
            for i in range(10):
                number = str(random.randint(1, 45))
                if '_' in prior:
                    self.random_label.text = number
                    line[linelen-1] = ''
                    all_num = ''
                    for x in line:
                        if x == line[linelen - 1]:
                            all_num += x
                        else:
                            all_num += x + '\n'
                    if int(number) <= 9:
                        self.lotto_number.text = f'{all_num}{0}{number}'
                    else:
                        self.lotto_number.text = f'{all_num}{number}'
                    break
                elif number in re.findall(r'\b\d+\b', line[linelen-1]):
                    continue
                elif len(re.findall(r'\b\d+\b', line[linelen-1])) == 7:
                    self.random_label.text = "You got all numbers!"
                    break
                else:
                    self.random_label.text = number
                    if int(number) <= 9:
                        self.lotto_number.text = f'{prior}{" "}{0}{number}'
                    else:
                        self.lotto_number.text = f'{prior}{" "}{number}'
                    break

    def generate_more_number(self):
        prior = self.lotto_number.text
        if len(re.findall(r'\b\d+\b', prior)) <= 34:
            if '_' not in prior:
                self.random_label.text = '_'
                self.lotto_number.text = f'{prior}\n{"_"}'



class RouletteWindow(Screen):
    def select_option(self):
        number_of_options = self.ids.number_option.text
        if '1' in number_of_options:
            answer = self.ids.option1.text
            self.ids.answer.text = answer
        elif '2' in number_of_options:
            answer = random.choice((self.ids.option1.text,
                                    self.ids.option2.text))
            self.ids.answer.text = answer
        elif '3' in number_of_options:
            answer = random.choice((self.ids.option1.text,
                                    self.ids.option2.text,
                                    self.ids.option3.text))
            self.ids.answer.text = answer
        elif '4' in number_of_options:
            answer = random.choice((self.ids.option1.text,
                                    self.ids.option2.text,
                                    self.ids.option3.text,
                                    self.ids.option4.text))
            self.ids.answer.text = answer
        elif '5' in number_of_options:
            answer = random.choice((self.ids.option1.text,
                                    self.ids.option2.text,
                                    self.ids.option3.text,
                                    self.ids.option4.text,
                                    self.ids.option5.text))
            self.ids.answer.text = answer
        else:
            answer = random.choice((self.ids.option1.text,
                                    self.ids.option2.text,
                                    self.ids.option3.text,
                                    self.ids.option4.text,
                                    self.ids.option5.text,
                                    self.ids.option6.text))
            self.ids.answer.text = answer


    def add_option(self):
        number_of_options = self.ids.number_option.text
        if '1' in number_of_options:
            self.ids.option2.background_color = (1,1,1,1)
            self.ids.number_option.text = "# of Options: 2"
        elif '2' in number_of_options:
            self.ids.option2.background_color = (1, 1, 1, 1)
            self.ids.option3.background_color = (1, 1, 1, 1)
            self.ids.number_option.text = "# of Options: 3"
        elif '3' in number_of_options:
            self.ids.option2.background_color = (1, 1, 1, 1)
            self.ids.option3.background_color = (1, 1, 1, 1)
            self.ids.option4.background_color = (1, 1, 1, 1)
            self.ids.number_option.text = "# of Options: 4"
        elif '4' in number_of_options:
            self.ids.option2.background_color = (1, 1, 1, 1)
            self.ids.option3.background_color = (1, 1, 1, 1)
            self.ids.option4.background_color = (1, 1, 1, 1)
            self.ids.option5.background_color = (1, 1, 1, 1)
            self.ids.number_option.text = "# of Options: 5"
        else:
            self.ids.option2.background_color = (1, 1, 1, 1)
            self.ids.option3.background_color = (1, 1, 1, 1)
            self.ids.option4.background_color = (1, 1, 1, 1)
            self.ids.option5.background_color = (1, 1, 1, 1)
            self.ids.option6.background_color = (1, 1, 1, 1)
            self.ids.number_option.text = "# of Options: 6"
            self.ids.plus_button.text = '.'

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