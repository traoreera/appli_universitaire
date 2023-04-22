import customtkinter
from PIL import Image

class Ico_Loads():
    
    
    def ico_loads(self):
        self.alerte_ico = customtkinter.CTkImage(Image.open("ico\\alerte_octo.png").resize((40,40), Image.ANTIALIAS))
        self.patern_ico = customtkinter.CTkImage(Image.open("ico\\pattern.png").resize((20, 20), Image.ANTIALIAS))
        self.arrow_right = customtkinter.CTkImage(Image.open("ico\\arrow-right.png").resize((20, 20), Image.ANTIALIAS))
        self.arrow_left = customtkinter.CTkImage(Image.open("ico\\arrow-left.png").resize((20, 20), Image.ANTIALIAS))

    def setting(self):
        pass
    
    def __Downloads(self):
        pass
    