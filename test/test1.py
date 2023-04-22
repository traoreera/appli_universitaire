from tkinter import *

class ListeSelection:
    def __init__(self, master):
        self.listbox = Listbox(master)
        self.listbox.pack()

        self.listbox.insert(1, "Option 1")
        self.listbox.insert(2, "Option 2")
        self.listbox.insert(3, "Option 3")

        self.listbox.bind("<<ListboxSelect>>", self.get_selected)

    def get_selected(self, event):
        selection = event.widget.curselection()
        for i in selection:
            print(event.widget.get(i))

root = Tk()

liste_selection = ListeSelection(root)

root.mainloop()
