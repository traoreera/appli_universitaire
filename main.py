import sys
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine
import Login_setup.Login as login
from Login_setup.Login import db__


class Login_Interface:

    def __init__(self):
        self.Interface()
        super(Login_Interface, self).__init__()

    def Interface(self):
        try:
            self.app = QApplication(sys.argv)
            engine = QQmlApplicationEngine()
            context = engine.rootContext()
            scriptRunner = login.ScriptRunner()
            context.setContextProperty("scriptRunner", scriptRunner)
            engine.load("interfaces.qml")
            sys.exit(self.app.exec_())
        except Exception as e:
            db__.__runner__(self=db__, erreur=e,
                            directory='Login_setup//login.log')
            sys.exit()
        
    def stop_Interface(self):
        try:
            sys.exit(self.app.exec_())
            newAcount()
        except Exception as e :
            print(e)
            
class newAcount():
    
    def __init__(self):
        
        super(newAcount,self).__init__()
        self.N_Interface()


        
    def N_Interface():
            
        print('running ...')
        
        
if __name__ == "__main__":

    Login_Interface()
