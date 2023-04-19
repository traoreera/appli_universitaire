# /usr/bin/python3

##########################
import os
import subprocess
import platform
from tkinter import  messagebox, filedialog
import threading
import customtkinter
##########################
class dropper():
    def __init__(self, ):
        

        """
            dropper consiste a stoke tous les command powershell 
            pour la maintemance du system d'exploitation windows ainsi 
            que les erreurs grafique on de la console en fichiers log
            en temp que super utilisateur c'est axe majeur sont :
                    > platform
                    > threading
                    > subprocess
                    > tkinter
            les commande powershell son stoke dans des fonction a ussage unique
            cette fonctions son liste et bien armonise pour ne pas plante votre os
            windows 
        """
        super(dropper, self).__init__() # initialisation de la class dropper avec __init__(self)
        
        
    def error_fen(self, error, msg): 
        
        # fonction pour recupere tout les erreur que se soit console ou graphique pour les affichier au user
        # msg pour le message d'erreur et error pour le tittre de l'erreur
        """
            cette fonction me permet de ne pas repete le meme code pour chaque fonction et erreur durant le programme
        """
        
        messagebox.showwarning(f'{error}',f"{msg}")
        
                
    def _UI_error_log(self):
        try :
            
            if os.path.exists : self.file = open("log/error.log", '+r')
            
            else : pass
        
        except (FileExistsError, FileNotFoundError) as e :
            dropper.error_fen(self,error="erreur de fichier log", msg = "erreur durant la lecture ou la recherche\n du fichier error.log veuiller cree un\n"
            "un fichier error.log a la racine du programme cella perdra automatiquement vos donnes log\n ")
            self.file.write(f"\nErreur de fichier log:\n\t{e}\n")
            




    def chkdsk_(self, option):
        """_summary_

        Args:
            option (/r /r /v
                ): option list as /f /r /v for check disk all partition and restore
                            disk
        """
        def _chkdsk():
            try:
                #subprocess.run(f"powershell chkdsk {option}") # command powershell
                print(option)
                pass
            
            except Exception as e :
                dropper.error_fen(self, error='erreur chkdsk', msg='Veuiller voir les fichier log')
                self.file.write(f"\nErreur durant l'execution de chkdsk: \n\t{e}\n")
                        
        thread_ = threading.Thread(target=_chkdsk) # utilisation du module threading a deamon = bool ==> true
        thread_.daemon = True
        thread_.start()
        

    def _verif_h(self):
        def _verif():
            try:
                #subprocess.run("powershell DISM /Online /Cleanup-image  /CheckHealth")
                pass
            
            except Exception as e:
                
                
                dropper.error_fen(self,error="erreur dism health",msg="veuillez consule les fichiers logs")
                self.file.write(f"\nErreur de dism check : \n\t{e}\n")
                
        thread_ = threading.Thread(target= _verif, )
        thread_.daemon = True
        thread_.start()

    def _scan_h(self):

        def _scan():
            try:
                
                #subprocess.run("powershell DISM /Online /Cleanup-image /ScanHealth")
                pass

            except Exception as e:
                
                dropper.error_fen(self, error="erreur de scan",msg="euiller consulter les fichier logs")
                self.file.write(f"\nErreur de dism scan: \n\t{e}\n")
                   
        thread_ = threading.Thread(target= _scan)
        thread_.daemon = True
        thread_.start()           
               
    def restore_h(self):
        
        def _restore():
            try:
                #subprocess.run("powershell DISM /Online /Cleanup-image /RestoreHealth")
                pass
            
            except Exception as e :
                dropper.error_fen(self,error="Erreur de restoration",msg="veuiller consulte les fichiers log")
                self.file.write(f"Erreur de restoration : \n\t{e}\n")
                                 
        thread_ = threading.Thread(target= _restore, )
        thread_.daemon = True
        thread_.start()
            
    def Open_files(self):
        def _open_f():
            try:
                    
                filetype = (
                    ('text file', '*.log')
                    ,)     
                file = filedialog.askopenfilename(title='open file',initialdir='/', filetypes=filetype)
                
                #
                #    la suite du cote pour l'affichier dans la fennetre comme log
                #
                    
            except Exception as e :
                dropper.error_fen(self,error="erreur d'ouverture", msg="veuiller consule les fichiers logs")

        thrad_ = threading.Thread(target=_open_f)
        thrad_.daemon = True
        thrad_.start()
        
    def boot_repaire(self):
        
        def Boot_R():
            
            try:
        
                subprocess.run("powershell bootrec /fixmbr")
               
                
            except Exception as e :
                
                dropper.error_fen(self,error="erreur du boot repaire", msg="veuiller consule les fichiers logs")
                
        thrad_ = threading.Thread(target=Boot_R)
        thrad_.daemon = True
        thrad_.start()
                

        


class partail_inject_ui_ttk():
    
    def __init__(self):
        
        super(partail_inject_ui_ttk, self).__init__()
        partail_inject_ui_ttk.os_info(self)

    def os_info(self):
        
        arch = platform.architecture()
        os_ = platform.system()
        machine = platform.machine()
        nodes = platform.node()
        version = platform.version()
        processor = platform.processor()
        relase = platform.release()
        uname = platform.uname()
        
        return (arch,os_,machine,nodes,version,processor)

partail_inject_ui_ttk()