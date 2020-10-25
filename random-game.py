import time
import sys
import random
import os

def banner_menu():
    print("""
    -------------------------------------------
              Python 'Random' Game
    -------------------------------------------
    
    1- Easy
    2- Medium
    3- Hard
    4- God
    5- Exit

    ---------------------------------------------
    """)
    print("")
    choice = int(input("[ ? ] Make a choise > "))

    if choice == 1:
        easy()
    elif choice == 2:
        medium()
    elif choice == 3:
        hard()
    elif choice == 4:
        god()
    elif choice == 5:
        sys.exit()
    else:
        print("Wrong input. Try again! ")
        if sys.platform == "linux":
            time.sleep(1)
            os.system("clear")
        elif sys.platform == "win32":
            time.sleep(1)
            os.system("cls")
        banner_menu()
    
def easy():
    
    if sys.platform == "linux":
            time.sleep(1)
            os.system("clear")
    elif sys.platform == "win32":
            time.sleep(1)
            os.system("cls")

    guess_easy = int(input("[ ? ] Guess a number between 0 and 10 > "))

    easy_number = random.randrange(0, 10)
    
    if guess_easy == easy_number:
        print("[ + ] Congratulations, you found.")
    else:
        print("[ - ] Wrong answer. ","Number is : ",easy_number)
        time.sleep(1)
        banner_menu()


def medium():
    
    if sys.platform == "linux":
            time.sleep(1)
            os.system("clear")
    elif sys.platform == "win32":
            time.sleep(1)
            os.system("cls")

    guess_medium = int(input("[ ? ] Guess a number between 0 and 20 > "))

    medium_number = random.randrange(0, 20)
    
    if guess_medium == medium_number:
        print("[ + ] Congratulations, you found.")
    else:
        print("[ - ] Wrong answer. ","Number is : ",medium_number)
        time.sleep(1)
        banner_menu()



def hard():
    
    if sys.platform == "linux":
            time.sleep(1)
            os.system("clear")
    elif sys.platform == "win32":
            time.sleep(1)
            os.system("cls")

    guess_hard = int(input("[ ? ] Guess a number between 0 and 30 > "))

    hard_number = random.randrange(0, 30)
    
    if guess_hard == hard_number:
        print("[ + ] Congratulations, you found.")
    else:
        print("[ - ] Wrong answer. ","Number is : ",hard_number)
        time.sleep(1)
        banner_menu()



def god():
    
    if sys.platform == "linux":
            time.sleep(1)
            os.system("clear")
    elif sys.platform == "win32":
            time.sleep(1)
            os.system("cls")

    guess_god = int(input("[ ? ] Guess a number between 0 and 50 > "))

    god_number = random.randrange(0, 50)
    
    if guess_god == god_number:
        print("[ + ] Congratulations, you found.")
    else:
        print("[ - ] Wrong answer. ","Number is : ",god_number)
        time.sleep(1)
        banner_menu()

banner_menu()