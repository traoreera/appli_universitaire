
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("300x300")

img = Image.open("\ico\1.jpg",'r')
img = img.resize((100, 100), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

btn = Button(root, image=img, borderwidth=0, highlightthickness=0)
btn.pack(pady=50)

root.mainloop()
