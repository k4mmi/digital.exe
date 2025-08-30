import sys
import webbrowser
import tkinter as tk
from tkinter import messagebox

name = "Digitál"

root = tk.Tk()
root.withdraw()

messagebox.showinfo(name, "Ahoj...")

if messagebox.askyesno(name, "Chceš se k nám připojit?"):
    webbrowser.open("https://prihlaska.utb.cz/obor-detail/?obor=2710&global=6620")
else:
    root.destroy()


# If script reach end...
sys.exit(0)