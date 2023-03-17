# Разработка простейшего калькулятора для десятичных чисел

import sys
import math

from PyQt6.QtWidgets import QApplication, QMainWindow
from UIMainWindow import Ui_MainWindow


class Operations:
    Not = 0
    Plus = 1
    Minus = 2
    Multiplication = 3
    Division = 4
    Power = 5


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.operand = None
        self.operation = 0
        self.needClear = False

        self.operations = Operations

        self.Button0.clicked.connect(self.print(0))
        self.Button1.clicked.connect(self.print(1))
        self.Button2.clicked.connect(self.print(2))
        self.Button3.clicked.connect(self.print(3))
        self.Button4.clicked.connect(self.print(4))
        self.Button5.clicked.connect(self.print(5))
        self.Button6.clicked.connect(self.print(6))
        self.Button7.clicked.connect(self.print(7))
        self.Button8.clicked.connect(self.print(8))
        self.Button9.clicked.connect(self.print(9))

        self.ButtonComma.clicked.connect(self.print_comma)

        self.ButtonClear.clicked.connect(self.clear)
        self.ButtonBackspace.clicked.connect(self.backspace)

        self.ButtonSqrt.clicked.connect(self.sqrt)
        self.ButtonLogarifm.clicked.connect(self.logarithm)
        self.ButtonPlusMinus.clicked.connect(self.sign_change)
        self.ButtonFactorial.clicked.connect(self.factorial)
        self.ButtonPercent.clicked.connect(self.percent)

        self.ButtonPlus.clicked.connect(self.do_operation(self.operations.Plus))
        self.ButtonMinus.clicked.connect(self.do_operation(self.operations.Minus))
        self.ButtonMultiplication.clicked.connect(self.do_operation(self.operations.Multiplication))
        self.ButtonDivision.clicked.connect(self.do_operation(self.operations.Division))
        self.ButtonPower.clicked.connect(self.do_operation(self.operations.Power))

        self.ButtonEquals.clicked.connect(self.equals)

        # self.Button1.click()

    def set_text_num(self, num):
        if num == int(num):
            self.lineEdit.setText(str(int(num)))
        else:
            self.lineEdit.setText(str(num))

    def set_error_text(self):
        self.lineEdit.setText("Error!")
        self.needClear = True
        self.operation = Operations.Not
        self.operand = None

    def print(self, num):

        def outFunc(e):
            text = self.lineEdit.text()

            if text == "0" or self.needClear:
                self.needClear = False
                self.lineEdit.setText(str(num))
            else:
                self.lineEdit.setText(text+str(num))

        return outFunc

    def print_comma(self, e):
        text = self.lineEdit.text()

        if text == "":
            self.lineEdit.setText("0.")
        elif text.find(".") != -1:
            return
        else:
            self.lineEdit.setText(text + ".")

    def clear(self, e):
        self.lineEdit.setText("0")
        self.needClear = False
        self.operation = self.operations.Not
        self.operand = None

    def sqrt(self, e):
        text = self.lineEdit.text()

        if text == "Error!" or float(text) < 0:
            self.set_error_text()
        elif text == "":
            self.lineEdit.setText("0")
        else:
            self.set_text_num(math.sqrt(float(text)))

    def logarithm(self, e):
        text = self.lineEdit.text()

        if text == "" or text == "Error!" or float(text) <= 0:
            self.set_error_text()
        else:
            self.set_text_num(math.log(float(text), math.e))

    def sign_change(self, e):
        text = self.lineEdit.text()

        if text == "" or text == "Error!":
            self.set_text_num(0)
        else:
            self.set_text_num(-float(text))

    def factorial(self, e):
        text = self.lineEdit.text()

        if text == "Error!" or float(text) < 0 or float(text) != int(float(text)):
            self.set_error_text()
        elif text == "":
            self.lineEdit.setText("0")
        else:
            self.set_text_num(math.factorial(int(text)))

    def percent(self, e):
        text = self.lineEdit.text()

        if text == "Error!" or self.operand is None:
            self.set_error_text()
        else:
            self.lineEdit.setText(str((float(text)*self.operand)/100))
            self.equals("")

    def backspace(self, e):
        text = self.lineEdit.text()

        if text == "" or text[:-1] == "" or self.needClear:
            self.lineEdit.setText("0")
            self.needClear = False
        else:
            self.lineEdit.setText(text[:-1])

    def equals(self, e):
        num = float(self.lineEdit.text())

        if self.operation == self.operations.Not or self.lineEdit.text() == "Error!":
            return
        elif self.operation == self.operations.Plus:
            self.set_text_num(self.operand + num)
        elif self.operation == self.operations.Minus:
            self.set_text_num(self.operand - num)
        elif self.operation == self.operations.Multiplication:
            self.set_text_num(self.operand * num)
        elif self.operation == self.operations.Division:
            if float(self.lineEdit.text()) == 0:
                self.set_error_text()
            else:
                self.set_text_num(self.operand / num)
        elif self.operation == self.operations.Power:
            self.set_text_num(math.pow(self.operand, num))

        self.operand = None
        self.needClear = True
        self.operation = self.operations.Not

    def do_operation(self, op):

        def out(e):
            if self.lineEdit.text() == "Error!":
                self.operand = 0
            elif self.operand is not None:
                if self.operation == self.operations.Plus:
                    self.operand += float(self.lineEdit.text())
                elif self.operation == self.operations.Minus:
                    self.operand -= float(self.lineEdit.text())
                elif self.operation == self.operations.Multiplication:
                    self.operand *= float(self.lineEdit.text())
                elif self.operation == self.operations.Division:
                    if float(self.lineEdit.text()) == 0:
                        self.set_error_text()
                    else:
                        self.set_text_num(self.operand / float(self.lineEdit.text()))
                elif self.operation == self.operations.Power:
                    self.operand = math.pow(self.operand, float(self.lineEdit.text()))

                self.set_text_num(self.operand)
            else:
                self.operand = float(self.lineEdit.text().replace(",", '.'))

            self.operation = op
            self.needClear = True

        return out


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
