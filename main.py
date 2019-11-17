import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from ui.py import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.label.setText("OK")


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())