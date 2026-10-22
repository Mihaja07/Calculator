from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QGridLayout
import sys
from calulate import calculate


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.operation = "0"
        self.setWindowTitle("Calculator")
        self.init_UI()
        self.show()
    
    def init_UI(self):
        layout = QGridLayout(self)
        
        #Display
        self.display = QLineEdit("0", self)

        #Buttons
        nb_buttons:list[QPushButton] = []
        for i in range(0, 10):
            nb_buttons.append(QPushButton(str(i), self))
        
        op_buttons:list[QPushButton] = []
        for i in ['(', ')', '+', '-', 'x', '/', '^', '.', 'cos', 'sin', 'e', 'C', 'CE','=']:
            op_buttons.append(QPushButton(i, self))

        #Placement
        layout.addWidget(self.display, 0, 0, 1, 3)
        row = 1
        for i, button in enumerate(nb_buttons[1:]):
            if i % 3 == 0:
                row += 1
            layout.addWidget(button, row, i % 3)
        row += 1
        layout.addWidget(nb_buttons[0], row, 1)
        
        layout.addWidget(op_buttons[0], row, 0)
        layout.addWidget(op_buttons[1], row, 2)
        for i, button in enumerate(op_buttons[2:]):
            if i % 3 == 0:
                row += 1
            layout.addWidget(button, row, i % 3)
        
        #Binding
        nb_buttons[0].clicked.connect(lambda : self.add(nb_buttons[0].text()))
        nb_buttons[1].clicked.connect(lambda : self.add(nb_buttons[1].text()))
        nb_buttons[2].clicked.connect(lambda : self.add(nb_buttons[2].text()))
        nb_buttons[3].clicked.connect(lambda : self.add(nb_buttons[3].text()))
        nb_buttons[4].clicked.connect(lambda : self.add(nb_buttons[4].text()))
        nb_buttons[5].clicked.connect(lambda : self.add(nb_buttons[5].text()))
        nb_buttons[6].clicked.connect(lambda : self.add(nb_buttons[6].text()))
        nb_buttons[7].clicked.connect(lambda : self.add(nb_buttons[7].text()))
        nb_buttons[8].clicked.connect(lambda : self.add(nb_buttons[8].text()))
        nb_buttons[9].clicked.connect(lambda : self.add(nb_buttons[9].text()))
        
        op_buttons[0].clicked.connect(lambda : self.add(op_buttons[0].text()))
        op_buttons[1].clicked.connect(lambda : self.add(op_buttons[1].text()))
        op_buttons[2].clicked.connect(lambda : self.add(op_buttons[2].text()))
        op_buttons[3].clicked.connect(lambda : self.add(op_buttons[3].text()))
        op_buttons[4].clicked.connect(lambda : self.add(op_buttons[4].text()))
        op_buttons[5].clicked.connect(lambda : self.add(op_buttons[5].text()))
        op_buttons[6].clicked.connect(lambda : self.add(op_buttons[6].text()))
        op_buttons[7].clicked.connect(lambda : self.add(op_buttons[7].text()))
        op_buttons[8].clicked.connect(lambda : self.add(op_buttons[8].text()+'('))  #cos
        op_buttons[9].clicked.connect(lambda : self.add(op_buttons[9].text()+'('))  #sin
        op_buttons[10].clicked.connect(lambda : self.add(op_buttons[10].text()))
        op_buttons[11].clicked.connect(self.clear)
        op_buttons[12].clicked.connect(self.clear_all)
        op_buttons[13].clicked.connect(self.calculate)

    def add(self, string:str):
        if self.operation == "0" and string != '.':
            self.operation = string
        else:
            self.operation += string
        self.display.setText(self.operation)
    
    def clear(self):
        if len(self.operation) == 1:
            self.operation = "0"
        else:
            self.operation = self.operation[:-1]
        self.display.setText(self.operation)
    
    def clear_all(self):
        self.operation = "0"
        self.display.setText(self.operation)
    
    def calculate(self):
        result = calculate(self.operation)
        if result:
            self.display.setText(result)
            self.operation = "0"
        else:
            self.display.setText("Error")
            self.operation = "0"


if '__main__' == __name__:
    app = QApplication(sys.argv)
    window = Calculator()
    sys.exit(app.exec())