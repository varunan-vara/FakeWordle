import requests
import random
import os

class wordlerepo:
    def __init__(self, checkonline:bool = True):
        print("Setting up list of words")
        with open(os.path.abspath(os.getcwd()) + "\\sample\\five-letters.txt") as f: 
            listy = []
            lines = f.readlines()
            for line in lines:
                listy.append(line.strip("\n"))
        self.wordlelist = listy
        self.online = False
        if checkonline:
            try:
                print("Connecting Online")
                defaultwords_url = "https://raw.githubusercontent.com/varunan-vara/FakeWordle/main/sample/five-letters.txt"
                defaultwords_unlisted : str = requests.get(defaultwords_url).text
                self.wordlelist = defaultwords_unlisted.splitlines()
                self.online = True
            except (requests.ConnectionError, requests.Timeout) as exception:
                print("Failed to get online repo - using local set of words")
    def returnonline (self):
        return self.online
    def randword (self, num:int = None):
        if num == None:
            num = random.randint(0,(len(defaultwords) - 1))
        return self.wordlelist[num]

class game:
    def __init__ (self, correct, checkIfReal = True, readableoutput = False):
        self.correct = correct
        self.tries = 0
        self.attempts = []
        self.won = False
        self.real = checkIfReal
        if readableoutput:
            self.errors = ["Already won game!", "No more attempts allowed!"]
        else:
            self.errors = [3,4]
    def isReal(self, checkword:str, listy:list):
        if self.real:
            if checkword not in listy:
                raise Exception(
                    "Word not found in List - To disable check, add parameter to 'game' init: checkIfReal = False"
                    )
    def comparewords (self, answer, guess):
        # returns 0 if not present in word, 1 if present but in the incorrect position, 2 if present in the correct position
        if len(answer) != len(guess):
            raise Exception("Answer and Guess are not the same length!")
        response = [0] * 5
        for i in range(len(guess)):
            if guess[i] == answer[i]:
                response[i] = 2
            elif guess[i] in answer:
                response[i] = 1
        return response
    def attemptstore (self, attemptword, score):
        result = {"word": attemptword, "score": score}
        self.attempts.append(result)
    def play (self, response:str, totallist:list):
        self.isReal(response,totallist)
        if self.won:
            return self.errors[0]
        if self.tries >= 5:
            return self.errors[1]
        scorelist = self.comparewords(self.correct, response)
        self.attemptstore(response, scorelist)
        if scorelist == [2] *5:
            self.won = True
            return scorelist
        self.tries += 1
        return scorelist