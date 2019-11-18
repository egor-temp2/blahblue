import sys,random
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPainter, QColor,QBrush
from ui.py import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.isdraw = False

    def paintEvent(self, event):
        if self.isdraw:
            pain = QPainter()
            pain.begin(self)
            pain.setBrush(QBrush(QColor(255,223,0)))
            pain.drawEllipse(15,15,self.width-30,self.height-30)
            pain.end()

    def run(self):
        self.isdraw = True


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())