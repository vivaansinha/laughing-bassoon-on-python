from tkinter import *
from tkinter import ttk

import keyboard
while True:
    if keyboard.is_pressed('return'):
        print('Goodbye')
        window = Tk()

        notebook = ttk.Notebook(window)

        tab = ttk.Frame(notebook)

        tab2 = ttk.Frame(notebook)

        tab3 = ttk.Frame(notebook)

        notebook.pack()

        window.mainloop()