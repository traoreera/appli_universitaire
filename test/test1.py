
import tkinter as tk

class RoundedLabel(tk.Canvas):
    def __init__(self, parent, text='', bg='white', fg='black', radius=10, **kwargs):
        tk.Canvas.__init__(self, parent, **kwargs)
        self.config(bg=bg, highlightthickness=0)
        self.fg = fg
        self.radius = radius
        self.text = text
        self.redraw()

    def redraw(self):
        self.delete('all')
        width = self.winfo_width()
        height = self.winfo_height()
        r = self.radius
        x1 = width/2 - r
        y1 = height/2 - r
        x2 = width/2 + r
        y2 = height/2 + r
        self.create_oval(x1, y1, x2, y2, fill=self['bg'], outline=self.fg)
        self.create_text(width/2, height/2, text=self.text)

root = tk.Tk()
label = RoundedLabel(root, text='Hello World!', bg='red', fg='white', radius=50)
label.pack(fill='both', expand=True)

root.mainloop()
