import time
import sys
clear = "\n" * 100

def kill():
    sys.exit()
def cls():
    print(clear)
def sleep(t):
    time.sleep(t)

calculate = True
calculated = False
operator = ""
fnumber = ""
snumber = ""
op = ""
tf = False
ts = False
to = False
start = False
ready = False

cls()
print("Python Practices: Misc.")
print("Misc.: Calculator")
print("VERSION v0.1 (VERY UNSTABLE)")
sleep(5)

while True:
    while calculate == True:
        if calculated == True:
            operator = ""
            fnumber = ""
            snumber = ""
            tf = False
            ts = False
            to = False
        cls()
        print("CALCULATOR")
        print("--------------------------------------")
        print("FIRST NUMBER: " + fnumber)
        print("SECOND NUMBER: " + snumber)
        print("OPERATOR: " + op)
        print("--------------------------------------")

        if tf == False:
            fnumber = input("FIRST: ")
            tf = True
            cls()
            print("CALCULATOR")
            print("--------------------------------------")
            print("FIRST NUMBER: " + fnumber)
            print("SECOND NUMBER: " + snumber)
            print("OPERATOR: " + op)
            print("--------------------------------------")
        if ts == False:
            snumber = input("SECOND: ")
            ts = True
            cls()
            print("CALCULATOR")
            print("--------------------------------------")
            print("FIRST NUMBER: " + fnumber)
            print("SECOND NUMBER: " + snumber)
            print("OPERATOR: " + op)
            print("--------------------------------------")
        if to == False:
            operator = input("OP (*, /, +, -): ")
            to = True
            cls()

        if tf == True:
            if ts == True:
                if to == True:
                    start = True

        if start == True:
            if operator == "*":
                answer = int(fnumber) * int(snumber)
                op = "Multiplication"
                ready = True
            elif operator == "/":
                answer = int(fnumber) / int(snumber)
                op = "Division"
                ready = True
            elif operator == "+":
                answer = int(fnumber) + int(snumber)
                op = "Addition"
                ready = True
            elif operator == "-":
                answer = int(fnumber) - int(snumber)
                op = "Subtraction"
                ready = True
            else:
                cls()
                print("OPERATOR INVALID")
                to = False
                start = False
                operator = ""
                sleep(2)
            if ready == True:
                cls()
                print("CALCULATOR")
                print("--------------------------------------")
                print("FIRST NUMBER: " + fnumber)
                print("SECOND NUMBER: " + snumber)
                print("OPERATOR: " + op)
                print("--------------------------------------")
                print("ANSWER: " + str(answer))
                calculated = True
                break
    if ready == True:
        if calculated == True:
            print("///////////////////////////////////////////////////")
            feset = input("Calculate again? (Y/N)")
            if feset.islower() == False:
                reset = feset.lower()
            elif feset.islower() == True:
                reset = feset
            if reset == "y":
                operator = ""
                fnumber = ""
                snumber = ""
                op = ""
                tf = False
                ts = False
                to = False
                start = False
                ready = False
                calculate = True
                cls()
            elif reset == "n":
                cls()
                print("See you next time.")
                sleep(2)
                kill()
            else:
                cls()
                print("Invalid Answer.")
                sleep(2)
                cls()










