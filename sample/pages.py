from wordle import wordlerepo, game
from window import tkWindow

class TkWordle:
    def __init__ (self):
        self.ready = False
        self.windows = {}
    def defineWordle (self, gamesess:game):
        self.game = gamesess
    def definerepo (self, repo:wordlerepo):
        self.wordlerepo = repo
    