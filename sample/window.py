from doctest import master
from tkinter import Tk, Label, Button, StringVar, Frame, Entry
from turtle import back

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
        self.window.geometry("{}x{}".format(str(xlen), str(ylen)))
        self.labels = {}
        self.texts = {}
        self.buttons = {}
        self.gridnames = {}
        self.entry = {}
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
        pady:int = 0,
        pack:bool = True
        ):
        self.texts[name] = StringVar()
        self.texts[name].set(labeltext)
        self.labels[name] = Label(
            self.window, 
            textvariable=self.texts[name], 
            font=(fontfamily,size), 
            bg = bgcolour, 
            fg = colour)
        if pack:
            self.labels[name].pack(padx = padx, pady = pady)
        print("Created Label {} with string {}".format(name, labeltext))
    def createGrid(self, gridname: str, parentwindow: str = "window", bg:str = "black"):
        if parentwindow == "window":
            self.gridnames[gridname] = Frame(self.window, background = bg)
        else:
            self.gridnames[gridname] = Frame(self.gridnames[parentwindow], background = bg)
        self.gridnames[gridname].grid(column = 0, row = 0, sticky="NESW")
        self.gridnames[gridname].grid_rowconfigure(0, weight=1)
        self.gridnames[gridname].grid_columnconfigure(0, weight=1)
    def addLabeltoGrid(
        self, 
        gridname:str, 
        name:str, 
        labeltext:str, 
        size:int, 
        colnum:int, 
        rownum: int, 
        width: int,
        height: int,
        fontfamily:str = "Courier", 
        bgcolour = "black",
        colour = "white",
        colspan: int = 1, 
        rowspan: int = 1,
        padx: int = 0,
        pady: int = 0
        ):
        self.texts[name] = StringVar()
        self.texts[name].set(labeltext)
        self.labels[name] = Label(
            self.gridnames[gridname],
            textvariable=self.texts[name], 
            font=(fontfamily,size), 
            bg = bgcolour, 
            fg = colour,
            width=width,
            height=height
        )
        self.labels[name].grid(column = colnum, row=rownum, columnspan = colspan, rowspan = rowspan, padx = padx, pady = pady)
    def addButtontoGrid(
        self, 
        gridname:str, 
        name:str, 
        labeltext:str, 
        size:int, 
        colnum:int, 
        rownum: int, 
        func,
        fontfamily:str = "Courier", 
        bgcolour = "black",
        colour = "white",
        colspan: int = 1, 
        rowspan: int = 1,
        padx: int = 0,
        pady: int = 0):
        if func == "kill":
            def executfunc ():
                self.window.destroy()
        else:
            executfunc = func
        self.texts[name + "button"] = StringVar()
        self.texts[name + "button"].set(labeltext)
        self.buttons[name] = Button(
            self.gridnames[gridname], 
            textvariable= self.texts[name + "button"], 
            font = (fontfamily, size), 
            fg=colour, 
            bg=bgcolour, 
            command=executfunc)
        self.buttons[name].grid(column = colnum, row=rownum, columnspan = colspan, rowspan = rowspan, padx = padx, pady = pady)
    def addEntrytoGrid(
        self, 
        gridname:str, 
        name:str, 
        labeltext:str, 
        size:int, 
        colnum:int, 
        rownum: int, 
        fontfamily:str = "Courier", 
        bgcolour = "black",
        colour = "white",
        colspan: int = 1, 
        rowspan: int = 1,
        padx: int = 0,
        pady: int = 0
        ):
        self.texts[name + "_entry"] = StringVar()
        self.texts[name + "_entry"].set(labeltext)
        self.entry[name] = Entry(
            self.gridnames[gridname],
            textvariable=self.texts[name + "_entry"], 
            font=(fontfamily,size), 
            bg = bgcolour, 
            fg = colour,
        )
        self.entry[name].grid(column = colnum, row=rownum, columnspan = colspan, rowspan = rowspan, padx = padx, pady = pady)
    def packGrid(self, gridname: str, padx:int = 0, pady:int = 0):
        self.girdnames[gridname].pack(padx = padx, pady = pady)
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
        if func == "kill":
            def executfunc ():
                self.window.destroy()
        else:
            executfunc = func
        self.buttons[name] = Button(
            self.window, 
            textvariable= self.texts[name + "button"], 
            font = (fontfamily, size), 
            fg=colour, 
            bg=bgcolour, 
            command=executfunc)
        self.buttons[name].pack(padx = padx, pady = pady)
    def editButtonColour (self, name:str, newcolour:str):
        self.labels[name].config(bg=newcolour)
    def killLoop (self):
        self.window.destroy()
        print("Killed Loop")
    def listOfVars (self):
        returnlist = [item for item in self.texts]
        return str(returnlist)