import customtkinter
from PIL import Image, ImageTk
import sqlite3
import os
import time


class Ico_Loads():

    def __init__(self):
        super(Ico_Loads, self).__init__()

    def ico_loads(self):
        self.search = customtkinter.CTkImage(dark_image=Image.open(
            "ico\\search.png",).resize((50, 50), Image.ANTIALIAS))
        self.right = customtkinter.CTkImage(dark_image=Image.open(
            "ico\\double_right_64px.png",).resize((50, 50), Image.ANTIALIAS))
        self.left = customtkinter.CTkImage(dark_image=Image.open(
            "ico\\double_left_64px.png",).resize((50, 50), Image.ANTIALIAS))

    def Profile_image(self):
        self.ico1 = customtkinter.CTkImage(
            dark_image=Image.open('ico\\1.jpg'), size=(200, 200))
        self.ico2 = customtkinter.CTkImage(
            dark_image=Image.open('ico\\2.jpg'), size=(200, 200))
        self.ico3 = customtkinter.CTkImage(
            dark_image=Image.open('ico\\3.jpg'), size=(200, 200))
        self.ico4 = customtkinter.CTkImage(
            dark_image=Image.open('ico\\4.jpg'), size=(200, 200))
        self.ico5 = customtkinter.CTkImage(
            dark_image=Image.open('ico\\5.jpg'), size=(200, 200))
        self.ico6 = customtkinter.CTkImage(
            dark_image=Image.open('ico\\6.jpg'), size=(200, 200))
        self.ico7 = customtkinter.CTkImage(
            dark_image=Image.open('ico\\7.jpg'), size=(200, 200))
        self.ico8 = customtkinter.CTkImage(
            dark_image=Image.open('ico\\8.jpg'), size=(200, 200))
        self.ico9 = customtkinter.CTkImage(
            dark_image=Image.open('ico\\9.jpg'), size=(200, 200))
        self.ico10 = customtkinter.CTkImage(
            dark_image=Image.open('ico\\10.jpg'), size=(200, 200))

    def saver(self):

        con = sqlite3.connect('ico.db')
        cur = con.cursor()
        list_inage = [file for file in os.listdir() if file.endswith(
            'jpg') if file.endswith('png')]

        i = 0

        for i in range(len(list_inage)):

            with open(f'{list_inage[i]}', 'rb') as img:
                img = img.read()

            cur.execute("INSERT INTO images (name,image) VALUES(?,?)",
                        (f"{list_inage[i]}", img))
            con.commit()
            print(
                f"image {i} as be saved : name {list_inage[i]} value : value is binary ")
            time.sleep(0.3)


Ico_Loads()
