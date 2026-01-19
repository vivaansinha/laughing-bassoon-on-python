import time
import webbrowser
from tkinter import messagebox

print("welcome to WinDos 11")

while True:
    x=input()
    if x=="quit":
        break
    elif x=="win":
        y = input('press enter to continue..')
        print("downloading")
        time.sleep(1)
        webbrowser.open_new_tab("https://win11.blueedge.me/")
    elif x=="downgrade":
        y = input('press enter to continue..')
        print("downloading")
        time.sleep(1)
        webbrowser.open_new_tab('https://scratch.mit.edu/projects/892918001/fullscreen/')

def define():
    messagebox.showinfo('Message', 'enter password')
    password = input()
    if password == 'Gublu@1917':
        webbrowser.open('https://win11.blueedge.me/')
    else:
        print('wrong password :( reboot WinDos 11')