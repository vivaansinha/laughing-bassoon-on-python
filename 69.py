import time
import webbrowser
from tkinter import *
def main():
    for i in range(1,101):
        print()
        time.sleep(0.07)
    print("done")
    webbrowser.open("https://www.windows93.net/")
window = Tk()
butt = Button(window, text="start windows 93 codename 3.41",command=main)
butt.pack()








window.mainloop()