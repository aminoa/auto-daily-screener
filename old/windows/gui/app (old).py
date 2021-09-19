from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
import sys

def window():
    Form, Window = uic.loadUiType('settings.ui')
    app = QApplication(sys.argv)
    window = Window()
    form = Form()
    form.setupUi(window)
    window.show()
    app.exec()

window()

# Form, Window = uic.loadUiType('settings.ui')
# app = QApplication([])
# window = Window()
# form = Form()
# form.setupUi(window)
# window.show()
# app.exec()