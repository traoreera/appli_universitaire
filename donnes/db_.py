from . import *
import sqlite3 as sql
import os
from tkinter import messagebox
import customtkinter

class Data:

    def __init__(self) -> None:

        super(Data, self).__init__()

    def data_verification(self):
        """
        db connection end verification ...
        """
        try:
            if os.path.exists("donnes\\data.db"):
                connect = sql.connect('donnes\\data.db')
                curseur = connect.cursor()
                print("connected")
                curseur.execute("select * from masters ")
                return 1

            else:
                messagebox.showerror(title='db error', message="base de donnes inexsitant")
                print("not connected")
                return 0

        except Exception as e:
            messagebox.showwarning(title='erreur',message='os error or runtime')
            print(e)
            return 0

    def Requesting(self):
        """

        """
        if Data.data_verification(self)==1:
            connect = sql.connect('donnes\\data.db')
            curseur = connect.cursor()
                    
            curseur.execute
            (
                """CREATE TABLE "master" 
                (
                    "id"	INTEGER,
                    "username"	TEXT UNIQUE,
                    "passwords"	TEXT,
                    "remenber"	INTEGER UNIQUE,
                    PRIMARY KEY("id" AUTOINCREMENT)
                );
                """
            )
            connect.commit()

    def _login_veriffication(self, password, username):

        if Data.data_verification(self) == 1:
            connect = sql.connect('donnes\\data.db')
            curseur = connect.cursor()
            result = curseur.execute('SELECT * FROM masters ')

            for i in result:
                if i[1] == username and i[2] == password:
                    print(i[1] + " : ", i[2])
                    
                    return username
                    
                else:
                    frame = self.frame
                    print("not user on db storage")
                    self.label2=customtkinter.CTkLabel(frame,width=24,height=24,image=self.alerte_ico,text="")
                    self.label2.place(x=270,y=165)
                    self.label=customtkinter.CTkLabel(frame,width=24,height=24,image=self.alerte_ico,text="")
                    self.label.place(x=270,y=110)

        else :
            messagebox.showerror(title="error", message="erreur de connection avec la base de donne")
            try:
                quit()
            except (Warning):pass
            