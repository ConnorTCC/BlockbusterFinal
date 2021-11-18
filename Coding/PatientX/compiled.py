###############Libraries####################################################    
import random
import sys
import time
import os
###############CODE#########################################################
def patientx_func():
    def slowprint(s):
        for c in s + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(1./50)
############################################################################
    def intro_func():
        slowprint("\n\n\n\n\n\033[1;34;40m                                                           Welcome to Team 5's:")
        time.sleep(2)
        os.system("cls")
        print("\n\n\n\033[1;31;40m                                                                                                                          ___            ___ ")
        print("\033[1;31;40m                                                                                                                          \  \          /  / ")
        print("\033[1;31;40m                                                                                                                           \  \        /  /  ")
        print("\033[1;31;40m                        _______          __        ______________     __     __________     __     __     ______________    \  \      /  /   ")          
        print("\033[1;31;40m                       |   __  \        /  \      |_____    _____|   |  |   |   _______|   |  \   |  |   |_____    _____|    \  \    /  /    ")
        print("\033[1;31;40m                       |  |  |  \      /    \           |  |         |  |   |  |           |   \  |  |         |  |           \  \__/  /     ")
        print("\033[1;31;40m                       |  |  |  |     /  /\  \          |  |         |  |   |  |____       |    \ |  |         |  |            \      /      ")
        print("\033[1;31;40m                       |  |__|  /    /  /__\  \         |  |         |  |   |   ____|      |  |\ \|  |         |  |            /  __  \      ")
        print("\033[1;31;40m                       |   ____/    /  ______  \        |  |         |  |   |  |           |  | \    |         |  |           /  /  \  \     ")
        print("\033[1;31;40m                       |  |        /  /      \  \       |  |         |  |   |  |_______    |  |  \   |         |  |          /  /    \  \    ")
        print("\033[1;31;40m                       |__|       /__/        \__\      |__|         |__|   |__________|   |__|   \__|         |__|         /  /      \  \   ")
        print("\033[1;31;40m                                                                                                                           /  /        \  \  ")
        print("\033[1;31;40m                                                                                                                          /__/          \__\ \033[0;37;40m\n\n\n")
        time.sleep(3)        
        os.system("cls")

############################################################################
        task1_func()
############################################################################
    def task1_func():
        global attempts
        attempts = 3
        def function(): # introduction
            slowprint("\033[1;33;40mWould you like to begin?\033[0;37;40m")
            choice = input ("[Y/N]\n\n")
            if choice.upper() == "Y":
                function1()
            if choice.upper() == "N":
                slowprint("\n\033[1;31;40mWe need your permission too begin...\033[0;37;40m")
                function()
            else:
                function()
        
        def function1(): # character
            name = input("\n\033[1;33;40mEnter patient ID: \033[0;37;40m").capitalize()
            slowprint(f"\nWelcome {name}..\n")
                
            if name == ("Connor").capitalize():
                slowprint("An interesting name, have we met before?")
                function2()
                time.sleep(2)
            if name == ("Hiral").capitalize():
                slowprint("I knew of a scholar who bore a similar name, no relation I assume?")
                time.sleep(3)
                function2()
            if name == ("Adam").capitalize():
                slowprint("Have you been searching for us all this time?")
                time.sleep(3)
                function2()
            if name == ("Leigh").capitalize():
                slowprint("Welcome back, it has been some time hasnt it?")
                time.sleep(3)
                function2()
            if name == ("Jordan").capitalize():
                slowprint("Back so soon? We hope this game doesnt hurt your brain too much!")
                time.sleep(3)
                function2()
            if name == ("Keira"):
                slowprint("Thanks for all the help along the way, we couldnt have done it without you!")
                time.sleep(3)
                function2()
            else:
                slowprint("Ahhh, a new face?..")
                time.sleep(2)
                
            time.sleep(2)
            os.system("cls")
            function2()
        def function2(): #Plot stuff
            slowprint("\nAs you lay, you feel a sense of comfort, as you slip into a deep slumber, you hear something whisper your name.")
            time.sleep(3)
            print("                       ")
            print("\033[1;31;40m\n\n                                                          !!!!!!!!!!!!!! SIRENS !!!!!!!!!!!!!!\n\n\033[0;37;40m")
            time.sleep(1)
            slowprint("\nDeafening sirens From a bygone era jolt you awake, as you come to your senses you realise your not in Kansas anymore.")
            time.sleep(1)
            slowprint("\nYou sit up and realise you were lying in bed. As you examine your surroundings you realise this must be a hospital room... and you are alone.\n")
            time.sleep(1)
            slowprint("The room is decaying, rotten drapes adorn the window, the air is cold, you see your every breath infront of you. Just what is this place..?")
            time.sleep(1)
            slowprint("\nThe door you entered through only hours ago, is gone. In its place a giant steel door, it seemed as out as place as you.")
            time.sleep(1)
            slowprint("\nIts opening barred with 3 by 2 steel pipes, a cool wind breezed through, and you daren't gaze through the opening. 4 strangly coloured locks adorn it...\n")
            time.sleep(1)
            slowprint("As your mind races you scan across the room, the intercoms control panel hung precariously below the speaker, can it be turned off?\n\n\n")
            time.sleep(1)
            function3()
            print("                                      ")
            
        def function3():
            print("\033[1;36;40m--------------------------------------")
            print("|          |            |            |")
            print("|     2    |      7     |      6     |     ==?   ")
            print("|          |            |            |")
            print("--------------------------------------")
            print("|          |            |            |")
            print("|     9    |      5     |      1     |     ==?  ")
            print("|          |            |            |")
            print("--------------------------------------")
            print("|          |            |            |")
            print("|     4    |      3     |      8     |     ==?")
            print("|          |            |            |")
            print("--------------------------------------\033[0;37;40m")
            print("                        ")
            time.sleep(2)           
            slowprint("A small keypad hangs below the intercom...")
            slowprint("\nIts letters are old and worn, you can just make out most symbols, but the override code is missing, can you solve this riddle? Or be consumed by your madness.")   #sort this input as 2 digits in boxes can lead too confusion
            function4
            function4()
            
        def function4(): #riddle
            global attempts
            attempts == 3
            pin = "15"       
            pin = input("\n\033[1;33;40mEnter 2 Digit Terminal Override command:  \033[0;37;40m\n")
            if pin == "15":
                time.sleep(1)
                os.system("cls")                
                slowprint("\033[1;31;40m[Intercom Override] Initializing...\033[0;37;40m")
                time.sleep(3)
                slowprint("\nThe sirens wind down as you finally begin to let your mind wander, what is happening too me..?\n")
                slowprint("The control terminal shifts and warps into a small opening with a small key of somekind.")
                slowprint("\n\033[1;35;40m                                                   Magenta Key Acquired \033[0m")

                print("\n\n\033[1;35;40m                                                                ")
                print("                                          8 8 8 8                     ,ooo.")
                print("                                          8a8 8a8                    oP   ?b  ")
                print("                                         d888a888zzzzzzzzzzzzzzzzzzzz8     8b")
                print("                                            `""^""'                      ?o___oP'\033[0;37;40m")
                print("                                      """)

                time.sleep(3)
                function5()
            else:
                slowprint("\033[1;31;40mUnauthorized Access\033[0;37;40m")
                attempts -= 1
                if attempts <= 0:
                    slowprint("\n\033[1;31;40m*HINT*\033[0;37;40m The sum of all parts must be equal. All sides must add up too the missing code")
                function4()            
                    
        def function5(): #ending
            slowprint("\nYou look around the room you entered just a few hours ago, it seems twisted now, different.")
            time.sleep(2)
            slowprint("\nThe walls are damp, you hear strange noises and hear something calling your name...")
            time.sleep(3)
            slowprint("\nWhat more is too come of this nightmare..?")
            time.sleep(3)
            os.system("cls")
############################################################################              
            task2_func()
############################################################################
        function()

    def task2_func():
        
        slowprint("\n\nA deafening sound what more awaits?...A riddle, maybe two?")
        time.sleep(2)
        slowprint("\nHmm… not quite the answer you were hoping for?")
        time.sleep(2)
        slowprint("\nQuestions, questions... It's not you who needs answers here, it's me. You answer my riddles and you won't \033[1;31;40mDIE\033[0;37;40m. So, shall we begin?\n\n")
        time.sleep(3)

        question_1 = [
            "\033[1;33;40m What belongs to you, but others will use it?\033[0;37;40m \n\n\n 1. Your pain? 2. Your name?", #Riddle1
            "\033[1;33;40m What is broken when it's not held?\033[0;37;40m \n\n\n 1. Promise? 2. Heart?", #Riddle2
            "\033[1;33;40m What question can you never answer yes to?\033[0;37;40m \n\n\n 1. Are you deaf? 2. Are you dead? " #Riddle3
            ]

        def ask_question():

            question = random.choice(question_1)
            slowprint(question)
            answer = input("")
            
            if question == question_1[0] and answer == "2":
                slowprint("\nThat is merely a taste of what is to come. You will regret trying to outsmart me.")
            elif question == question_1[1] and answer == "1":
                slowprint("\nThat is merely a taste of what is to come. You will regret trying to outsmart me.")
            elif question == question_1[2] and answer == "2":
                slowprint("\nThat is merely a taste of what is to come. You will regret trying to outsmart me.")
            else:
                time.sleep(1)
                slowprint("\n\033[1;31;40mYou tried. I'll give you that...\n\033[0;37;40m")
                ask_question()

        ask_question()

        slowprint("\n\n\033[1;32;40m                                                   Green Key Acquired \033[0m")
        print("\n\n\033[1;32;40m                                                                ")
        print("                                          8 8 8 8                     ,ooo.")
        print("                                          8a8 8a8                    oP   ?b  ")
        print("                                         d888a888zzzzzzzzzzzzzzzzzzzz8     8b")
        print("                                            `""^""'                      ?o___oP'\033[0;37;40m")
        print("                                      """)

        slowprint("\nThe key is yours! It looks the same as the one before this!")
        time.sleep(2)
        slowprint("\nWould you look at that, you came this far.. why would you stop?")
        time.sleep(4)
        os.system("cls")
############################################################################
        task3_func()
############################################################################
    def task3_func():            
        def task3():
            time.sleep(1)
            slowprint("\n\033[1;33;40mAre you ready to play for your sanity?\033[0;37;40m\n")
            choice = input("[Y/N]\n")
            if choice.upper() == "Y":
                anagram1()
            elif choice.upper() == "N":
                task3()
            else:
                task3()

        global attempts
        attempts = 3
                
        def anagram1(): #psychopath
            global attempts          
            s1 = input("\n\033[1;33;40mSolve the following anagram to unlock the next piece of code.\n\n [stahyopcph]\033[0;37;40m\n\n")
            s2 = "psychopath"

            if s1 == s2:
                slowprint("\n\nYou're one step closer to your freedom.\n")
                attempts = 3
                anagram2() 
            else:
                slowprint("\n\033[1;31;40mThis task is not for the faint-hearted. Try again!\033[0;37;40m\n")
                attempts -=1
                if attempts <= 1:
                    slowprint("\n\033[1;31;40m*HINT*\033[0;37;40m p _ _ _ _ _ _ _ _ h\n")
                anagram1()

        def anagram2(): #enigma
            global attempts    
            s3 = input("\033[1;33;40mSolve the following anagram to unlock a piece of code.\n\n [amigen]\n\033[0;37;40m\n")
            s4 = "enigma"

            if s3 == s4:
                slowprint("\nThere's no place like home, is there?\n\n")
                attempts = 3  
                anagram3() 
            else:
                slowprint("\n\n\033[1;31;40mIt's as if you want to stay trapped, try again!\033[0;37;40m\n\n")
                attempts -=1
                if attempts <= 1:
                    slowprint("\n\033[1;31;40m*HINT*\033[0;37;40m e _ _ _ _ a\n")
                anagram2()

        def anagram3(): #sociopath
            global attempts             
            s3 = input("\033[1;33;40mYou must solve the anagram to proceed.\n\n[tosapocih]\n\033[0;37;40m\n")
            s4 = "sociopath"

            if s3 == s4:
                slowprint("\nThat was a CLOSE call!\n")
                slowprint("Your body drops in relief, a sigh leaves your lips as you wait for the doors to unlock.\nThey don't.\nYou stand, and with your every exhale a sense of heightened fear overpowers you. Suddenly, a small, sharp cling releases what you so patiently waited for. You kneel...\n")
                slowprint("\033[1;34;40m                                                   Blue Key Acquired \033[0m\n")
                print("\033[1;34;40m                                                                ")
                print("                                          8 8 8 8                     ,ooo.")
                print("                                          8a8 8a8                    oP   ?b  ")
                print("                                         d888a888zzzzzzzzzzzzzzzzzzzz8     8b")
                print("                                            `""^""'                      ?o___oP'\033[0;37;40m")
                print("                                      ""\n\n")
                slowprint("Don't celebrate just yet, as your celebrations are still premature. You must locate and complete the next task in order to defeat the door. Good luck...")
                time.sleep(3)
                os.system("cls")
############################################################################
                task4_func()
############################################################################
            else:
                slowprint("\n\n\033[1;31;40mDo you even want to be free? Try again!\033[0;37;40m\n")
                attempts -=1
                if attempts <= 1:
                    slowprint("\033[1;31;40m*HINT*\033[0;37;40m s _ _ _ _ _ _ _ h\n")
                    time.sleep(1)
                anagram3()
        task3()
    def task4_func():
     
        global task4attempts
        global question1
        global question2
        global question3
        global question4

        task4attempts = 3
        question1 = [
                    "One of Jack Nicholson's most famous films in which tennants of The Overlook Hotel are told to avoid room 237 is what 'S'? The ________?", 
                    "What 'S' is a film from 2010 starring Leonardo Di'Caprio set in a psychiatric facility in the 1950's? _______ Island.",
                    "What 'S' is the classic Anthony Hopkins film _____ of the Lambs?"
                    ]
        question2 = [
                    "What 'D' is the surname of Donnie who has visions of a mysterious rabbit who tells him the world will end?", 
                    "What 'D' is the surname of the Brad Pitt character of Fight Club: Tyler _____?",
                    "Taxi Driver is a film about a war veteran dealing with post-traumatic stress dissorder. What 'D' is the surname of the actor who player the lead role? Robert ______"
                    ]
        question3 = [
                    "What 'L' is the surname of the actor who played The Joker who tragicly died shortly after filming 'The Dark Knight' in 2008", 
                    "What 'L' is the film starring Benicio del Toro and Johnny Depp as journalists travelling across the Nevada desert under the influence of psychoactive substances:  Fear and ________ in Las Vegas?",
                    "Which 'L' is the surname of the co-lead actress in the film Natural Born Killers alongside Woody Harrelson: Julliette ______?"
                    ]
        question4 = [
                    "John Travolta played a lead role Pulp Fiction; a film full of eccentric and violent psychopaths, but which other 'J' was the surname of the actor who played his partner? ", 
                    "Which 'J' is the lead actor who starred in the 1975 psycholoigcal comedy One Flew Over the Cuckoos Nest: ____ Nicholson",
                    "'Unluckily for you, this one is a little harder! What 'J' is the first name of the actress who played the lead role in the classic film Psycho? (no clues. AND NO GOOGLING! time is running out!!"
                    ]

        slowprint("\nA distant memory flashes into your mind! A view of an auditorium with seats stretching out before you, all facing a huge screen. Suddenly the screen fills with light and shows a view of the Earth from space. From the right side, a single word moves to the centre in large captitals...")
        time.sleep(3)
        print("\n\n")
        print("                              ____ __________  ._______   _________________________  _________   _____   .____         ")
        print("                             |    |   \      \ |   \   \ /   /\_   _____/\______   \/   _____/  /  _  \  |    |       ")
        print("                             |    |   /   |   \|   |\   Y   /  |    __)_  |       _/\_____  \  /  /_\  \ |    |       ")
        print("                             |    |  /    |    \   | \     /   |        \ |    |   \/        \/    |    \|    |___    ")
        print("                             |______/\____|____/___|  \___/   /_________/ |____|___/_________/\____|____/|________|   ")
        time.sleep(2)
        slowprint("\n\nAs quickly as it came, it is gone.....")
        time.sleep(3)
        os.system("cls")
        slowprint("and you realise you are back in the hospital. Was this a clue to what is to come? ")
        slowprint("\nNext to the bed is a cabinet. A clinical white, but clearly old and used. It seems locked, but it is fragile enough to prise off.")
        slowprint("It comes off cleanly in your hand, and inside lies a digital screen connected to a simple keyboard.")
        slowprint("\nThe screen shows 4 red boxes with a letter in each box:\n")
        time.sleep(3)

        print("---------------------------------")
        print("\033[0;30;41m|   S   |   D   |   L   |   J   |\033[0;37;40m")
        print("---------------------------------")

        slowprint("As you press 'Enter', the following text is displayed:")
        time.sleep(5)
        os.system("cls")

        def step1_func(): # question 1
            global question1
            global task4attempts

            if task4attempts == 0:
                slowprint("\033[1;31;40m                                                                       You have failed and gone crazy. Game Over\033[0;37;40m \n")
                exit()
            else:
                selection1 = (random.choice(question1))

                print("\n")        
                slowprint(selection1)
                answer1 = input("\n\033[0;33;40mAnswer?\033[0;37;40m\n\n")
                if selection1 == question1[0]:
                    correct_answer1 = "shining"
                    if answer1.lower() == correct_answer1:
                        slowprint("\n\033[1;32;40m     Correct!\033[0;37;40m\n")
                        slowprint("The screen lights up and the letter 'S' has turned to green. Surely you are on the right path?")
                        print("---------------------------------")
                        print("\033[0;30;41m|\033[0;30;42m   S   \033[0;30;41m|   D   |   L   |   J   |\033[0;37;40m")
                        print("---------------------------------")
                        time.sleep(4)
                        os.system("cls")

                        step2_func()
                    else:
                        slowprint("\n\033[1;31;40m     Incorrect!\n")
                        task4attempts -= 1
                        slowprint(f"You have {task4attempts} attempts remaining...\033[0;37;40m\n")
                        question1.pop(0)
                        time.sleep(3)
                        os.system("cls")
                        step1_func()
                elif selection1 == question1[1]:
                    correct_answer1 = "shutter"
                    if answer1.lower() == correct_answer1:
                        slowprint("\n\033[1;32;40m     Correct!\033[0;37;40m\n")
                        slowprint("The screen lights up and the letter 'S' has turned to green. Surely you are on the right path?")
                        print("---------------------------------")
                        print("\033[0;30;41m|\033[0;30;42m   S   \033[0;30;41m|   D   |   L   |   J   |\033[0;37;40m")
                        print("---------------------------------")
                        time.sleep(4)
                        os.system("cls")
                        step2_func()
                    else:
                        slowprint("\n\033[1;31;40m     Incorrect!\n")
                        task4attempts -= 1
                        slowprint(f"You have {task4attempts} attempts remaining...\033[0;37;40m\n")
                        question1.pop(1)
                        time.sleep(3)
                        os.system("cls")
                        step1_func()
                elif selection1 == question1[2]:
                    correct_answer1 = "silence"
                    if answer1.lower() == correct_answer1:
                        slowprint("\n\033[1;32;40m     Correct!\033[0;37;40m\n")
                        slowprint("The screen lights up and the letter 'S' has turned to green. Surely you are on the right path?")
                        print("---------------------------------")
                        print("\033[0;30;41m|\033[0;30;42m   S   \033[0;30;41m|   D   |   L   |   J   |\033[0;37;40m")
                        print("---------------------------------")
                        time.sleep(4)
                        os.system("cls")                        
                        step2_func()
                    else:
                        slowprint("\n\033[1;31;40m     Incorrect!\n")
                        task4attempts -= 1
                        slowprint(f"You have {task4attempts} attempts remaining...\033[0;37;40m\n")
                        question1.pop(2)
                        time.sleep(3)
                        os.system("cls")
                        step1_func()
                else:
                    step1_func() 
          
        def step2_func(): # question 2
            global question2
            global task4attempts
            if task4attempts == 0:
                print("\033[1;31;40m                                                                       You have failed and gone crazy. Game Over\033[0;37;40m \n")
                exit()
            else:
                selection2 = (random.choice(question2))

                slowprint(selection2)
                answer1 = input("\n\033[0;33;40mAnswer?\033[0;37;40m\n\n")
                if selection2 == question2[0]:
                    correct_answer1 = "darko"
                    if answer1.lower() == correct_answer1:
                        slowprint("\n\033[1;32;40m     Correct!\033[0;37;40m\n")
                        slowprint("The screen lights up again with the letter 'D' has turned to green! This is it! You making progress for sure.")
                        print("---------------------------------")
                        print("\033[0;30;41m|\033[0;30;42m   S   \033[0;30;41m|\033[0;30;42m   D   \033[0;30;41m|   L   |   J   |\033[0;37;40m")
                        print("---------------------------------")
                        time.sleep(4)
                        os.system("cls")                        
                        step3_func()
                    else:
                        slowprint("\n\033[1;31;40m     Incorrect!\n")
                        task4attempts -= 1
                        slowprint(f"You have {task4attempts} attempts remaining...\033[0;37;40m\n")
                        question2.pop(0)
                        time.sleep(3)
                        os.system("cls")
                        step2_func()
                elif selection2 == question2[1]:
                    correct_answer1 = "durden"
                    if answer1.lower() == correct_answer1:
                        slowprint("\n\033[1;32;40m     Correct!\033[0;37;40m\n")
                        slowprint("The screen lights up again with the letter 'D' has turned to green! This is it! You making progress for sure.")
                        print("---------------------------------")
                        print("\033[0;30;41m|\033[0;30;42m   S   \033[0;30;41m|\033[0;30;42m   D   \033[0;30;41m|   L   |   J   |\033[0;37;40m")
                        print("---------------------------------")
                        time.sleep(4)
                        os.system("cls")                        
                        step3_func()
                    else:
                        slowprint("\n\033[1;31;40m     Incorrect!\n")
                        task4attempts -= 1
                        slowprint(f"You have {task4attempts} attempts remaining...\033[0;37;40m\n")
                        question2.pop(1)
                        time.sleep(3)
                        os.system("cls")
                        step2_func()
                elif selection2 == question2[2]:
                    correct_answer1 = "de niro"
                    if answer1.lower() == correct_answer1:
                        slowprint("\n\033[1;32;40m     Correct!\033[0;37;40m\n")
                        slowprint("The screen lights up again with the letter 'D' has turned to green! This is it! You making progress for sure.")
                        print("---------------------------------")
                        print("\033[0;30;41m|\033[0;30;42m   S   \033[0;30;41m|\033[0;30;42m   D   \033[0;30;41m|   L   |   J   |\033[0;37;40m")
                        print("---------------------------------")
                        time.sleep(4)
                        os.system("cls")                        
                        step3_func()
                    else:
                        slowprint("\n\033[1;31;40m     Incorrect!\n")
                        task4attempts -= 1
                        slowprint(f"You have {task4attempts} attempts remaining...\033[0;37;40m\n")
                        question2.pop(2)
                        time.sleep(3)
                        os.system("cls")
                        step2_func()
                else:
                    step3_func()
       
        def step3_func(): # question 3
            global question3
            global task4attempts
            if task4attempts == 0:
                print("\033[1;31;40m                                                                       You have failed and gone crazy. Game Over\033[0;37;40m \n")
                exit()
            else:
                selection3 = (random.choice(question3))
                slowprint(selection3)
                answer1 = input("\n\033[0;33;40mAnswer?\033[0;37;40m\n\n")
                if selection3 == question3[0]:
                    correct_answer1 = "ledger"
                    if answer1.lower() == correct_answer1:
                        slowprint("\n\033[1;32;40m     Correct!\033[0;37;40m\n")
                        slowprint("'L' turns to green. 1 more to go!")
                        print("---------------------------------")
                        print("\033[0;30;41m|\033[0;30;42m   S   \033[0;30;41m|\033[0;30;42m   D   \033[0;30;41m|\033[0;30;42m   L   \033[0;30;41m|   J   |\033[0;37;40m")
                        print("---------------------------------")
                        time.sleep(4)
                        os.system("cls")                        
                        step4_func()
                    else:
                        slowprint("\n\033[1;31;40m     Incorrect!\n")
                        task4attempts -= 1
                        slowprint(f"You have {task4attempts} attempts remaining...\033[0;37;40m\n")
                        question3.pop(0)
                        time.sleep(3)
                        os.system("cls")
                        step3_func()
                elif selection3 == question3[1]:
                    correct_answer1 = "loathing"
                    if answer1.lower() == correct_answer1:
                        slowprint("\n\033[1;32;40m     Correct!\033[0;37;40m\n")
                        slowprint("'L' turns to green. 1 more to go!")
                        print("---------------------------------")
                        print("\033[0;30;41m|\033[0;30;42m   S   \033[0;30;41m|\033[0;30;42m   D   \033[0;30;41m|\033[0;30;42m   L   \033[0;30;41m|   J   |\033[0;37;40m")
                        print("---------------------------------")
                        time.sleep(4)
                        os.system("cls")                        
                        step4_func()
                    else:
                        slowprint("\n\033[1;31;40m     Incorrect!\n")
                        task4attempts -= 1
                        slowprint(f"You have {task4attempts} attempts remaining...\033[0;37;40m\n")
                        question3.pop(1)
                        time.sleep(3)
                        os.system("cls")
                        step3_func()
                elif selection3 == question3[2]:
                    correct_answer1 = "lewis"
                    if answer1.lower() == correct_answer1:
                        slowprint("\n\033[1;32;40m     Correct!\033[0;37;40m\n")
                        slowprint("'L' turns to green. 1 more to go!")
                        print("---------------------------------")
                        print("\033[0;30;41m|\033[0;30;42m   S   \033[0;30;41m|\033[0;30;42m   D   \033[0;30;41m|\033[0;30;42m   L   \033[0;30;41m|   J   |\033[0;37;40m")
                        print("---------------------------------")
                        time.sleep(4)
                        os.system("cls")                        
                        step4_func()
                    else:
                        slowprint("\n\033[1;31;40m     Incorrect!\n")
                        task4attempts -= 1
                        slowprint(f"You have {task4attempts} attempts remaining...\033[0;37;40m\n")
                        question3.pop(2)
                        time.sleep(3)
                        os.system("cls")
                        step3_func()
                else:
                    step4_func()

        def step4_func(): # question 4
            global question4
            global task4attempts
            if task4attempts == 0:
                print("\033[1;31;40m                                                                       You have failed and gone crazy. Game Over\033[0;37;40m \n")
                exit()
            else:
                selection4 = (random.choice(question4))
                slowprint(selection4)
                answer1 = input("\n\033[0;33;40mAnswer?\033[0;37;40m\n\n")
                if selection4 == question4[0]:
                    correct_answer1 = "jackson"
                    if answer1.lower() == correct_answer1:
                        slowprint("\n\033[1;32;40m     Correct!\033[0;37;40m\n")
                        slowprint("As the final letter 'J' turns green the back of the tablet opens up and a fourth key drops to the floor.")
                        print("---------------------------------")
                        print("\033[0;30;41m|\033[0;30;42m   S   \033[0;30;41m|\033[0;30;42m   D   \033[0;30;41m|\033[0;30;42m   L   \033[0;30;41m|\033[0;30;42m   J   \033[0;30;41m|\033[0;37;40m")
                        print("---------------------------------")
                        time.sleep(4)
                        os.system("cls")                        
                        slowprint("\033[1;33;40m                                                   Yellow Key Acquired \033[0m")
                        print("\033[1;33;40m                                                                ")
                        print("                                          8 8 8 8                     ,ooo.")
                        print("                                          8a8 8a8                    oP   ?b  ")
                        print("                                         d888a888zzzzzzzzzzzzzzzzzzzz8     8b")
                        print("                                            `""^""'                      ?o___oP'\033[0;37;40m")
                        print("                                      """)
############################################################################
                        outro_func()
############################################################################

                    else:
                        slowprint("\n\033[1;31;40m     Incorrect!\n")
                        task4attempts -= 1
                        slowprint(f"You have {task4attempts} attempts remaining...\033[0;37;40m\n")
                        question4.pop(0)
                        time.sleep(3)
                        os.system("cls")
                        step4_func()
                elif selection4 == question4[1]:
                    correct_answer1 = "jack"
                    if answer1.lower() == correct_answer1:
                        slowprint("\n\033[1;32;40m     Correct!\033[0;37;40m\n")
                        slowprint("As the final letter 'J' turns green the back of the tablet opens up and a fourth key drops to the floor.")
                        print("---------------------------------")
                        print("\033[0;30;41m|\033[0;30;42m   S   \033[0;30;41m|\033[0;30;42m   D   \033[0;30;41m|\033[0;30;42m   L   \033[0;30;41m|\033[0;30;42m   J   \033[0;30;41m|\033[0;37;40m")
                        print("---------------------------------")
                        time.sleep(4)
                        os.system("cls")                        
                        slowprint("\033[1;33;40m                                                   Yellow Key Acquired \033[0m")
                        print("\033[1;33;40m                                                                ")
                        print("                                          8 8 8 8                     ,ooo.")
                        print("                                          8a8 8a8                    oP   ?b  ")
                        print("                                         d888a888zzzzzzzzzzzzzzzzzzzz8     8b")
                        print("                                            `""^""'                      ?o___oP'\033[0;37;40m")
                        print("                                      """)
############################################################################
                        outro_func()
############################################################################

                    else:
                        slowprint("\n\033[1;31;40m     Incorrect!\n")
                        task4attempts -= 1
                        slowprint(f"You have {task4attempts} attempts remaining...\033[0;37;40m\n")
                        question4.pop(1)
                        time.sleep(3)
                        os.system("cls")
                        step4_func()
                elif selection4 == question4[2]:
                    correct_answer1 = "janet"
                    if answer1.lower() == correct_answer1:
                        slowprint("\n\033[1;32;40m     Correct!\033[0;37;40m\n")
                        slowprint("As the final letter 'J' turns green the back of the tablet opens up and a fourth key drops to the floor.")
                        print("---------------------------------")
                        print("\033[0;30;41m|\033[0;30;42m   S   \033[0;30;41m|\033[0;30;42m   D   \033[0;30;41m|\033[0;30;42m   L   \033[0;30;41m|\033[0;30;42m   J   \033[0;30;41m|\033[0;37;40m")
                        print("---------------------------------")
                        time.sleep(4)
                        os.system("cls")                        
                        slowprint("\033[1;33;40m                                                   Yellow Key Acquired \033[0m")
                        print("\033[1;33;40m                                                                ")
                        print("                                          8 8 8 8                     ,ooo.")
                        print("                                          8a8 8a8                    oP   ?b  ")
                        print("                                         d888a888zzzzzzzzzzzzzzzzzzzz8     8b")
                        print("                                            `""^""'                      ?o___oP'\033[0;37;40m")
                        print("                                      """)
############################################################################
                        outro_func()
############################################################################

                    else:
                        slowprint("\n\033[1;31;40m     Incorrect!\n")
                        task4attempts -= 1
                        slowprint(f"You have {task4attempts} attempts remaining...\033[0;37;40m\n")
                        question4.pop(2)
                        time.sleep(3)
                        os.system("cls")
                        step4_func()
                else:
                    slowprint("you have found a bug. please fix me")
        step1_func()
    def outro_func():
        time.sleep(4)
        os.system("cls")

        slowprint("\n\nGazing upon the door you notice the 4 large brass locks, upon further inspection you see each has a colour...\n\n")
        time.sleep(2)
        print('                                               """"_____________')
        print("                                               |\ ___________ /|")
        print("                                               | |  _ _ _ _  | |")
        print("                                               | | | | | | | | |")
        print("                                               | | |-+-+-+-| | |")
        print("                                               | | |-+-+-+-| | |")
        print("                                               | | |_|_|_|_| | |")
        print("                                               | |     ___   | |")
        print("                                               | |    /__/   | |")
        print("                                               | |   [%==] \033[1;35;40m()\033[0;37;40m| |")
        print("                                               | |         \033[1;32;40m()\033[0;37;40m| |")
        print("                                               | |         \033[1;34;40m()\033[0;37;40m| |")
        print("                                               | |         \033[1;33;40m()\033[0;37;40m| |")
        print("                                               | |           | |")
        print("                                               | |           | |")
        print("                                               |_|___________|_|")
        print('                                               """"\n\n')
        slowprint("Thats it! The colours match the strange #COLOURED KEYS# you have found!")
        time.sleep(3)
        slowprint("You approach the door cautiously...")
        slowprint("                                           ")

        time.sleep(1)
        slowprint("The locks fall one by one, the sound of rusted brass locks cascade on the floor as you frantically turn each key. ")
        time.sleep(4)
        slowprint("The door is heavy, and damp, as you pull the door towards yourself, with every fibre stretched to its breaking point you heave the door towards yourself. ")
        time.sleep(5)
        slowprint("The door groans and shifts slowly open, the cold dark abyss stares back at you, an all-encompassing darkness. ")
        time.sleep(5)
        print("                                           ")
        print("                                           ")
        
        slowprint("You are flooded with dread as something compels you too go further into this slumber, you feel your body move without any thought through the doorway. ")
        time.sleep(5)
        print("                                           ")
        print("                                           ")
        slowprint("Your eyes shoot open as the light floods your face, looking around you notice a nurse filling out a medical sheet, she notices you are awake as she leaves and smile")
        slowprint("Looking around the room you feel a sense of relief, as the wind picks up, it sounds like the trees whispering too you. Relief turns too panic, something from below calls you back...")
        time.sleep(4)
        os.system("cls")
######################################################Credits#######################################################       
        slowprint("\n\n\n\033[1;31;40m                                                  Thank you you playing Patient X!\033[0;37;40m")
        time.sleep(0.5)
        print("\n")
        time.sleep(0.5)
        print("\n")
        time.sleep(0.5)
        print("\n")
        time.sleep(0.5)
        print("\n")
        time.sleep(0.5)
        print("\n")
        time.sleep(0.5)
        print("\n")
        time.sleep(0.5)
        print("\n")
        time.sleep(0.5)
        print("\n")
        time.sleep(0.5)
        print("\n")
        time.sleep(0.5)
        print("\n")
        time.sleep(0.5)
        print("\n")
        
        CURSOR_UP_ONE = '\x1b[1A' 
        ERASE_LINE = '\x1b[2K' 

        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(CURSOR_UP_ONE)
        slowprint("\033[1;36;40m                                                             Team 5 was:")
        time.sleep(2)
        sys.stdout.write(CURSOR_UP_ONE) 
        sys.stdout.write(ERASE_LINE)
        print("\033[1;35;40m                                                            Connor Colman")
        time.sleep(2)
        sys.stdout.write(CURSOR_UP_ONE) 
        sys.stdout.write(ERASE_LINE)
        print("\033[1;36;40m                                                          Adam Jeske-Stock")
        time.sleep(2)
        sys.stdout.write(CURSOR_UP_ONE) 
        sys.stdout.write(ERASE_LINE)
        print("\033[1;34;40m                                                            Hiral Patel")
        time.sleep(2)
        sys.stdout.write(CURSOR_UP_ONE) 
        sys.stdout.write(ERASE_LINE)
        print("\033[1;33;40m                                                           Leigh Hearne")
        time.sleep(2)
        sys.stdout.write(CURSOR_UP_ONE) 
        sys.stdout.write(ERASE_LINE)
        slowprint("\033[1;34;40m                                                      Thank you for playing!")
######################################################Credits#######################################################
        sys.stdout.write(CURSOR_UP_ONE) 
        sys.stdout.write(ERASE_LINE)
        time.sleep(10)
######################################################Goofball#######################################################
        print("\033[1;33;40m                                                LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        time.sleep(1)
        print("\033[1;33;40m        LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        time.sleep(0.9)
        print("\033[1;33;40m                                                                                LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        time.sleep(0.8)
        print("\033[1;33;40m                            LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        time.sleep(0.7)
        print("\033[1;33;40m                                                                        LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        time.sleep(0.6)
        print("\033[1;33;40m                    LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        time.sleep(0.5)
        print("\033[1;33;40m                                                                                        LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        time.sleep(0.1)
        print("\033[1;33;40m                                                    LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        time.sleep(0.1)
        print("\033[1;33;40m        LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        time.sleep(0.1)
        print("\033[1;33;40m                                                                LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        time.sleep(0.1)
        print("\033[1;33;40m                                LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        time.sleep(0.1)
        print("\033[1;33;40m                                                                            LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        time.sleep(0.1)
        print("\033[1;33;40m                                                LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        time.sleep(0.1)
        print("\033[1;33;40m        LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        time.sleep(0.1)
        print("\033[1;33;40m                                                                                LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        time.sleep(0.1)
        print("\033[1;33;40m                            LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        time.sleep(0.1)
        print("\033[1;33;40m                                                                        LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        time.sleep(0.1)
        print("\033[1;33;40m                    LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        time.sleep(0.1)
        print("\033[1;33;40m                                                                                        LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        time.sleep(0.1)
        print("\033[1;33;40m                                                    LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        time.sleep(0.1)
        print("\033[1;33;40m        LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        time.sleep(0.1)
        print("\033[1;33;40m                                                                LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        time.sleep(0.1)
        print("\033[1;33;40m                                LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        time.sleep(0.1)
        print("\033[1;33;40m                                                                            LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(CURSOR_UP_ONE)
        time.sleep(0.1)
        print("\033[1;33;40m                                                LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(CURSOR_UP_ONE)
        time.sleep(0.1)
        print("\033[1;33;40m        LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        sys.stdout.write(CURSOR_UP_ONE)
        time.sleep(0.1)
        print("\033[1;33;40m                                                                                        LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        sys.stdout.write(CURSOR_UP_ONE)
        time.sleep(0.1)
        print("\033[1;33;40m                    LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(CURSOR_UP_ONE)
        time.sleep(0.1)
        print("\033[1;33;40m                                                    LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        sys.stdout.write(CURSOR_UP_ONE)
        time.sleep(0.01)
        print("\033[1;33;40m                                                                LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        sys.stdout.write(CURSOR_UP_ONE)
        time.sleep(0.01)
        print("\033[1;33;40m                                LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        sys.stdout.write(CURSOR_UP_ONE)
        time.sleep(0.01)
        print("\033[1;33;40m                                                                            LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        sys.stdout.write(CURSOR_UP_ONE)
        time.sleep(0.1)
        print("\033[1;33;40m                                                LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        sys.stdout.write(CURSOR_UP_ONE)
        time.sleep(0.1)
        print("\033[1;33;40m        LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        sys.stdout.write(CURSOR_UP_ONE)
        time.sleep(0.1)
        print("\033[1;33;40m                                                                                        LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        sys.stdout.write(CURSOR_UP_ONE)
        time.sleep(0.1)
        print("\033[1;33;40m                    LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        sys.stdout.write(CURSOR_UP_ONE)
        time.sleep(0.1)
        print("\033[1;33;40m                                                    LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        sys.stdout.write(CURSOR_UP_ONE)
        time.sleep(0.01)
        print("\033[1;33;40m                                                                LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        sys.stdout.write(CURSOR_UP_ONE)
        time.sleep(0.01)
        print("\033[1;33;40m                                LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        sys.stdout.write(CURSOR_UP_ONE)
        time.sleep(0.01)
        print("\033[1;33;40m                                                                            LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        sys.stdout.write(CURSOR_UP_ONE)
        time.sleep(0.1)
        print("\033[1;33;40m                                                LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        sys.stdout.write(CURSOR_UP_ONE)
        time.sleep(0.1)
        print("\033[1;33;40m        LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        sys.stdout.write(CURSOR_UP_ONE)
        time.sleep(0.1)
        print("\033[1;33;40m                                                                                        LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        sys.stdout.write(CURSOR_UP_ONE)
        time.sleep(0.1)
        print("\033[1;33;40m                    LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        sys.stdout.write(CURSOR_UP_ONE)
        time.sleep(0.1)
        print("\033[1;33;40m                                                    LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        sys.stdout.write(CURSOR_UP_ONE)
        time.sleep(0.01)
        print("\033[1;33;40m                                                                LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        sys.stdout.write(CURSOR_UP_ONE)
        time.sleep(0.01)
        print("\033[1;33;40m                                LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        sys.stdout.write(CURSOR_UP_ONE)
        time.sleep(0.01)
        print("\033[1;33;40m                                                                            LETS GO CRAZY!!! PARTY TIIIIME!!!!")
        time.sleep(1)
        os.system("cls")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n                                                                      \033[1;31;40mMy bad.")

        time.sleep(3)

######################################################Goofball#######################################################

        exit()
     
    intro_func()                   
patientx_func()