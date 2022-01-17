import sys
from PyQt5.QtWidgets import QDialog, QApplication
from Guest_SignUpPage import *


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        Ui_Dialog()
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
