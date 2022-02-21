from window import tkWindow
from wordle import wordlerepo, game
import window
from tkinter import StringVar

def main ():
    repo = wordlerepo()
    def firstpage (isOnline : bool) :
        startpage = window.tkWindow(800,800)
        startpage.addLabel("title","Fake Wordle", 50, pady = 100)
        startpage.addLabel("Loading Label", "", 20, pady=(100,0))
        if isOnline:
            startpage.editLabel("Loading Label", "Online")
        else:
            startpage.editLabel("Loading Label", "Failed to Connect Online")
        startpage.addButton("Start", "Start Game", 25, "kill", pady=(30, 0))
        print("Mainloop")
        startpage.mainloop()
        return True
    def guessrunner (guess: str, gamesess: game, window: tkWindow, var1: str, var2: str, var3: str, var4: str, var5: str):
        result = gamesess.play(guess)
        if not (gamesess.won):
            window.editLabel(var1, guess[0])
            window.editLabel(var2, guess[1])
            window.editLabel(var3, guess[2])
            window.editLabel(var4, guess[3])
            window.editLabel(var5, guess[4])
    if firstpage(repo.returnonline()):
        print("Initiating Game")
        session = game(repo.randword(), repo.wordlelist)
        mainpage = window.tkWindow(340,800)
        mainpage.createGrid("Mainpage-Maingrid")
        mainpage.createGrid("WordDisplay", "Mainpage-Maingrid")
        for i in range(25):
            mainpage.addLabeltoGrid("WordDisplay", "wordle-" + str(i), " ", 10, i%5, i//5, bgcolour="white", colour="black", padx= 10, pady = 10, width=5, height=5)
        mainpage.addEntrytoGrid("Mainpage-Maingrid", "WordleAttempt", "aroma", 20, 0, 1, bgcolour="white", colour="black")
        mainpage.addButtontoGrid(
            "Mainpage-Maingrid", 
            "WordleSubmit", 
            "Submit Guess", 
            20, 0, 2, 
            guessrunner(mainpage.texts["WordleAttempt_entry"], session, mainpage, "wordle-0", "wordle-1", "worlde-2", "wordle-3", "worlde-4"), 
            padx=(10,0))
        # mainpage.editLabel("wordle-0", "L")
        # mainpage.editButtonColour("wordle-0", "yellow")
        mainpage.mainloop()

main()