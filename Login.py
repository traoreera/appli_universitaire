import tkinter
import customtkinter
from PIL import ImageTk,Image
from ico.ico_loads import *
from donnes.db_ import Data
from ico.ico_loads import Ico_Loads

class Login():
    
    def __init__(self) :
        super(Login,self)
        customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
        Login.Configuration(self)
        Login.FontSetup(self)
        Ico_Loads.ico_loads(self)
        Login.FrameConf(self)
        Login.Principal(self)
        Login.__Butoon(self)
        self.app.mainloop()
        

    def Configuration(self):
        self.app = customtkinter.CTk()  #creating cutstom tkinter window
        self.app.geometry("600x440")
        self.app.title('Login')

    def FontSetup(self):
        img1=ImageTk.PhotoImage(Image.open("ico/pattern.png"))
        self.l1=customtkinter.CTkLabel(master=self.app,image=img1)
        self.l1.pack()

    #creating custom frame
    def FrameConf(self):
        self.frame=customtkinter.CTkFrame(master=self.l1, width=320, height=360, corner_radius=15)
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    
    def db_logverif(self):
        frame = self.frame
        
        result = Data._login_veriffication(self,username=self.entry1.get(),password=self.entry2.get())
        
        if result == self.entry1.get():
           self.app.destroy()
            
            
                        
    def Principal(self):
        frame = self.frame
        
        l2=customtkinter.CTkLabel(master=frame, text="Log into your Account",font=('Century Gothic',20))
        l2.place(x=50, y=45)

        self.entry1=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Username')
        self.entry1.place(x=50, y=110)
        

        
        self.entry2=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
        self.entry2.place(x=50, y=165)
        


        l3=customtkinter.CTkLabel(master=frame, text="Forget password?",font=('Century Gothic',12))
        l3.place(x=155,y=195)

    #Create custom button
    def __Butoon(self):
        frame = self.frame
        
        button1 = customtkinter.CTkButton(master=frame, width=220, text="Login", corner_radius=6,command= lambda:self.db_logverif())
        button1.place(x=50, y=240)