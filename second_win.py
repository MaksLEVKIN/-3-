from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtGui import QFont
from instr import *  
from final_win import * 


class Experiment():
    def __init__(self, age, test1, test2, test3):
       self.age = age
       self.t1 = test1
       self.t2 = test2
       self.t3 = test3

class TestWin(QWidget):
    def __init__(self, experiment=None):
        super().__init__()
        self.exp = experiment
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
        self.timer = QTimer()

    def set_appear(self):
        self.setWindowTitle(txt_title)  
        self.resize(1000, 600) 
        self.move(100, 100)  

    def initUI(self):
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()

       
        self.txt_name = QLabel(txt_name)  
        self.btn1 = QPushButton(txt_sendresults)  
        
        self.txt_hintname = QLineEdit(self)
        self.txt_hintname.setPlaceholderText(txt_hintname)  

        self.txt_age = QLabel(txt_age)

        self.txt_hintage = QLineEdit(self)
        self.txt_hintage.setPlaceholderText(txt_hintage)

        self.txt_test1 = QLabel(txt_test1)

        self.txt_starttest1 = QPushButton(txt_starttest1)

        self.txt_hinttest1 = QLineEdit(self)
        self.txt_hinttest1.setPlaceholderText(txt_hinttest1)

        self.txt_test2 = QLabel(txt_test2)


        self.txt_starttest2 = QPushButton(txt_starttest2)

        self.txt_test3 = QLabel(txt_test3)

        self.txt_starttest3 = QPushButton(txt_starttest3)


        self.txt_hinttest2 = QLineEdit(self)
        self.txt_hinttest2.setPlaceholderText(txt_hinttest2)


        self.txt_hinttest3 = QLineEdit(self)
        self.txt_hinttest3.setPlaceholderText(txt_hinttest3)
        

        self.txt_timer = QLabel(txt_timer)  
        self.txt_timer.setStyleSheet("font-size: 60px; font-weight: bold;")


        self.r_line.addWidget(self.txt_timer)
       
        self.l_line.addWidget(self.txt_name)  
        self.l_line.addWidget(self.txt_hintname) 
        self.l_line.addWidget(self.txt_age)
        self.l_line.addWidget(self.txt_hintage) 
        self.l_line.addWidget(self.txt_test1) 
        self.l_line.addWidget(self.txt_starttest1)
        self.l_line.addWidget(self.txt_hinttest1)
        self.l_line.addWidget(self.txt_test2) 
        self.l_line.addWidget(self.txt_starttest2)
        self.l_line.addWidget(self.txt_test3) 
        self.l_line.addWidget(self.txt_starttest3)
        self.l_line.addWidget(self.txt_hinttest2)
        self.l_line.addWidget(self.txt_hinttest3)
        self.l_line.addWidget(self.btn1) 

        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def connects(self):
        self.btn1.clicked.connect(self.next_click)
        self.txt_starttest1.clicked.connect(self.timer_test)
        self.txt_starttest2.clicked.connect(self.timer_sits)
        self.txt_starttest3.clicked.connect(self.timer_final)


    def next_click(self):
        self.hide()
        self.exp = Experiment(
            int(self.txt_hintage.text()),      
            float(self.txt_hinttest1.text()),
            float(self.txt_hinttest2.text()),    
            float(self.txt_hinttest3.text())     
        )
        self.tw = FinalWin(self.exp)


    def results(self):
        self.index=(4*(int(self.exp.t1)+int(self.exp.t2)+int(self.exp.t3))-200)/10


    def timer_test(self):
        global time
        time = QTime(0, 0, 16)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)


    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.txt_timer.setText(time.toString("hh:mm:ss"))
        self.txt_timer.setFont(QFont('Times',36 , QFont.Bold))
        self.txt_timer.setStyleSheet('color: rgb (0,0,0)')
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer_sits(self):
        self.time = QTime(0, 0, 16)
        self.timer.stop()
        try:
            self.timer.timeout.disconnect()
        except TypeError:
            pass 


        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)

    def timer2Event(self):
        self.time = self.time.addSecs(-1)
        self.txt_timer.setText(self.time.toString("ss"))
        self.txt_timer.setFont(QFont('Times', 36, QFont.Bold))
        self.txt_timer.setStyleSheet('color: rgb(0, 0, 0)')
        if self.time == QTime(0, 0, 0):
            self.timer.stop()
        
    def timer_final(self):
        global time
        time = QTime(0, 0, 16)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)


    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
           self.txt_timer.setStyleSheet("color: rgb(0,255,0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
           self.txt_timer.setStyleSheet("color: rgb(0,255,0)")
        else:
           self.txt_timer.setStyleSheet("color: rgb(0,0,0)")


    