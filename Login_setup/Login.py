from . import *


class ScriptRunner(QObject):
    finished = pyqtSignal()
    
    @pyqtSlot(str)
    def getusername(self, username):
        self.username = username
        self.finished.emit()

    @pyqtSlot(str)
    def getpassword(self, password):
        username = self.username
        # verifier si la chaine de caractere entre est vide ou pas avant d'envoye a la methode verification
        self.verification(username=username, password=password)
        self.finished.emit()

    def verification(self, username, password):
        try:
            result = db__(__DIR__="Login_setup//login.db")
            connect = sq.connect("Login_setup//login.db")
            curseur = connect.cursor()
            results = curseur.execute(
                f"""SELECT * FROM users WHERE name="{username}" AND password="{password}" """)
            # ______________________________________________________
            for i in results:
                continue
            name, passwd = i
            if name != username and passwd != password:
                pass
            else:
                pass
        except Exception as e:
            # gestionneur d'erreur dans __init__.py
            db__.__runner__(self=db__, erreur=e,
                            directory='Login_setup//login.log')
