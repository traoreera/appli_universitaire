import tkinter as tk
root = tk.Tk()
root.geometry("200x200")

# Supprimer la bordure de la fenêtre
root.overrideredirect(True)

# Ajouter un label à la fenêtre
label = tk.Label(root, text="Hello World!", bg="white", fg="black")
label.pack(fill="both", expand=True)

root.mainloop()