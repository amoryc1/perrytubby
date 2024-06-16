# Math game running from console. Edit code to run off a screen for the Teletubbie Perty Perry

import random
import subprocess
import sys

add = True # Is addition going to be present in the questions?
sub = True # Is subtraction going to be present in the questions?
div = True # Is division going to be present in the questions?
mul = True # Is multiplication going to be present in the questions?
deb = False # Debug mode

difficulty = 1 # Gets higher if >90% was achieved in the previous set of questions. Makes them slightly harder.

ingame = False
loaded = True # Is loop running cause infinite loops are not cool

while loaded:
    if not ingame:
        inp = input("\nRun command ( '?' for help ): ")
        
        if inp == "?": # View help
            print(" BASIC COMMANDS")
            print("     start           -- Start the game.")
            print("     ?               -- Show this menu.")
            print("     ui              -- Play a version of this with UI elements")
            print(" GAME SETTINGS")
            print(f"     -add            -- Allow addition to be in the question pool ({add}).")
            print(f"     -sub            -- Allow subtraction to be in the question pool ({sub}).")
            print(f"     -div            -- Allow division to be in the question pool ({div}).")
            print(f"     -mul            -- Allow multiplication to be in the question pool ({mul}).")
            print(f"     -deb            -- Debug mode({deb}).")
            print("\n")
            
            print(" ")
        
        # Settings
        # Change equation settings
        if inp == "-add" or inp == "-sub" or inp == "-div" or inp == "-mul" or inp == "-deb":
            exec(f"{inp[1:]} = not {inp[1:]}")
            exec(f"newVar = {inp[1:]}")
            print(f"{inp} allowed: {newVar}")
        
        
        if inp == "start":
            confirm = input("If everything is set up, type Y: ")
            if confirm == "Y":
                if add or sub or mul or div:
                    ingame = True
                else:
                    print("     ERROR : At least one symbol needs to be enabled. Type '?' for more information")
        
        
        if inp == "ui":
            exec(open("MathGameUI.py").read()) # uii
    else:
        # Game logics
        symbolTable = [] # Make a list of all symbols allowed
        if add:
            symbolTable.append("+")
        if sub:
            symbolTable.append("-")
        if div:
            symbolTable.append("/")
        if mul:
            symbolTable.append("*")
            
        symbol = random.choice(symbolTable)
        
        num1 = 0
        num2 = 0
        # Pick a random number depending on symbol and add 1 to prevent 0 from appearing. This is made for 2 year olds it has to be simple :)
        if symbol == "+" or symbol == "-":
            num1 = random.randrange(99)
            num2 = random.randrange(99)
            if symbol == "-" and num2 > num1: # Prevent negative numbers
                num1, num2 = num2, num1
        elif symbol == "*":
            num1 = random.randrange(9)
            num2 = random.randrange(9)
        elif symbol == "/":
            num1 = random.randrange(19)
            num2 = random.randrange(19)
            if num2 > num1: # Prevent smaller numbers
                num1, num2 = num2, num1
        num1 += 1
        num2 += 1
        print(f"{num1} {symbol} {num2}")
        exec(f"answer = {num1}{symbol}{num2}")
        if deb: # debug mode
            print(f"answer:{round(answer, 1)}       symbolTable:{symbolTable}")
        resp = input(f"Your answer truncated to and intiger? (Make it a number with NO letters or whitespace): ")

        if float(resp) == float(round(answer, 1)):
            print("           - Yayyy")
        else:
            threats = ["I'm going to find you and hunt you.", "Kill me now.", "All that's going to be left are skeletons... when they're found."] 
            print("           - " + random.choice(threats))