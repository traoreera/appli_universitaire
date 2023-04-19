#
import sqlite3 as sq
import os
import tkinter
from tkinter import messagebox
import customtkinter

class new_cont():
    
    def ___init__(self):
        
        super(new_cont,self).__init__()
        
    
    def connect(self,Root_key,data_name):
        
        if Root_key == "": pass # mot de passe stoke dans le server 
        
        connect = sq.connect(f"{data_name}")
        curs = connect.cursor()
        
        return curs

class Log_in(new_cont):
    
    def __init__(self) :
        super(Log_in,self).__init__()
        
    def getting_info(self):
        """
                le root key est genere et stoke sur le server
        """
        key_ = ""
        data = ""
        result = self.connect(key_,data)
        
        return result
        
        #returning result
    
    def requesting(self,usermane,password):
        
        curseur  = self.getting_info()
        
        result = curseur.execute("#fichier sql a execute ...")
        
        if usermane != result and password != result:
            messagebox.showwarning(title="Login",message=":ot de passe ou nom d'utilisateur invalide")
                        
            
        
        
        
        
        

            
            
        