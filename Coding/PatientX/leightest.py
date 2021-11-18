import random
import sys
import time

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

        def slowprint(s):
            for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(1./50)
        slowprint("A distant memory flashes into your mind! A view of an auditorium with seats stretching out before you, all facing a huge screen. Suddenly the screen fills with light and shows a view of the Earth from space. From the right side, a single word moves to the centre in large captitals...")
        slowprint("\n\n\n                                               'UNIVERSAL'                                                     \n\n\n")
        slowprint("As quickly as it came, it is gone, and you realise you are back in the hospital. Was this a clue to what is to come? ")
        slowprint("\nNext to the bed is a cabinet. A clinical white, but clearly old and used. It seems locked, but it is fragile enough to prise off.")
        slowprint("It comes off cleanly in your hand, and inside lies a digital screen connected to a simple keyboard.")
        slowprint("The screen shows 4 red boxes with a letter in each box:")

        print("---------------------------------")
        print("\033[0;30;41m|   S   |   D   |   L   |   J   |\033[0;37;40m")
        print("---------------------------------")

        slowprint("As you press 'Enter', the following text is displayed:")
        task4_func

        def step1_func(): # question 1
            global question1
            global task4attempts

            if task4attempts == 0:
                print("\033[1;31;40mYou have failed and gone crazy. Game Over\033[0;37;40m \n")
            else:
                selection1 = (random.choice(question1))

                print("\n")        
                slowprint(selection1)
                answer1 = input("\n\033[0;33;40mAnswer?\033[0;37;40m\n\n")
                if selection1 == question1[0]:
                    correct_answer1 = "shining"
                    if answer1.lower() == correct_answer1:
                        slowprint("\n\033[1;32;40m     Correct!\033[0;37;40m\n")
                        print("---------------------------------")
                        print("\033[0;30;41m|\033[0;30;42m   S   \033[0;30;41m|   D   |   L   |   J   |\033[0;37;40m")
                        print("---------------------------------")
                        step2_func()
                    else:
                        slowprint("\n\033[1;31;40m     Incorrect!\n")
                        task4attempts -= 1
                        slowprint(f"You have {task4attempts} attempts remaining...\033[0;37;40m\n")
                        question1.pop(0)
                        step1_func()
                elif selection1 == question1[1]:
                    correct_answer1 = "shutter"
                    if answer1.lower() == correct_answer1:
                        slowprint("\n\033[1;32;40m     Correct!\033[0;37;40m\n")
                        print("---------------------------------")
                        print("\033[0;30;41m|\033[0;30;42m   S   \033[0;30;41m|   D   |   L   |   J   |\033[0;37;40m")
                        print("---------------------------------")
                        step2_func()
                    else:
                        slowprint("\n\033[1;31;40m     Incorrect!\n")
                        task4attempts -= 1
                        slowprint(f"You have {task4attempts} attempts remaining...\033[0;37;40m\n")
                        question1.pop(1)
                        step1_func()
                elif selection1 == question1[2]:
                    correct_answer1 = "silence"
                    if answer1.lower() == correct_answer1:
                        slowprint("\n\033[1;32;40m     Correct!\033[0;37;40m\n")
                        print("---------------------------------")
                        print("\033[0;30;41m|\033[0;30;42m   S   \033[0;30;41m|   D   |   L   |   J   |\033[0;37;40m")
                        print("---------------------------------")
                        step2_func()
                    else:
                        slowprint("\n\033[1;31;40m     Incorrect!\n")
                        task4attempts -= 1
                        slowprint(f"You have {task4attempts} attempts remaining...\033[0;37;40m\n")
                        question1.pop(2)
                        step1_func()
                else:
                    step1_func() 
          
        def step2_func(): # question 2
            global question2
            global task4attempts
            if task4attempts == 0:
                print("\033[1;31;40mYou have failed and gone crazy. Game Over\033[0;37;40m \n")
            else:
                selection2 = (random.choice(question2))
                def slowprint(s):
                    for c in s + '\n':
                        sys.stdout.write(c)
                        sys.stdout.flush()
                        time.sleep(1./50)
                slowprint(selection2)
                answer1 = input("\n\033[0;33;40mAnswer?\033[0;37;40m\n\n")
                if selection2 == question2[0]:
                    correct_answer1 = "darko"
                    if answer1.lower() == correct_answer1:
                        slowprint("\n\033[1;32;40m     Correct!\033[0;37;40m\n")
                        print("---------------------------------")
                        print("\033[0;30;41m|\033[0;30;42m   S   \033[0;30;41m|\033[0;30;42m   D   \033[0;30;41m|   L   |   J   |\033[0;37;40m")
                        print("---------------------------------")
                        step3_func()
                    else:
                        slowprint("\n\033[1;31;40m     Incorrect!\n")
                        task4attempts -= 1
                        slowprint(f"You have {task4attempts} attempts remaining...\033[0;37;40m\n")
                        question2.pop(0)
                        step2_func()
                elif selection2 == question2[1]:
                    correct_answer1 = "durden"
                    if answer1.lower() == correct_answer1:
                        slowprint("\n\033[1;32;40m     Correct!\033[0;37;40m\n")
                        print("---------------------------------")
                        print("\033[0;30;41m|\033[0;30;42m   S   \033[0;30;41m|\033[0;30;42m   D   \033[0;30;41m|   L   |   J   |\033[0;37;40m")
                        print("---------------------------------")
                        step3_func()
                    else:
                        slowprint("\n\033[1;31;40m     Incorrect!\n")
                        task4attempts -= 1
                        slowprint(f"You have {task4attempts} attempts remaining...\033[0;37;40m\n")
                        question2.pop(1)
                        step2_func()
                elif selection2 == question2[2]:
                    correct_answer1 = "de niro"
                    if answer1.lower() == correct_answer1:
                        slowprint("\n\033[1;32;40m     Correct!\033[0;37;40m\n")
                        print("---------------------------------")
                        print("\033[0;30;41m|\033[0;30;42m   S   \033[0;30;41m|\033[0;30;42m   D   \033[0;30;41m|   L   |   J   |\033[0;37;40m")
                        print("---------------------------------")
                        step3_func()
                    else:
                        slowprint("\n\033[1;31;40m     Incorrect!\n")
                        task4attempts -= 1
                        slowprint(f"You have {task4attempts} attempts remaining...\033[0;37;40m\n")
                        question2.pop(2)
                        step2_func()
                else:
                    step3_func()
       
        def step3_func(): # question 3
            global question3
            global task4attempts
            if task4attempts == 0:
                print("\033[1;31;40mYou have failed and gone crazy. Game Over\033[0;37;40m \n")
            else:
                selection3 = (random.choice(question3))
                def slowprint(s):
                    for c in s + '\n':
                        sys.stdout.write(c)
                        sys.stdout.flush()
                        time.sleep(1./50)
                slowprint(selection3)
                answer1 = input("\n\033[0;33;40mAnswer?\033[0;37;40m\n\n")
                if selection3 == question3[0]:
                    correct_answer1 = "ledger"
                    if answer1.lower() == correct_answer1:
                        slowprint("\n\033[1;32;40m     Correct!\033[0;37;40m\n")
                        print("---------------------------------")
                        print("\033[0;30;41m|\033[0;30;42m   S   \033[0;30;41m|\033[0;30;42m   D   \033[0;30;41m|\033[0;30;42m   L   \033[0;30;41m|   J   |\033[0;37;40m")
                        print("---------------------------------")
                        step4_func()
                    else:
                        slowprint("\n\033[1;31;40m     Incorrect!\n")
                        task4attempts -= 1
                        slowprint(f"You have {task4attempts} attempts remaining...\033[0;37;40m\n")
                        question3.pop(0)
                        step3_func()
                elif selection3 == question3[1]:
                    correct_answer1 = "loathing"
                    if answer1.lower() == correct_answer1:
                        slowprint("\n\033[1;32;40m     Correct!\033[0;37;40m\n")
                        print("---------------------------------")
                        print("\033[0;30;41m|\033[0;30;42m   S   \033[0;30;41m|\033[0;30;42m   D   \033[0;30;41m|\033[0;30;42m   L   \033[0;30;41m|   J   |\033[0;37;40m")
                        print("---------------------------------")
                        step4_func()
                    else:
                        slowprint("\n\033[1;31;40m     Incorrect!\n")
                        task4attempts -= 1
                        slowprint(f"You have {task4attempts} attempts remaining...\033[0;37;40m\n")
                        question3.pop(1)
                        step3_func()
                elif selection3 == question3[2]:
                    correct_answer1 = "lewis"
                    if answer1.lower() == correct_answer1:
                        slowprint("\n\033[1;32;40m     Correct!\033[0;37;40m\n")
                        print("---------------------------------")
                        print("\033[0;30;41m|\033[0;30;42m   S   \033[0;30;41m|\033[0;30;42m   D   \033[0;30;41m|\033[0;30;42m   L   \033[0;30;41m|   J   |\033[0;37;40m")
                        print("---------------------------------")
                        step4_func()
                    else:
                        slowprint("\n\033[1;31;40m     Incorrect!\n")
                        task4attempts -= 1
                        slowprint(f"You have {task4attempts} attempts remaining...\033[0;37;40m\n")
                        question3.pop(2)
                        step3_func()
                else:
                    step4_func()

        def step4_func(): # question 4
            global question4
            global task4attempts
            if task4attempts == 0:
                print("\033[1;31;40mYou have failed and gone crazy. Game Over\033[0;37;40m \n")
            else:
                selection4 = (random.choice(question4))
                def slowprint(s):
                    for c in s + '\n':
                        sys.stdout.write(c)
                        sys.stdout.flush()
                        time.sleep(1./50)
                slowprint(selection4)
                answer1 = input("\n\033[0;33;40mAnswer?\033[0;37;40m\n\n")
                if selection4 == question4[0]:
                    correct_answer1 = "jackson"
                    if answer1.lower() == correct_answer1:
                        slowprint("\n\033[1;32;40m     Correct!\033[0;37;40m\n")
                        print("---------------------------------")
                        print("\033[0;30;41m|\033[0;30;42m   S   \033[0;30;41m|\033[0;30;42m   D   \033[0;30;41m|\033[0;30;42m   L   \033[0;30;41m|\033[0;30;42m   J   \033[0;30;41m|\033[0;37;40m")
                        print("---------------------------------")

                        ############################################################

                        ############################################################

                    else:
                        slowprint("\n\033[1;31;40m     Incorrect!\n")
                        task4attempts -= 1
                        slowprint(f"You have {task4attempts} attempts remaining...\033[0;37;40m\n")
                        question4.pop(0)
                        step4_func()
                elif selection4 == question4[1]:
                    correct_answer1 = "jack"
                    if answer1.lower() == correct_answer1:
                        slowprint("\n\033[1;32;40m     Correct!\033[0;37;40m\n")
                        print("---------------------------------")
                        print("\033[0;30;41m|\033[0;30;42m   S   \033[0;30;41m|\033[0;30;42m   D   \033[0;30;41m|\033[0;30;42m   L   \033[0;30;41m|\033[0;30;42m   J   \033[0;30;41m|\033[0;37;40m")
                        print("---------------------------------")

                        ############################################################

                        ############################################################

                    else:
                        slowprint("\n\033[1;31;40m     Incorrect!\n")
                        task4attempts -= 1
                        slowprint(f"You have {task4attempts} attempts remaining...\033[0;37;40m\n")
                        question4.pop(1)
                        step4_func()
                elif selection4 == question4[2]:
                    correct_answer1 = "janet"
                    if answer1.lower() == correct_answer1:
                        slowprint("\n\033[1;32;40m     Correct!\033[0;37;40m\n")
                        print("---------------------------------")
                        print("\033[0;30;41m|\033[0;30;42m   S   \033[0;30;41m|\033[0;30;42m   D   \033[0;30;41m|\033[0;30;42m   L   \033[0;30;41m|\033[0;30;42m   J   \033[0;30;41m|\033[0;37;40m")
                        print("---------------------------------")

                        ############################################################

                        ############################################################

                    else:
                        slowprint("\n\033[1;31;40m     Incorrect!\n")
                        task4attempts -= 1
                        slowprint(f"You have {task4attempts} attempts remaining...\033[0;37;40m\n")
                        question4.pop(2)
                        step4_func()
                else:
                    slowprint("you have found a bug. please fix me")
task4_func()