import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine
class __Login__:
    
    def __init__(self) :
        
        self.__Run_Login()
        
        super(__Login__,self)
    
    def __Run_Login(self):
        if __name__ == "__main__":
            app = QApplication(sys.argv)
            engine = QQmlApplicationEngine()

            # Charger le fichier QML
            engine.load("test.qml")

            if not engine.rootObjects():
                sys.exit(-1)

            sys.exit(app.exec_())


__Login__()