import sys
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine



app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.load("test.qml")
sys.exit(app.exec_())
