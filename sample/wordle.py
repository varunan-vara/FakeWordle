import requests
import random
import os

with open(os.getcwd() + "\\sample\\five-letters.txt") as f: 
    listy = []
    lines = f.readlines()
    for line in lines:
        listy.append(line.strip("\n"))


defaultwords = listy
checkOnline = False
gottenOnline = True

def returncheckOnline ():
    return checkOnline

def returngottenOnline ():
    return gottenOnline

try:
    defaultwords_url = "https://raw.githubusercontent.com/varunan-vara/FakeWordle/main/sample/five-letters.txt"
    defaultwords_unlisted : str = requests.get(defaultwords_url).text
    defaultwords = defaultwords_unlisted.splitlines()
    checkonline = True
except (requests.ConnectionError, requests.Timeout) as exception:
    gottenOnline = False
    checkonline = True


def randword (listy : list = defaultwords, num:int = None):
    if num == None:
        num = random.randint(0,(len(defaultwords) - 1))
    return listy[num]

