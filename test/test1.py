
import tkinter as t 

root = t.Tk()
def scrol():
    pass
bost = t.Listbox(root,justify='center')
bost.place(x=0,y=0)
scroll = t.Scrollbar(root)
scroll.place(x=150,y=0)
for i in range(100): bost.insert(i,f"option {i}")
scroll.set(0,99)
scroll.activate()
root.mainloop()