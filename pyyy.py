from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox, ttk

win = Tk()
win.geometry("300x300")
win.configure(background="black")
notebook = ttk.Notebook(win)
notebook.pack(fill="both", expand=True)
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Tab 1")
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Tab 2")
notebook.pack(fill="both", expand=True)
notebook.pack()
label = ttk.Label(tab1, text="google ")
entry = ttk.Entry(tab1)
entry.pack(side='top')
label.pack(side='top')
label2 = ttk.Label(tab2, text="no internet connection")
label2.pack(side='top')
win.mainloop()