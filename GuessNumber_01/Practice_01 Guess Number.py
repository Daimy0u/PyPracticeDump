import random
import time
import sys
clear = "\n" * 100

def kill():
    sys.exit()
def cls():
    print(clear)
def sleep(t):
    time.sleep(t)

tries = 0
hol = ""
win = False

cls()
print("Python Practices: Games")
print("Game: Random Guess")
print("----------------------------")
print("VERSION v0.1 (VERY UNSTABLE)")
sleep(5)
cls()
print("SELECT DIFFICULTY:")
print("EASY / HARD")
print("(no capslock please)")
dfselect = input("INPUT: ")

if dfselect == "easy":
    dmode = 1
elif dfselect == "hard":
    dmode = 2
else:
    cls()
    print("ERROR: INVALID INPUT")
    print("Please enter a valid answer with no caps.")
    print("Re-run the .py script.")
    sleep(0.5)
    print("///////////////////////////////////////////")
    print("Process terminating in 2 seconds.")
    sleep(2.5)
    kill()

cls()
sleep(0.5)

if dmode == 1:
    iline = "1-10"
    dline = "easy"
    mline = "EASY"
    rnumber = random.randint(1, 10)
elif dmode == 2:
    iline = "1-100"
    dline = "hard"
    mline = "HARD"
    rnumber = random.randint(1, 100)

print("Very well, you have chosen the " + dline + " difficulty.")
sleep(2)
cls()

while win == False:
    cls()
    print(mline + " - GUESSING NUMBER")
    print("--------------------------------------------------")
    print("Guess between " + iline)
    tries = str(tries)
    print('Tries: ' + tries)
    print(hol)
    print("--------------------------------------------------")
    ig = input("Guess: ")
    ig = int(ig)

    if ig > rnumber:
        hol = "Lower"
        tries = int(tries)
        tries = tries + 1
    elif ig < rnumber:
        hol = "Higher"
        tries = int(tries)
        tries = tries + 1
    elif ig == rnumber:
        hol = "Correct!"
        win = True
        break
cls()
print("--------------------------------------------------")
rnumber = str(rnumber)
print("Correct! The number was " + rnumber + ".")
print("It took you " + tries + " tries to guess the number!")
print("--------------------------------------------------")
kill()










