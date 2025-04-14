from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
)
from PyQt5.QtCore import Qt
from instr import * 
from second_win import TestWin



class Experiment:
    def __init__(self):
        self.t1 = 0
        self.t2 = 0
        self.t3 = 0


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.exp = Experiment()  
        self.initUI()
        self.set_appear()
        self.connects()

    def set_appear(self): 
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)

        btn_layout = QHBoxLayout()
        btn_layout.addStretch(1)
        btn_layout.addWidget(self.button)
        btn_layout.addStretch(1)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.instruction, alignment=Qt.AlignCenter)
        self.layout.addLayout(btn_layout)  
        self.setLayout(self.layout)

    def connects(self): 
        self.button.clicked.connect(self.next_click)
  
    def next_click(self):
        self.hide()
        self.tw = TestWin(self.exp) 

app = QApplication([])
mw = MainWin()
mw.show()
app.exec_()

