
import tkinter as tk

def on_resize(event):
    # get the new window size
    width = event.width
    height = event.height

    # calculate the new dimensions for the widget
    widget_width = int(width * 0.5)
    widget_height = int(height * 0.5)

    # place the widget at the center of the window
    x = int(width / 2 - widget_width / 2)
    y = int(height / 2 - widget_height / 2)

    # configure the widget with the new dimensions and position
    canvas.place(x = x, y = y, width = widget_width, height = widget_height)

root = tk.Tk()
canvas = tk.Canvas(root)

# bind the resize event to on_resize function
root.bind("<Configure>", on_resize)
tk.Label(root,text="hello").pack(padx=0,pady=10)
tk.Label(root,text="hello").pack(padx=0,pady=20)
tk.Label(root,text="hello").pack(padx=0,pady=30)
tk.Label(root,text="hello").pack(padx=0,pady=40)
root.mainloop()