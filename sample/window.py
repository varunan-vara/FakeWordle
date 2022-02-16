from tkinter import Tk, Label, Button
from wordle import returncheckOnline, returngottenOnline, defaultwords
import time

class tkintergui:
    def __init__(self,window):
        self.window = window
        window.title("Fake Wordle")
        window.geometry("800x800")
        window.configure(bg="black")
        self.labels = {}
    def addlabel(self, labelname:str, labeltext: str, size:int, fontfamily : str = "Courier", padx:int = 0, pady:int = 0):
        self.labels[labelname] = Label(self.window, text=labeltext, font = (fontfamily, size))
        self.labels[labelname].pack(padx = padx, pady = pady)

def loadinglabel (guiname, root):
    guiname.addlabel("Loading Label", "Loading Online set of 5 - Letter Words...", 20, pady=(100,0))
    timeoutcounter = 0
    window.update_idletasks()

    while not returncheckOnline or timeoutcounter > 10:
        time.sleep(1)
        timeoutcounter += 1
    guiname.labels["Loading Label"].after(1000, guiname.labels["Loading Label"].destroy())
    window.update_idletasks()
    if returngottenOnline():
        guiname.addlabel("Loading Label", "Loaded Online Repo of Words", 20, pady=(100,0))
        window.update_idletasks()
    else:
        guiname.addlabel("Loading Label", "Couldn't find Online Repo", 20, pady=(100,0))
        guiname.addlabel("Test", defaultwords[0], 20, pady=(10,0))
        window.update_idletasks()


window = Tk()
gui = tkintergui(window)
gui.addlabel("title","Fake Wordle", 50, pady = 100)



# mainloop
window.mainloop()
loadinglabel(gui, window)
