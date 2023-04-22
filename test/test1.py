from tkinter import *

def get_selected():
    selection = listbox.curselection()
    for i in selection:
        print(listbox.get(i))

root = Tk()

listbox = Listbox(root)
listbox.pack()

listbox.insert(1, "Option 1")
listbox.insert(2, "Option 2")
listbox.insert(3, "Option 3")

button = Button(root, text="Get Selected", command=get_selected)
button.pack()

root.mainloop()
