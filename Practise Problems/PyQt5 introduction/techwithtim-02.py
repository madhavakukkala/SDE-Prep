import sys
from PyQt5 import QtWidgets , QtGui
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QApplication , QMainWindow

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        ## Setting screen size
        self.setGeometry(200, 200, 700, 300)
        ## setting screen title
        self.setWindowTitle("Kukkapilla lu")
        ## setting icon 
        self.setWindowIcon(QIcon('C:\\Users\\aspir\\Desktop\\SDEDream\\DSA_Learns\\Python\\Python\\Practise Problems\\PyQt5 introduction\\image.png'))
        self.initUI()
    
    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Hello kukkapilla")
        self.label.setText("Hello Budankay")
        self.label.setFont(QFont("system-ui", 15))
        self.label.setGeometry(0,0,1000,100)
        self.label.setStyleSheet(
            "color: Teal;"
            "letter-spacing: -1px;"
            "background-color: black;"
        )
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click Me")
        self.b1.clicked.connect(self.clicked)


    def clicked(self):
        self.label.setText("You pressed the button")
    #     self.update()

    # def update(self):
    #     self.label.adjustSize()

def windows():

    ## Creating application
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


windows()