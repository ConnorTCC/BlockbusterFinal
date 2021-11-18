########LIBRARIES########
import time
import random
import string
import datetime
import sys
import turtle
import os
########LIBRARIES########

# def countdown(timer):
#     while timer > 0:
#         print(timer)
#         timer -= 1
#         time.sleep(1)
#         print("The walls seem too close in on you, as you fall into a deeper slumber, you wonder if there is anyway out of here at all")
        
# def countdown(t):
#     while t:
#         mins, secs = divmod(t, 60)
#         timeformat = '{:02d}:{:02d}'.format(mins, secs)
#         print(timeformat, end='\r')
#         time.sleep(1)
#         t -= 1
#     print('Goodbye!\n\n\n\n\n')
global attempts
attempts = 3

def start_game():

    def function(): # introduction
        print("Would you like to begin?")
        choice = input ("[Y/N]\n")
        if choice.upper() == "Y":
            function1()
        if choice.upper() == "N":
            print("We need your permission too begin...")
            return function()
        else:
            return function()
        
    def function1(): # character
        name = input("Enter patient ID: ").capitalize()
        print(f"Welcome {name}..")

        
        if name == ("Connor").capitalize():
            print("An interesting name, have we met before?")
            function2()
            time.sleep(2)
        if name == ("Hiral").capitalize():
            print("I knew of a scholar who bore a similar name, no relation I assume?")
            time.sleep(3)
            function2()
        if name == ("Adam").capitalize():
            print("Have you been searching for us all this time?")
            time.sleep(3)
            function2()
        if name == ("Leigh").capitalize():
            print("Welcome back, it has been some time hasnt it?")
            time.sleep(3)
            function2()
        if name == ("Jordan").capitalize():
            print("Back so soon? We hope this game doesnt hurt your brain too much!")
            time.sleep(3)
            function2()
        if name == ("Keira"):
            print("Thanks for all the help along the way, we couldnt have done it without you!")
            time.sleep(3)
            function2()
        else:
            print("Ahhh, a new face?..")
            time.sleep(2)
        
        time.sleep(2)
        function2

        function2()

    def function2(): #Plot stuff
        print("As you lay, you feel a sense of comfort, as you slip into a deep slumber, you hear something whisper your name")
        time.sleep(3)
        print("                       ")
        print("!!!!!!!!!!!!!! SIRENS !!!!!!!!!!!!!!")
        print("Deafening sirens From a bygone era jolt you awake, as you come to your senses you realise your not in Kansas anymore.")
        time.sleep(3)
        print("The room was decaying, rotten drapes adorn the window, the air is cold, you see your every breath infront of you. Just what is this place?..")
        time.sleep(4)
        print("The door you entered through only hours ago, is gone. In its place a giant steel door, it seemed as out as place as you.")
        print("Its opening barred with 3 by 2 steel pipes, a cool wind breezed through, and you daren't gaze through the opening. 4 strangly coloured locks adorn it..")
        time.sleep(3)
        print("As your mind races you scan across the room, the intercoms control panel hung precariously below the speaker, can it be turned off?")
        time.sleep(5)
        function3()
        print("                                      ")
    


    def function3():
        print("                        ")
        print("|          |            |            |")
        print("|     2    |      7     |      6     |     ==?   ")
        print("|          |            |            |")
        print("----------------------------------------")
        print("|          |            |            |")
        print("|     9    |      5     |     1      |     ==?  ")
        print("|          |            |            |")
        print("----------------------------------------")
        print("|          |            |            |")
        print("|     4    |      3     |      8     |     ==?")
        print("|          |            |            |")
        print("                        ")
        print("                        ")
        print("A small keypad hangs below the intercom..")
        print("Its letters are old and worn, you can just make out most symbols, but the override code is missing, can you solve this riddle? Or be consumed by your madness")   #sort this input as 2 digits in boxes can lead too confusion

        function4
        function4()

    
        
    def function4(): #riddle
        global attempts
        attempts == 3
        pin = 15
 ####################################################       
        pin = input("Enter 2 Digit Terminal Override command:  \n")
        if pin == "15":
            print("[Intecom Override] Initializing...")
            time.sleep(3)
            print("The sirens wind down as you finally begin to let your mind wander, what is happening too me?..")
            print("The control terminal shifts and warps into a small opening with a small key of somekind.")
            print("\033[1;35;40m Magenta Key Acquired \033[0m")
            time.sleep(3)
            function5
            function5()
        else:
            print("Unauthorized access")
        attempts -= 1
        if attempts <= 0:
                print("*HINT* The sum of all parts must be equal. All sides must add up too the missing code")
                
        function4()

            
    def function5(): #ending
        print("You look around the room you entered just a few hours ago, it seems twisted now, different.")
        time.sleep(2)
        print("The walls are damp, you hear strange noises and hear something calling your name...")
        time.sleep(3)
        print("What more is too come of this nightmare?...")
        exit()
  
    function()
start_game()



# def function4(): #! overall function
#     global attempts
#     attempts = 0
# #######################################################
#     def pin_func(): #! function 1 - takes a pin input and checks if it is correct
#         pin = input("Please enter your pin...\n")
#         if pin == "15":
#             print("OVERRIDE ACCEPTED")
#             balance_func() #! correct - next function
#         else:
#             print("UNAUTHORIZED ACCESS!")
#             global attempts
#             attempts += 1
#             if attempts  >= 3:
#                 print("*HINT* The sum of all parts must")
#             else:
#                 pin_func() #! incorrect - return to start of function

#The door you entered through has changed, instead there sits a huge door that seems to beat in time with your heart. Adorned with 4 small locks, there must be some keys around here somewhere?
