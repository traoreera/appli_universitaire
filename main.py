import tkinter as tk
import customtkinter
from PIL import ImageTk, Image
from ico.ico_loads import *

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
        Root.chortcut(self)
        self.root.mainloop()
        

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
            self.profile.configure(width=200,height=180,)
            self.profile.place_configure(x=0,y=10)
            self.resize_bt.place(x=999,y=180)
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
            self.profile.configure(width=200,height=180)
            self.profile.place_configure(x=0,y=10)
            self.resize_bt.place(x=700,y=180)
    
    def Bodyframe(self):
        self.bodyframe = customtkinter.CTkFrame(self.root, width=760,height=660,corner_radius=15,bg_color='transparent')
        self.bodyframe.place(x=310,y=30)
        
    
    def SegmentButon(self):
        
        self.segmentbt =customtkinter.CTkSegmentedButton(master=self.root,
                                                        values=["Command","Configuration","Fichier","Serveur","Aide","Version","quit",
                                                                "mise a jour","reload","login","logout",],font=("",14),
                                                        text_color=("blue","white"),command=self.bt_segmented)
        self.segmentbt.place(x=200,y =0)     

        
    def bt_segmented(self,value):
        #print(value)
        if value =="quit":
            try: self.root.quit()
            except: self.root.destroy()
            finally:pass
            

    def HomeFrame(self):
        
        self.homeframe = customtkinter.CTkFrame(master=self.bodyframe,width=760,height=220,corner_radius=15,bg_color='transparent')
        self.homeframe.place(x=0,y=0)
        
        self.profile = customtkinter.CTkFrame(self.homeframe,height=200,corner_radius=15)
        self.profile.place(x=0,y=10)
        
        self.info1= customtkinter.CTkFrame(self.homeframe,height=50,width=250,corner_radius=15)
        self.info1.place(x=220,y=10)
        
        self.info2 = customtkinter.CTkFrame(self.homeframe,width=250,height=120)
        self.info2.place(x=220,y=29)    

        self.info3 = customtkinter.CTkFrame(self.homeframe,height=30,width=250,corner_radius=15)
        self.info3.place(x=220,y=159)

        self.description_label = customtkinter.CTkLabel(self.info2,text="description",width=250,height=120)
        self.description_label.place(x=0,y=0)
        
        self.profile_ico =customtkinter.CTkLabel(self.profile,text="profile image")
        self.profile_ico.place(x=50,y=100)
        
        self.username =customtkinter.CTkLabel(self.info3,text="username",)
        self.username.place(x=0,y=0)
        
        self.resize_bt = customtkinter.CTkButton(self.homeframe,corner_radius=100,text=">>",height=45,width=40)
        self.resize_bt.place(x=700,y=180)
        

    
    def __button(self):  

        self.bt_chat = customtkinter.CTkButton(self.Menu_frame,text="Chat",font=("",12),width=40,height=45)
        self.bt_chat.place(x=0,y=50)
        ToolTip(self.bt_chat,"for chat and an person on your univercity")

        ### bt setup all menu bt in one 
        self.bt_electrobinder = customtkinter.CTkButton(self.Menu_frame,text="",font=("",12),width=40,height=45)
        self.bt_electrobinder.place(x=0,y=100)
        ToolTip(self.bt_electrobinder,"to find electronicien in your univercity")
        ### bt setup all menu bt in one 
        
        self.bt_itech = customtkinter.CTkButton(self.Menu_frame,text="",font=("",12),width=40,height=45)
        self.bt_itech.place(x=0,y=150)
        ToolTip(self.bt_itech,"known invention on your univercity")
        
        ### bt setup all menu bt in one 
        
        self.setting_bt = customtkinter.CTkButton(self.Menu_frame,text="",font=("",12),width=40,height=45)
        self.setting_bt.place(x=0,y=200)
        ToolTip(self.setting_bt,"to configure tour interface with\nJSON file")
        ### bt setup all menu bt in one 
        
        self.bt_utm = customtkinter.CTkButton(self.Menu_frame,text="",font=("",12),width=40,height=45)
        self.bt_utm.place(x=0,y=250)
        ToolTip(self.bt_utm,text="buton UTM")
        ### bt setup all menu bt in one 
        
        self.bt_quit = customtkinter.CTkButton(self.Menu_frame,text="",font=("",12),width=40,height=45)
        self.bt_quit.place(x=0,y=300)
        ToolTip(self.bt_quit,"to exit ")

        self.bt_maj = customtkinter.CTkButton(self.Menu_frame,text="",font=("",12),width=40,height=45,)
        self.bt_maj.place(x=0,y=350)
        ToolTip(self.bt_maj,"to verifed update for logitiel")
        ### bt setup all menu bt in one
        
        self.label_version = customtkinter.CTkLabel(master=self.Menu_frame,text="verion 1.0.1 dernier MAJ",font=("",10),text_color="#fff")
        self.label_ico = customtkinter.CTkLabel(master=self.Menu_frame,text="",image= self.alerte_ico) # type: ignore     
        self.label_version.place(x=40,y=640)
        self.label_ico.place(x=10,y=630)
        
    def LoopTrap(self): pass
    

        
        
    def chortcut(self):   
        def hello(self):
            quit()
        """"""
        self.root.bind("<Control-h>",hello)



class ToolTip:
    def __init__(self, widget, text):
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
        tw.attributes('-alpha',0.8)
        tw.attributes('-topmost',1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                      background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hide_tip(self, event):
        tw = self.tipwindow
        if tw:
            tw.destroy()









if __name__ == "__main__":
    Root()