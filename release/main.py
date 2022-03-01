import sys
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem, QLabel
from PyQt5 import uic
from random import randint
import sqlite3


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('main.ui', self)
        self.do_paint = False
        self.table_update()

    def table_update(self):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        result = cur.execute("""SELECT userid FROM coffee""")
        count = 0
        for i in result:
            count += 1
        result = cur.execute("""SELECT * FROM coffee""")
        self.tbl.setRowCount(count)
        count = 0
        for i in result:
            print(i[0])
            for j in range(7):
                new = QTableWidgetItem(str(i[j]))
                self.tbl.setItem(count, j, new)
            count += 1
        self.tbl.resizeRowsToContents()
        con.close()


class New(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.state = 0
        # 1 - new, 2 - change

    def initUI(self):
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.lineEdit.setEnabled(False)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_7.setEnabled(False)
        self.btn3.setEnabled(False)
        self.btn4.setEnabled(False)
        self.btn1.clicked.connect(self.f1)
        self.btn2.clicked.connect(self.f2)
        self.btn3.clicked.connect(self.f3)
        self.btn4.clicked.connect(self.f4)

    def f1(self):
        self.state = 1
        self.lineEdit.setEnabled(True)
        self.btn2.setEnabled(False)
        self.btn4.setEnabled(True)

    def f2(self):
        self.state = 2
        self.lineEdit.setEnabled(True)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_5.setEnabled(True)
        self.lineEdit_6.setEnabled(True)
        self.lineEdit_7.setEnabled(True)
        self.btn3.setEnabled(True)

    def f3(self):
        a1 = self.lineEdit.text()
        a2 = self.lineEdit_2.text()
        a3 = self.lineEdit_3.text()
        a4 = self.lineEdit_4.text()
        a5 = self.lineEdit_5.text()
        a6 = self.lineEdit_6.text()
        a7 = self.lineEdit_7.text()
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        if self.state == 1:
            cur.execute(f"""INSERT INTO coffee (userid,name,fire,status,info,price,v)
                    VALUES('{a1}', '{a2}', '{a3}', '{a4}', '{a5}', '{a6}', '{a7}')""")
        elif self.state == 2:
            cur.execute(f"""DELETE from coffee WHERE userid LIKE '{a1}'""")
            cur.execute(f"""INSERT INTO coffee (userid,name,fire,status,info,price,v)
                                VALUES('{a1}', '{a2}', '{a3}', '{a4}', '{a5}', '{a6}', '{a7}')""")
        con.commit()
        con.close()

    def f4(self):
        self.btn3.setEnabled(True)
        self.lineEdit.setEnabled(True)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_5.setEnabled(True)
        self.lineEdit_6.setEnabled(True)
        self.lineEdit_7.setEnabled(True)


def except_hook(cls, exception, traceback):  # показ ошибок
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    ex2 = New()
    ex2.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
