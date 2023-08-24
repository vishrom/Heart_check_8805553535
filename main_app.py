# напиши здесь свое приложение
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from instructions import txt_instruction, txt_test1, txt_test2, txt_test3, txt_sits
from ruffier import test
from seconds import Seconds
age = 7
name = ''
p1, p2, p3 = 0, 0, 0
def check_int(str_num):
    try:
        return int(str_num)
    except:
        return False

class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        infor = Label(txt = txt_instruction)
        lbl1 = Label(text = 'Введите имя', halign = 'right')
        self.in_name = TextInput(text = '7', multiline = False)
        lbl2 = Label(text = 'Введите возраст', halign = 'right')
        self.in_age = TextInput(multiline = False)
        self.btn = Button(text = 'Начать', size_hint = (0.3, 0.2), pos_hint = ('center_x': 0.5))
        self.btn.on_press = self.next
        line1 = BoxLayout( size_hint = (0.8, None), height = '36sp')
        line1.add_widget(lbl1)
        line1.add_widget(self.in_name)
        line2 = BoxLayout( size_hint = (0.8, None), height = '36sp')
        line2.add_widget(self.in_age)
        line2.add_widget(lbl2)
        outer = BoxLayout(orientation = 'vertical', padding = 8, sprasing = 8)
        outer.add_widget(infor)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        self.add_widget(outer)

    def next(self):
        name = self.in_name.text
        age = check_int(self.in_age.text)
        if age == False or age < 7:
            age = 7
            self.in_age.text = str(age)
        else:
            self.manager.current = "Pscr1"

class PulsScreen1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False

        instr = Label(text = txt_test1)
        self.al1_sec = Second(10)
        self.al1_sec.bind(done=self.sec_finished)

        line = BoxLayout( size_hint = (0.8, None), height = '36sp')
        al1_result = Label(text = 'Введите результат')
        self.al1_result = TextInput(text = '0', multiline = False)
        self.in_result.set_disabled(True)
        
        line.add_widget(al1_result)
        line.add_widget(self.in_result)
        self.btn = Button(text = 'Начать', size_hint = (0.3, 0.2), pos_hint = ('center_x': 0.5))
        self.btn.on_press = self.next
        outer = BoxLayout(orientation = 'vertical', padding = 8, sprasing = 8)
        outer.add_widget(instr)
        outer.add_widget(self.al1_sec)
        outer.add_widget(line)
        outer.add_widget(self.btn)
        self.add_widget(outer)
    
    def sec_finished(self, *args):
        self.next_screen = True
        self.in_result.set_disabled(False)
        self.btn.set_disabled(False)
        self.btn.text = 'Продолжить'

    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.al1_sec.start()
        else:
            global p1
            p1 = check_int(self.in_result.text)
            if p1 == False or p1 <= 0:
                p1 = 0
                self.in_result.text = str(p1)
            else:
                self.manager.current = "Check"

class CheckScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        infor = Label(txt = txt_sits)
        self.lbl_sist = Sits(30)
        self.run = Runner(total = 30, steptime = 1.5, size_hint())
        self.run.bind(finished = self.run_finished)

        line = BoxLayout()
        vlay = BoxLayout(orientation = 'vertical', size_hint = (0.3, 1))
        vlay.add_widget()
        self.instr = Label(text = '')
        self.btn = Button(text = 'Начать', size_hint = (0.3, 0.2), pos_hint = ('center_x': 0.5))
        self.btn.on_press = self.next
        outer = BoxLayout(orientation = 'vertical', padding = 8, sprasing = 8)
        outer.add_widget(infor)
        outer.add_widget(self.btn)
        self.add_widget(outer)


    def next(self):
        self.manager.current = "Pscr2"

class PulsScreen2(Screen):
    def __init__(self, **kwargs):
        self.next_screen = False
        self.stage = 0
        super().__init__(**kwargs)
        infor = Label(txt = txt_test3)
        line1 = BoxLayout( size_hint = (0.8, None), height = '36sp')
        self.al1_sec = Second(15)
        self.al1_sec.bind(done=self.sec_finished)
        self.al1txt = Label(text = 'Считайте пульс')

        lbl_result1 = Label(test = 'Результат', haling = 'right')
        self.in_result1 = TextInput(text = '0', multiline = False)
        line1.add_widget(lbl_result1)
        line1.add_widget(self.in_result1)
        line2 = BoxLayout( size_hint = (0.8, None), height = '36sp')
        lbl_result2 = Label(text = 'Результат после отдыха:', height = 'right')
        self.in_result2 = TextInput(text = '0', multiline = False)

        self.in_result1.set_disabled(True)
        self.in_result2.set_disabled(True)
        line2.add_widget(lbl_result2)
        line2.add_widget(self.in_result2)
        self.btn = Button(text = 'Завершить', size_hint = (0.3, 0.2), pos_hint = ('center_x': 0.5))
        self.btn.on_press = self.next
        outer = BoxLayout(orientation = 'vertical',, padding = 8, sprasing = 8)
        outer.add_widget(infor)
        outer.add_wiget(self.al1txt)
        outer.add_wiget(self.al1_sec)
        outer.add_widget(lbl1)
        outer.add_widget(lbl2)
        outer.add_widget(self.btn)
        self.add_widget(outer)
    
    def sec_finished(self, *args):
        if self.al1_sec.done:
            if self.stage == 0:
                self.stage = 1
                self.al1txt.text = 'Отдыхайте'
                self.al1_sec.restart(30)
                self.in_result1.set_disabled(False)
            elif self.stage == 1:
                self.stage = 2
                self.al1txt.text = 'Считайте пульс'
                self.al1_sec.restart(15)
            elif self.stage == 2:
                self.in_result2.set_disabled(False)
                self.btn.set_disabled(False)
                self.btn.text = 'Завершить'
                self.next_screen = True

    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.al1_sec.start()
        else:
            global p2, p3
            p2 = check_int(self.in_result1.text)
            p3 = check_int(self.in_result2.text)
            if p2 == False:
                p2 = 0
                self.in_result1.text = str(p2)
            elif p3 == False:
                p3 = 0
                self.in_result2.text = str(p2)
            else:
                self.manager.current = "result"
    




class Result(Screen)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.outer = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        self.instr = Label(text = '')
        self.outer.add_widget(self.instr)
        self.add_widget(self.outer)
        self.on_press = self.before
    def bafore(self):
        global name
        self.instr.text = name +'\n' + test(p1, p2, p3, age)

class EndScr(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr(name ='instr'))
        sm.add_widget(PulsScreen1(name = "Pscr1"))
        sm.add_widget(CheckScreen(name = "Check"))
        sm.add_widget(PulsScreen2(name = "Pscr2"))
        sm.add_widget(Result(name = "result"))
        return sm
        
app = EndScr()
app.run