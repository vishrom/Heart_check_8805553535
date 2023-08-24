# напиши модуль для подсчета количества приседаний
from kivy.uix.label import Label
from kivy.clock import Clock

class Sits(Label):
    
    def __init__(self, total, **kwargs):
        self.curent = 0
        self.total = total
        my_text = 'Осталось приседаний: '+ str(self.curent)
        super().__init__(text = my_text, **kwargs)

    def next(self, *args):
        self.curent += 1
        new_total = max(0, self.total - self.curent)
        my_text = 'Осталось преседаний: ' + str(new_total)
        self.text = my_text