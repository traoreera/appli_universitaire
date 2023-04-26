import customtkinter
from PIL import ImageTk, Image
import tkinter as tk


class Windown():

    def __init__(self):
        super(Windown, self).__init__()
        self.Configuration()
        self.Menu()
        self.Main_content()
        self.Header()
        self.Body()
        self.root.mainloop()

    def Configuration(self):
        # Modes: system (default), light, dark
        customtkinter.set_appearance_mode("dark")
        # Themes: blue (default), dark-blue, green
        customtkinter.set_default_color_theme("dark-blue")
        self.root = customtkinter.CTk()  # creating cutstom tkinter window
        self.root.title("")
        self.root.geometry("1070x620")
        self.root.configure(bg_color='transparent')

    def Menu(self):

        root = self.root
        self.menu = customtkinter.CTkFrame(
            root, width=40, height=560, corner_radius=15)  # type: ignore
        self.menu.grid(ipadx=0, ipady=100)
        Buton(widget=self.menu)
        self.resize = customtkinter.CTkButton(
            self.menu, text="", width=40, height=45, command=self.Menu_resize)
        self.resize.place(x=0, y=0)

    def Menu_resize(self):

        if self.menu._current_width == 40:
            self.menu.configure(width=300)
            self.resize.place(x=260, y=0)
            self.main_content.place(x=310, y=0)

        else:
            self.menu.configure(width=40)
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


class Buton: 
    """Configuration des boutton du menu
            widget ---> elle point vers le widget dont vous voullez l'affiche
    """
    def __init__(self, widget):
        self.Menu_frame = widget
        super().__init__()
        self.button()

    def button(self):

        self.bt_chat = customtkinter.CTkButton(
            self.Menu_frame, text="Chat", font=("", 12), width=40, height=45)
        self.bt_chat.place(x=0, y=50)
        ToolTip(self.bt_chat, "for chat and an person on your univercity")

        # bt setup all menu bt in one
        self.bt_electrobinder = customtkinter.CTkButton(
            self.Menu_frame, text="", font=("", 12), width=40, height=45)
        self.bt_electrobinder.place(x=0, y=100)
        ToolTip(self.bt_electrobinder,
                "to find electronicien in your univercity")
        # bt setup all menu bt in one

        self.bt_itech = customtkinter.CTkButton(
            self.Menu_frame, text="", font=("", 12), width=40, height=45)
        self.bt_itech.place(x=0, y=150)
        ToolTip(self.bt_itech, "Suport techique du logitiel")

        # bt setup all menu bt in one

        self.setting_bt = customtkinter.CTkButton(
            self.Menu_frame, text="", font=("", 12), width=40, height=45)
        self.setting_bt.place(x=0, y=200)
        ToolTip(self.setting_bt, "to configure tour interface with\nJSON file")
        # bt setup all menu bt in one

        self.bt_utm = customtkinter.CTkButton(
            self.Menu_frame, text="", font=("", 12), width=40, height=45)
        self.bt_utm.place(x=0, y=250)
        ToolTip(self.bt_utm, text="buton UTM")
        # bt setup all menu bt in one

        self.pdf = customtkinter.CTkButton(
            self.Menu_frame, text="", font=("", 12), width=40, height=45,)
        self.pdf.place(x=0, y=300)
        ToolTip(self.pdf, "liste des cours ")

        self.bt_maj = customtkinter.CTkButton(
            self.Menu_frame, text="", font=("", 12), width=40, height=45,)
        self.bt_maj.place(x=0, y=350)
        ToolTip(self.bt_maj, "to verifed update for logitiel")
        # bt setup all menu bt in one

        self.label_version = customtkinter.CTkLabel(
            master=self.Menu_frame, text="verion 1.0.1 dernier MAJ", font=("", 10), text_color="#fff")


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

    def __init__(self, Widget):
        self.frame = Widget
        self._SearchBar()
        super().__init__()

    def _SearchBar(self):

        def user_search(self):

            request = search_try.get()
            if request == "":
                print("valeur vide")
            else:
                print(f"select from pdflist where name like ={request}")
        frame = self.frame
        _search_bar_frame = customtkinter.CTkFrame(
            frame, width=600, height=45, corner_radius=15)
        _search_bar_frame.place(x=20, y=10)
        search_try = customtkinter.CTkEntry(
            _search_bar_frame, placeholder_text="rechercher un livre", height=45, width=550)
        search_try.place(x=0, y=0)
        ico = customtkinter.CTkLabel(_search_bar_frame,text='',)
        search_try.bind("<KeyRelease>", command=user_search)



Windown()
