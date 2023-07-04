from rich.console import Console as console 
import sys
import sqlite3 as sq
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from datetime import datetime
import os


class __log:
    
    """
        __log : class permettant de resencier les erreurs du logitiel 
        uniquement dans la base de donnes 
        gestionaire d'erreur en eregistrement des erreur dans un fichier log en fonction des
        heure du jour et du mois o l'erreur a ete releve
        
        information
            auteur: @hunters
            github: @traoreera
            email: traoreera@gmail.com ou traoreera01@gmail.com
            criptage: en cours
            cle de chiffrement: en cours
            type de base de donnes : sqlite offline db connector
        
    """
    maintenant = datetime.now()
    annee = maintenant.year
    mois = maintenant.month
    heure = maintenant.hour
    minute = maintenant.minute
    
    
    def __runner__(self,erreur, directory):
        
        
        if os.path.exists(str(directory)):
            with open (f'{directory}','+a') as file :
                
                if file.writable():
                    
                    
                    
                    file.write(f'\n\ninformation: annee : {self.annee} | mois : {self.mois} | heure :{self.heure} | minute : {self.minute}\nErreur :\n\t{erreur}')
                
                else:
                    pass
        
        else:
            with open(f'{directory}','+a') as file :
                
                if file.writable():
                    
                    file.write("""		Login Log file ui and db error 
					description: log file
						author	   : hunters tech io
						email 	   : traoreera@gmail.com | traoreera01@gmail.com
					
					information:
						les fichier log peut etre edite lie et modifier """)
                    file.write(f'\n\ninformation: annee : {self.annee} | mois : {self.mois} | heure :{self.heure} | minute : {self.minute}\nErreur :\n\t{erreur}')
    
class db__(__log):
    """_summary_

    Args:
        __log (class): classe de gestion d'ereur en stokage ans login.log
        db__(class): verf
    """
    def __init__(self,__DIR__,):
        self.__DIR__ = __DIR__
        super(db__,self).__init__()
        self.runner()
    def runner(self):
        self.verification()    
    
    def verification(self):
        if os.path.exists(self.__DIR__):
            print('db already  exit ')
    
        else: sys.exit(exec())