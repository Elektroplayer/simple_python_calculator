from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QLineEdit as Qle

class QLineEdit(Qle):
    def __init__(self, wg):
        self.wg = wg
        super().__init__(self.wg)

        self.funcs = {}

    def init_funcs(self, f):
        self.funcs = f

    def keyPressEvent(self, e):
        # отработать символ внутри поля ввода
        k = e.key()

        if str(k) in self.funcs:
            self.funcs[str(k)].click()
        else:
            super().keyPressEvent(e)

class Ui_MainWindow(object):
    def get_button(self, obj_name):
        button = QtWidgets.QPushButton(self.centralwidget)

        button_size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        button_size_policy.setHorizontalStretch(0)
        button_size_policy.setVerticalStretch(0)
        button_size_policy.setHeightForWidth(button.sizePolicy().hasHeightForWidth())

        button_font = QtGui.QFont()
        button_font.setPointSize(14)

        button.setSizePolicy(button_size_policy)
        button.setFont(button_font)
        button.setObjectName(obj_name)

        return button

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(468, 411)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.lineEdit.setObjectName("lineEdit")

        validator = QtGui.QDoubleValidator()
        validator.setLocale(QtCore.QLocale("UnitedStates"))

        self.lineEdit.setValidator(validator)

        self.verticalLayout_6.addWidget(self.lineEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.ButtonLogarifm = self.get_button("ButtonLogarifm")
        self.verticalLayout.addWidget(self.ButtonLogarifm)

        self.Button7 = self.get_button("Button7")
        self.verticalLayout.addWidget(self.Button7)

        self.Button4 = self.get_button("Button4")
        self.verticalLayout.addWidget(self.Button4)

        self.Button1 = self.get_button("Button1")
        self.verticalLayout.addWidget(self.Button1)

        self.Button0 = self.get_button("Button0")
        self.verticalLayout.addWidget(self.Button0)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.ButtonPower = self.get_button("ButtonPower")
        self.verticalLayout_2.addWidget(self.ButtonPower)

        self.Button8 = self.get_button("Button8")
        self.verticalLayout_2.addWidget(self.Button8)

        self.Button5 = self.get_button("Button5")
        self.verticalLayout_2.addWidget(self.Button5)

        self.Button2 = self.get_button("Button2")
        self.verticalLayout_2.addWidget(self.Button2)

        self.ButtonComma = self.get_button("ButtonComma")
        self.verticalLayout_2.addWidget(self.ButtonComma)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.ButtonSqrt = self.get_button("ButtonSqrt")
        self.verticalLayout_3.addWidget(self.ButtonSqrt)

        self.Button9 = self.get_button("Button9")
        self.verticalLayout_3.addWidget(self.Button9)

        self.Button6 = self.get_button("Button6")
        self.verticalLayout_3.addWidget(self.Button6)

        self.Button3 = self.get_button("Button3")
        self.verticalLayout_3.addWidget(self.Button3)

        self.ButtonMinus = self.get_button("ButtonMinus")
        self.verticalLayout_3.addWidget(self.ButtonMinus)

        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.ButtonFactorial = self.get_button("ButtonFactorial")
        self.verticalLayout_5.addWidget(self.ButtonFactorial)

        self.ButtonPercent = self.get_button("ButtonPercent")
        self.verticalLayout_5.addWidget(self.ButtonPercent)

        self.ButtonDivision = self.get_button("ButtonDivision")
        self.verticalLayout_5.addWidget(self.ButtonDivision)

        self.ButtonMultiplication = self.get_button("ButtonMultiplication")
        self.verticalLayout_5.addWidget(self.ButtonMultiplication)

        self.ButtonPlus = self.get_button("ButtonPlus")
        self.verticalLayout_5.addWidget(self.ButtonPlus)

        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.ButtonBackspace = self.get_button("ButtonBackspace")
        self.verticalLayout_4.addWidget(self.ButtonBackspace)

        self.ButtonClear = self.get_button("ButtonClear")
        self.verticalLayout_4.addWidget(self.ButtonClear)

        self.ButtonPlusMinus = self.get_button("ButtonPlusMinus")
        self.verticalLayout_4.addWidget(self.ButtonPlusMinus)

        self.ButtonEquals = self.get_button("ButtonEquals")
        self.verticalLayout_4.addWidget(self.ButtonEquals)

        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.lineEdit.init_funcs({
            "48": self.Button0,
            "49": self.Button1,
            "50": self.Button2,
            "51": self.Button3,
            "52": self.Button4,
            "53": self.Button5,
            "54": self.Button6,
            "55": self.Button7,
            "56": self.Button8,
            "57": self.Button9,

            "42": self.ButtonMultiplication,
            "43": self.ButtonPlus,
            "45": self.ButtonMinus,
            "47": self.ButtonDivision,
            "94": self.ButtonPower,

            "16777220": self.ButtonEquals,
            "16777219": self.ButtonBackspace,
            "16777223": self.ButtonComma,
            "44": self.ButtonComma
        })

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Простой калькулятор"))
        self.lineEdit.setText(_translate("MainWindow", "0"))
        self.ButtonLogarifm.setText(_translate("MainWindow", "ln x"))
        self.Button7.setText(_translate("MainWindow", "7"))
        self.Button4.setText(_translate("MainWindow", "4"))
        self.Button1.setText(_translate("MainWindow", "1"))
        self.Button0.setText(_translate("MainWindow", "0"))
        self.ButtonPower.setText(_translate("MainWindow", "x^y"))
        self.Button8.setText(_translate("MainWindow", "8"))
        self.Button5.setText(_translate("MainWindow", "5"))
        self.Button2.setText(_translate("MainWindow", "2"))
        self.ButtonComma.setText(_translate("MainWindow", ","))
        self.ButtonSqrt.setText(_translate("MainWindow", "√"))
        self.Button9.setText(_translate("MainWindow", "9"))
        self.Button6.setText(_translate("MainWindow", "6"))
        self.Button3.setText(_translate("MainWindow", "3"))
        self.ButtonMinus.setText(_translate("MainWindow", "-"))
        self.ButtonFactorial.setText(_translate("MainWindow", "!"))
        self.ButtonPercent.setText(_translate("MainWindow", "%"))
        self.ButtonDivision.setText(_translate("MainWindow", "÷"))
        self.ButtonMultiplication.setText(_translate("MainWindow", "x"))
        self.ButtonPlus.setText(_translate("MainWindow", "+"))
        self.ButtonBackspace.setText(_translate("MainWindow", "<"))
        self.ButtonClear.setText(_translate("MainWindow", "C"))
        self.ButtonPlusMinus.setText(_translate("MainWindow", "+/-"))
        self.ButtonEquals.setText(_translate("MainWindow", "="))
