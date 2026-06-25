import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Kukkapillalu')
        self.setGeometry(50, 50, 1000, 500)
        self.setWindowIcon(QIcon('C:\\Users\\aspir\\Desktop\\SDEDream\\DSA_Learns\\Python\\Python\\Practise Problems\\PyQt5 introduction\\image.png'))

        label_image = QLabel(self)
        label_image.setGeometry(50, 50, 1000, 500)

        pixmap = QPixmap('C:\\Users\\aspir\\Desktop\\SDEDream\\DSA_Learns\\Python\\Python\\Practise Problems\\PyQt5 introduction\\image.png')
        label_image.setPixmap(pixmap)
        label_image.setGeometry((self.width() - label_image.width()) // 2,
                                (self.height() - label_image.height()) // 2,
                                label_image.width(),
                                label_image.height())



        label = QLabel("Hello Kukkapilla", self)
        label.setFont(QFont("Helvetica", 14))
        label.setGeometry(0,0,1000,100)
        label.setStyleSheet(
            "color: teal;" 
            "background-color: black;" 
            "letter-spacing: -1px;"
            
        )
        # label.adjustSize()
        # label.setAlignment(Qt.AlignTop) ## Vertically to the top
        # label.setAlignment(Qt.AlignBottom) ## Vertically to the bottom
        # label.setAlignment(Qt.AlignVCenter) ## Vertically to the center
        # label.setAlignment(Qt.AlignRight) # Align Right
        # label.setAlignment(Qt.AlignHCenter) # Align Right
        # label.setAlignment(Qt.AlignLeft) # Align Right
        
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # Center and top
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # Center and top
        label.setAlignment(Qt.AlignCenter) # Center


        
        




def main():
    app = QApplication(sys.argv)
 
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()