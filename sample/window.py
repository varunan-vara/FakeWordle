from tkinter import Tk, Label, Button, StringVar

class tkWindow:
    def __init__ (
        self, 
        xlen:int, 
        ylen:int, 
        bgvar="black"
        ):
        window = Tk()
        self.window = window
        self.window.configure(bg=bgvar)
        self.window.geometry("{}.{}".format(str(xlen), str(ylen)))
        self.labels = {}
        self.texts = {}
        self.buttons = {}
        print("Tkwindow created")
    def mainloop (self):
        print("Began mainloop")
        self.window.mainloop()
    def addLabel(
        self, 
        name:str, 
        labeltext:str, 
        size:int, 
        fontfamily:str = "Courier", 
        bgcolour = "black",
        colour = "white",
        padx:int = 0, 
        pady:int = 0
        ):
        self.texts[name] = StringVar()
        self.texts[name].set(labeltext)
        self.labels[name] = Label(
            self.window, 
            textvariable=self.texts[name], 
            font=(fontfamily,size), 
            bg = bgcolour, 
            fg = colour)
        self.labels[name].pack(padx = padx, pady = pady)
        print("Created Label {} with string {}".format(name, labeltext))
    def returnLabelList (self):
        return self.labels
    def editLabel(self, name:str, text:str):
        self.texts[name].set(text)
        print("Edited Text {}".format(name))
    def deleteLabel(self, name:str):
        self.labels[name].destroy()
        print("Delted Label {}".format(name))
    def addButton(
        self, 
        name:str, 
        buttontext:str, 
        size:int, 
        func,
        fontfamily:str = "Courier", 
        colour:str = "black", 
        bgcolour:str = "white", 
        padx:int = 0, 
        pady:int = 0
        ):
        self.texts[name + "button"] = StringVar()
        self.texts[name + "button"].set(buttontext)
        self.buttons[name] = Button(
            self.window, 
            textvariable= self.texts[name + "button"], 
            font = (fontfamily, size), 
            fg=colour, 
            bg=bgcolour, 
            command=func)
        self.buttons[name].pack(padx = padx, pady = pady)
    def killLoop (self):
        self.window.destroy()
        print("Killed Loop")
    def listOfVars (self):
        return str(self.texts)



startpage = tkWindow()
startpage.addLabel("title","Fake Wordle", 50, pady = 100)
startpage.addLabel("Loading Label", "", 20, pady=(100,0))
if (returnonline()):
    startpage.editLabel("Loading Label", "Online")
else:
    startpage.editLabel("Loading Label", "Failed to Connect Online")
startpage.addButton("Start", "Start Game", 25, killLogin, pady=(30, 0))
startpage.mainloop()