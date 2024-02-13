
from tkinter import *

import tkinter as tk

root = tk.Tk()

root.title("Static Text Example")

static_text = tk.Label(root, text="This is a static text control.")

static_text.pack()

root.mainloop()