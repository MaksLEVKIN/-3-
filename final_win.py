from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from instr import * 
from final_win import * 

class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.set_appear()
        self.initUI()
        self.show()

    def set_appear(self): 
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        # Вычисляем результаты заранее, чтобы их можно было использовать в тексте
        result_text = self.results()

        # Создаём текстовые метки
        self.work_text = QLabel(txt_workheart + result_text)
        self.index_text = QLabel(txt_index + str(self.index))

        # Размещение виджетов
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.index_text)
        self.layout.addWidget(self.work_text)
        self.setLayout(self.layout)

    def results(self):
        self.index = (4 * (int(self.exp.t1) + int(self.exp.t2) + int(self.exp.t3)) - 200) / 10
        if self.exp.age >= 15:
            if self.index >= 15:
                return txt_res1
            elif self.index<=14.9 and self.index>=11:
                return txt_res2
            elif self.index< 6 and self.index>= 10.9:
                return txt_res3
            elif self.index< 0.5 and self.index>= 5.9:
                return txt_res4
            elif self.index>=0.4:
                return txt_res5
        return "Error"  # Возвращаем ошибку, если возраст меньше 15 лет