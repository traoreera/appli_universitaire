import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine

if __name__ == "__main__":
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # Charger le fichier QML
    engine.load("test.qml")

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())
