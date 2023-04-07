import tkinter
import tkinter.messagebox as messagebox
import customtkinter
from PIL import ImageTk, Image
from ico.ico_loads import *
import os
import datetime
from command.commands import partail_inject_ui_ttk as partial, dropper
from ico.txt.Readme import *
import ctypes

class Root:

    def __init__(self):

        super(Root, self).__init__()
        #Root.Root_register(self)

        Ico_Loads.ico_loads(self) # type: ignore
        #README.ReadFile(self) # type: ignore
        Root.Configuration(self)
        Root._Font_Setup(self)
        Root._frameMenu(self)
        Root.Bodyframe(self)
        Root.HomeFrame(self)
        Root.SegmentButon(self)
        Root.__button(self)
        self.root.mainloop()
        
    def Root_register(self):

        try:
            admin_modes = os.geteuid() == 0 # type: ignore
        except AttributeError:
            admin_modes = ctypes.windll.shell32.IsUserAnAdmin()

        if not admin_modes:
            print("no admin mods")
            messagebox.showwarning(
                title="admin", message="veuiller execute le logitiel en temp qu'administrateur du system")
            quit()

        else:
            pass

    def _Font_Setup(self):
        try:
            img1 = ImageTk.PhotoImage(Image.open("ico/pattern.png").resize((1070, 690), Image.LANCZOS))
            l1 = customtkinter.CTkLabel(master=self.root, text="", image=img1) # type: ignore
            l1.pack()
            

        except Exception: pass
        
    def Configuration(self):
        # Modes: system (default), light, dark
        customtkinter.set_appearance_mode("dark")
        # Themes: blue (default), dark-blue, green
        customtkinter.set_default_color_theme("green")
        self.root = customtkinter.CTk()  # creating cutstom tkinter window
        self.root.title("")
        #self.root.configure(bg_color='transparent')
        self.root.minsize(height=660, width=1070)
        self.root.resizable(False, False)


    def _frameMenu(self):
        self.Menu_frame = customtkinter.CTkFrame(master=self.root,width=300,height=660,corner_radius=20)
        self.Menu_frame.place(x=0,y=30)
        #configuration button 
        self.shadow_bt_menu = customtkinter.CTkButton(master=self.Menu_frame,image=self.arrow_left,text="",bg_color="transparent",corner_radius=None,width=20,command=lambda: self.Resize_Menu()) # type: ignore
        self.shadow_bt_menu.place(x=250,y=5)
        
    def Resize_Menu(self):
        if self.Menu_frame._current_width ==300:
            self.Menu_frame.configure(width=40)
            self.shadow_bt_menu.configure(image=self.arrow_right) # type: ignore
            self.shadow_bt_menu.place(x=0,y=5)
            #
            # body main frame reconfigurate#
            self.bodyframe.configure(width=1020)
            self.bodyframe.place_configure(x=50,y=30)
            self.homeframe.configure(width=1020,height=200)
            self.homeframe.place(x=0,y=0)
            self.ProfileFrame.place(x=380,y=110)
        else :
            self.Menu_frame.configure(width=300)
            self.shadow_bt_menu.configure(image=self.arrow_left) # type: ignore
            self.shadow_bt_menu.place(x=250,y=5)
            #
            # body main frame reconfigurate#
            self.bodyframe.configure(width=760)
            self.bodyframe.place_configure(x=310,y=30)
            self.homeframe.configure(width=760,height=200)
            self.homeframe.place(x=0,y=0)
            self.ProfileFrame.place(x=300,y=110)
    
    def Bodyframe(self):
        self.bodyframe = customtkinter.CTkFrame(self.root, width=760,height=660,corner_radius=15,bg_color='transparent')
        self.bodyframe.place(x=310,y=30)
        
    
    def SegmentButon(self):
        
        self.segmentbt =customtkinter.CTkSegmentedButton(master=self.root,
                                                        values=["Command","Configuration","Fichier","Serveur","Aide","Version","quit",
                                                                "mise a jour","reload","login","logout",],font=("",14),
                                                        text_color=("blue","white"))
        self.segmentbt.place(x=200,y =0)     


    def HomeFrame(self):
        
        self.homeframe = customtkinter.CTkFrame(master=self.bodyframe,width=760,height=220,corner_radius=15,bg_color='transparent')
        self.homeframe.place(x=0,y=0)
        self.ProfileFrame = customtkinter.CTkFrame(master=self.homeframe,corner_radius=100,bg_color='transparent')

        self.ProfileFrame.place(x=300,y=110)
    
    def __button(self):  

        self.bt_chat = customtkinter.CTkButton(self.Menu_frame,text="",font=("",12),width=40,height=45)
        self.bt_chat.place(x=0,y=50)

        ### bt setup all menu bt in one 
        self.bt_electrobinder = customtkinter.CTkButton(self.Menu_frame,text="",font=("",12),width=40,height=45)
        self.bt_electrobinder.place(x=0,y=100)
        ### bt setup all menu bt in one 
        
        self.bt_itech = customtkinter.CTkButton(self.Menu_frame,text="",font=("",12),width=40,height=45)
        self.bt_itech.place(x=0,y=150)
        ### bt setup all menu bt in one 
        
        self.setting_bt = customtkinter.CTkButton(self.Menu_frame,text="",font=("",12),width=40,height=45)
        self.setting_bt.place(x=0,y=200)
        ### bt setup all menu bt in one 
        
        self.bt_utm = customtkinter.CTkButton(self.Menu_frame,text="",font=("",12),width=40,height=45)
        self.bt_utm.place(x=0,y=250)
        ### bt setup all menu bt in one 
        
        self.bt_quit = customtkinter.CTkButton(self.Menu_frame,text="",font=("",12),width=40,height=45)
        self.bt_quit.place(x=0,y=300)

        self.bt_maj = customtkinter.CTkButton(self.Menu_frame,text="",font=("",12),width=40,height=45,)
        self.bt_maj.place(x=0,y=350)
        ### bt setup all menu bt in one
        
        self.label_version = customtkinter.CTkLabel(master=self.Menu_frame,text="verion 1.0.1 dernier MAJ",font=("",10),text_color="#fff")
        self.label_ico = customtkinter.CTkLabel(master=self.Menu_frame,text="",image= self.alerte_ico) # type: ignore     
        self.label_version.place(x=40,y=640)
        self.label_ico.place(x=10,y=630)
        
    def LoopTrap(self):
        
        result = datetime.datetime()
        heure = result.hour
        minute = result.minute
if __name__ == "__main__":
    Root()