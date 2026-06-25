from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication , QMainWindow ,  QWidget
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(2000,200,700,300)
    win.setWindowTitle("Kukkapilla and Budankay")

    label = QtWidgets.QLabel(win)
    label.setText("My First Label")
    label.move(50,30)

    win.show()
    sys.exit(app.exec_())



window()