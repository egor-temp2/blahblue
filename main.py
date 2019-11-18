import sys,random
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPainter, QColor,QBrush
from ui import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.circles = list()
        self.isdraw = False

    def paintEvent(self, event):
        if self.isdraw:
            pain = QPainter()
            pain.begin(self)
            pain.setBrush(QBrush(QColor(255,223,0)))
            for i in self.circles:
                pain.drawEllipse(i[0],i[1],i[2],i[3])

            pain.end()

    def run(self):
        self.isdraw = True
        n = random.randint(0, 40)
        self.circles.append([random.randint(0,self.window().width()-1),random.randint(0,self.window().height()-1),n,n])
        self.update()

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())