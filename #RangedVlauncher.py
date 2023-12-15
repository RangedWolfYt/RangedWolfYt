#RangedVlauncher

from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
from random import *
import os
from tkinter import *
import time




def Run():
    print("You Ran Gooberio")
    time.sleep(1)
    print("it did nothing cause it doesnt exist yet (:")
    time.sleep(20)
    exit()
    
    
def Run2():
    os.remove("C:\\Users\\range\\Desktop\\Vlauncher-Test-File")

def Run3():
    print("This Does Not Exist Yet")
    time.sleep(2)
    exit()

window = Tk()
window.title("RangedVLauncher-Beta-Private")





button = Button(text='Run Gooberio',
                command=Run)
button.pack()


button2 = Button(text='Run Malscript',
                 command=Run2)

button2.pack()

button3 = Button(text='J-Mal',
                 command=Run3)

button3.pack()







window.mainloop()




