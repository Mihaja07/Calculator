from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
import sys


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.show()
    
    def init_UI(self):
        pass

if '__main__' == __name__:
    app = QApplication(sys.argv)
    window = Calculator()
    sys.exit(app.exec())