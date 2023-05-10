#!/usr/bin/python
# -*- coding: utf-8 -*-
import customtkinter
import tkinter as tk
from tkinter import * # type: ignore

from ico.ico_loads import Ico_Loads
from donnes import requesting as req


class Windown():
    """
    Main class Content fonction and called fonction :
        Configuration : all main window setup and configuration  
        Menu: Horizontal menu setup
        Menu_resize : auto resizer of menu
        Main_content: incopore Header and Body
        Header: contente profile and more
        Body : second pricipal part of interface
    """

    def __init__(self):
        super(Windown, self).__init__()
        Ico_Loads.ico_loads(self)  # type: ignore
        self.Configuration()
        shortcut(root=self.root)
        self.Menu()
        self.Main_content()
        self.Header()
        self.Body()
        self.root.mainloop()

    def Configuration(self):
        # Modes: system (default), light, dark
        customtkinter.set_appearance_mode("dark")
        # Themes: blue (default), dark-blue, green
        customtkinter.set_default_color_theme("blue")
        self.root = customtkinter.CTk()  # creating cutstom tkinter window
        self.root.title("")
        self.root.geometry("1070x620")
        self.root.minsize(1070, 620)
        self.root.configure(bg_color='transparent')

    def Menu(self):

        root = self.root
        self.menu = customtkinter.CTkFrame(
            root, width=40, height=560, corner_radius=15)  # type: ignore
        self.menu.grid(ipadx=0, ipady=100)
        Buton(widget=self.menu, bt_width=40)
        self.resize = customtkinter.CTkButton(
            self.menu, text="", image=self.right, width=40, height=45, command=self.Menu_resize)  # type: ignore
        self.resize.place(x=0, y=0)
        ToolTip(widget=self.resize,text="resize menu")

    def Menu_resize(self):

        if self.menu._current_width == 40:
            self.menu.configure(width=300)
            self.resize.configure(image=self.left)  # type: ignore
            self.resize.place(x=260, y=0)
            self.main_content.place(x=310, y=0)

        else:
            self.menu.configure(width=40)
            self.resize.configure(image=self.right)  # type: ignore
            self.resize.place(x=0, y=0)
            self.main_content.place(x=50, y=0)

    def Main_content(self):

        self.main_content = customtkinter.CTkFrame(
            self.root, width=2000, height=1000, corner_radius=15)
        self.main_content.place(x=40, y=0)

    def Header(self):
        frame = self.main_content
        self.header = customtkinter.CTkFrame(frame, width=2000, height=180)
        self.header.place(x=0, y=0)
        Header_(Widget=self.header)

    def Body(self):
        frame = self.main_content
        self.body = customtkinter.CTkFrame(frame, width=2000, height=1000)
        self.body.place(x=0, y=190)
        Body(width=800, Widget=self.body, height=500)


class Buton:
    """Configuration des boutton du menu
            widget ---> elle point vers le widget dont vous voullez l'affiche
    """

    def __init__(self, widget, bt_width):
        self.Menu_frame = widget
        self.bt_width = bt_width
        super().__init__()
        self.button()

    def button(self):

        self.bt_chat = customtkinter.CTkButton(
            self.Menu_frame, text="", font=("", 12), width=self.bt_width, height=45)
        self.bt_chat.place(x=0, y=50)
        ToolTip(self.bt_chat, "for chat and an person on your univercity")

        # bt setup all menu bt in one
        self.bt_electrobinder = customtkinter.CTkButton(
            self.Menu_frame, text="", font=("", 12), width=self.bt_width, height=45)
        self.bt_electrobinder.place(x=0, y=100)
        ToolTip(self.bt_electrobinder,
                "to find electronicien in your univercity")
        # bt setup all menu bt in one

        self.bt_itech = customtkinter.CTkButton(
            self.Menu_frame, text="", font=("", 12), width=self.bt_width, height=45)
        self.bt_itech.place(x=0, y=150)
        ToolTip(self.bt_itech, "Suport techique du logitiel")

        # bt setup all menu bt in one

        self.setting_bt = customtkinter.CTkButton(
            self.Menu_frame, text="", font=("", 12), width=self.bt_width, height=45)
        self.setting_bt.place(x=0, y=200)
        ToolTip(self.setting_bt, "to configure tour interface with\nJSON file")
        # bt setup all menu bt in one

        self.bt_utm = customtkinter.CTkButton(
            self.Menu_frame, text="", font=("", 12), width=self.bt_width, height=45)
        self.bt_utm.place(x=0, y=250)
        ToolTip(self.bt_utm, text="buton UTM")
        # bt setup all menu bt in one

        self.pdf = customtkinter.CTkButton(
            self.Menu_frame, text="", font=("", 12), width=self.bt_width, height=45,)
        self.pdf.place(x=0, y=300)
        ToolTip(self.pdf, "liste des cours ")

        self.bt_maj = customtkinter.CTkButton(
            self.Menu_frame, text="", font=("", 12), width=self.bt_width, height=45,)
        self.bt_maj.place(x=0, y=350)
        ToolTip(self.bt_maj, "to verifed update for logitiel")
        # bt setup all menu bt in one

        self.label_version = customtkinter.CTkLabel(
            master=self.Menu_frame, text="verion 1.0.1 dernier MAJ", font=("", 10), text_color="#fff")
        
        self.label_version.place(x=0, y=700)
        


class ToolTip:
    """
    ToolTip est une class objet prement deux valeur en entre
    soit widget et text permentant de faire des infos bulle sur le
    widget que notre curseur poite dessus
        widget -->type: tkinter button ,any
        text ---->type: str 
    """

    def __init__(self, widget, text, **argv):
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.show_tip)
        self.widget.bind("<Leave>", self.hide_tip)

    def show_tip(self, event):
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # Créer une fenêtre de survol
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.attributes('-alpha', 0.8)
        tw.attributes('-topmost', 1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(tw, text=self.text, justify=tk.LEFT, background="#ffffe0",
                         relief=tk.SOLID, borderwidth=1, font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hide_tip(self, event):
        tw = self.tipwindow
        if tw:
            tw.destroy()


class Header_:
    """
    Setup frame contente search bar profile info and another info from user profile
    it resume of user compte it's taked 1 params : widget : type :frame 
    """

    def __init__(self, Widget):
        self.frame = Widget
        self._SearchBar()
        self.SelectionFilierLevel()
        super().__init__()

    def _SearchBar(self):

        def user_search(self):

            request = search_try.get()
            if request == "":
                print("valeur vide")
            else:

                req.Request(request=request, niveau_etude=1,)
                
        frame = self.frame
        _search_bar_frame = customtkinter.CTkFrame(
            frame, width=550, height=30, corner_radius=15)
        _search_bar_frame.place(x=350, y=10)
        search_try = customtkinter.CTkEntry(
            _search_bar_frame, placeholder_text="rechercher un livre", height=30, width=500)
        Ico_Loads.ico_loads(self)  # type: ignore
        search_try.place(x=0, y=0)
        ico = customtkinter.CTkLabel(
            _search_bar_frame, text='', image=self.search)  # type: ignore
        ico.place(x=510, y=5)
        search_try.bind("<KeyRelease>", command=user_search)


    def SelectionFilierLevel(self):
        frame = self.frame

        niveau = customtkinter.CTkOptionMenu(frame, corner_radius=10, values=[
                                             'L1', 'L2', 'L3', 'Master1', 'Master2',], width=100)
        niveau.place(x=100, y=10)

        filier = customtkinter.CTkOptionMenu(frame, corner_radius=10, values=[
                                             'rt', 'eii', 'gmp', 'btp', 'mi',], width=100)
        filier.place(x=210, y=10)

    def Preview(self):
        
        frame = self.frame
        

class Body:
    """
        Configuration du corp du logitiel avec la configuration de l'hauteur et la largeur de la boite
        qui doit la contenir mai avec de coordonne  defini de x=0 et y=0

        Argment  
                Widget : boite de pour contenir le body
                Width  : largeur du body
                height : hauteur du body

        type    
                Widget : variable CTk style boite d'enpactation
                width : variable de la largeur de type int
                heigth : variable de la hauteur de type int                  
    """

    def __init__(self, Widget, width, height):
        self.width = width
        self.height = height
        self.frame = Widget
        self.pdf_lst_frame()
        super(Body, self).__init__()
        self.Tab_view()

    def pdf_lst_frame(self):
        """
            Frame pour les pdf avec destruction 
        """
        self.pdf_frame = customtkinter.CTkFrame(
            self.frame, width=2000, height=1000)
        self.pdf_frame.place(x=0, y=0)
    
    
    def Tab_view(self):
        tables = customtkinter.CTkTabview(
            self.pdf_frame, width=self.width, height=self.height)
        tables.place(x=10, y=0)
        cour = tables.add("Cours dispence")
        exo = tables.add("Exercices et corige")
        tp = tables.add("Travaux Pratiques")
        devoir = tables.add("devoir")
        tables.set("devoir")
        
        ListeSelection(master=cour,master1=exo,master2=tp,master3=devoir)



class shortcut:
    """ Class racoucier clavier sur les evenement de la fenetre principal
            Argument :  root 
            Type :  variable CTk
            retournamt :    pas de resultant 
            variable d'erreur e 
            fichier log : shortcut_log.log
            @Auteur : 
    """

    def __init__(self, root):
        super().__init__()
        self.root = root
        self.short()

    def short(self):
        """
            fonction miroir pour le bind ...
        """

        def exit(self):
            """
            fonction chortcut pour quite la fenetre principale pour contole bind --> Ctrl-h --> exit()
                argument : pas d'argument 
                type de valeur : none

            """

            try:
                self.root.quit()
            except Exception as e:
                quit()

        self.root.bind("<Control-e>", exit)
        self.root.bind("<Control",)


class ListeSelection:
    def __init__(self, **master):

        for  _,value in master.items(): 
        
            scroll = customtkinter.CTkScrollbar(value)
            scroll.pack(side='right', fill='y')
            listbox = Listbox(value,yscrollcommand=scroll.set,width=100,
                            font=('Roboto',12),activestyle='none',background='#3d3d3d',fg='#fff')
            for i in range(100):listbox.insert(END,f"kj krjoj oijoidfbk iojofgb oijfoigb oijfogb oijoifg {i}")
            listbox.pack(side='left',fill='both')
            scroll.configure(command=listbox.yview)
            listbox.configure(highlightbackground='#3d3d3d',)
            listbox.bind("<<ListboxSelect>>", self.get_selected)

    def get_selected(self, event):
            selection = event.widget.curselection()
            for i in selection:
                print("votre selection est :",event.widget.get(i))
                choise = event.widget.get(i)
            


     
    


if __name__ == "__main__":
    Windown()
