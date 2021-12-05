import sys
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem
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


def except_hook(cls, exception, traceback):  # показ ошибок
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())