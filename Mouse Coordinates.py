import pyautogui
from tkinter import *
from tkinter.ttk import *

root = Tk()
var = StringVar()
var.set('0, 0')

l = Label(root, textvariable = var)
l.config(font=("Helvetica", 12))
l.pack()

while True:
        newVar = pyautogui.position()
        helperVar = "X: " + str(newVar[0]+8) + "  Y: " + str(newVar[1]+8)
        var.set(helperVar)
        root.update()
        
root.mainloop()
