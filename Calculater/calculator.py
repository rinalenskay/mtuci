import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QMessageBox


class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()

        self.vbox = QVBoxLayout(self)
        self.hbox_input = QHBoxLayout()
        self.hbox_first = QHBoxLayout()
        self.hbox_second = QHBoxLayout()
        self.hbox_third = QHBoxLayout()
        self.hbox_fourth = QHBoxLayout()
        self.hbox_fifth = QHBoxLayout()
        self.hbox_sixth = QHBoxLayout()

        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_second)
        self.vbox.addLayout(self.hbox_third)
        self.vbox.addLayout(self.hbox_fourth)
        self.vbox.addLayout(self.hbox_sixth)

        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)

        self.b_7 = QPushButton("7", self)
        self.hbox_first.addWidget(self.b_7)

        self.b_8 = QPushButton("8", self)
        self.hbox_first.addWidget(self.b_8)

        self.b_9 = QPushButton("9", self)
        self.hbox_first.addWidget(self.b_9)

        self.b_divide = QPushButton("/", self)
        self.hbox_first.addWidget(self.b_divide)

        self.b_4 = QPushButton("4", self)
        self.hbox_second.addWidget(self.b_4)

        self.b_5 = QPushButton("5", self)
        self.hbox_second.addWidget(self.b_5)

        self.b_6 = QPushButton("6", self)
        self.hbox_second.addWidget(self.b_6)

        self.b_multiply = QPushButton("*", self)
        self.hbox_second.addWidget(self.b_multiply)

        self.b_1 = QPushButton("1", self)
        self.hbox_third.addWidget(self.b_1)

        self.b_2 = QPushButton("2", self)
        self.hbox_third.addWidget(self.b_2)

        self.b_3 = QPushButton("3", self)
        self.hbox_third.addWidget(self.b_3)

        self.b_minus = QPushButton("-", self)
        self.hbox_third.addWidget(self.b_minus)

        self.b_0 = QPushButton("0", self)
        self.hbox_fourth.addWidget(self.b_0)

        self.b_float = QPushButton(".", self)
        self.hbox_fourth.addWidget(self.b_float)

        self.b_del = QPushButton("⌫", self)
        self.hbox_fourth.addWidget(self.b_del)

        self.b_plus = QPushButton("+", self)
        self.hbox_fourth.addWidget(self.b_plus)

        self.b_result = QPushButton("=", self)
        self.hbox_sixth.addWidget(self.b_result)

        self.b_7.clicked.connect(lambda: self._button("7"))
        self.b_8.clicked.connect(lambda: self._button("8"))
        self.b_9.clicked.connect(lambda: self._button("9"))
        self.b_divide.clicked.connect(lambda: self._operation("/"))
        self.b_4.clicked.connect(lambda: self._button("4"))
        self.b_5.clicked.connect(lambda: self._button("5"))
        self.b_6.clicked.connect(lambda: self._button("6"))
        self.b_multiply.clicked.connect(lambda: self._operation("*"))
        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))
        self.b_minus.clicked.connect(lambda: self._operation("-"))
        self.b_0.clicked.connect(lambda: self._button("0"))
        self.b_float.clicked.connect(lambda: self._button("."))
        self.b_del.clicked.connect(self._del)
        self.b_plus.clicked.connect(lambda: self._operation("+"))
        self.b_result.clicked.connect(self._result)

    def _button(self, param):
        line = self.input.text()
        self.input.setText(line + param)

    def _operation(self, op):
        repeak = 0

        if repeak == 0:
            self.num_1 = float(self.input.text())
            repeak += 1

        self.op = op
        self.input.setText("")

    def _result(self):

        self.num_2 = float(self.input.text())

        flag_result = False
        result = 0

        if self.op == "/":
            if self.num_2 == 0:
                QMessageBox.about(self, "Предупреждение", "Не получится поделить на Ноль")
            else:
                flag_result = True
                result = self.num_1 / self.num_2

        if self.op == "*":
            flag_result = True
            result = self.num_1 * self.num_2

        if self.op == "-":
            flag_result = True
            result = self.num_1 - self.num_2

        if self.op == "+":
            flag_result = True
            result = self.num_1 + self.num_2

        str_result = str(result)

        if flag_result:
            if len(str_result.split('.')[1]) == 1 and str_result.split('.')[1] == '0':
                self.input.setText(str(int(result)))
            else:
                self.input.setText(str(float(result)))

    def _del(self):
        line = self.input.text()
        if len(line) > 0:
            self.input.setText(line.rstrip(line[-1]))


if __name__ == '__main__':

    app = QApplication(sys.argv)

    win = Calculator()
    win.show()

    sys.exit(app.exec())
