import sys
from PyQt5.QtWidgets import QDialog, QApplication
from Start.Starter import Ui_starter_window


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_starter_window()
        self.ui.setupUi(self)
        Ui_starter_window()
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
