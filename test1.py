from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

app = QApplication([])
ui_file = 'untitled.ui'
window = uic.loadUi(ui_file)
window.show()
app.exec_()