# CODE FOR TEXT BASED ADEVENTURE GAME 
import time

def game_start():
    print("Welcome to the Haunted House Adventure!")
    time.sleep(1)
    print("You find yourself standing in front of a mysterious old house.")
    time.sleep(1)
    print("Legend has it that the house is haunted and holds hidden treasures.")
    time.sleep(1)
    print("Your goal is to explore the house and find the treasure.")
    time.sleep(1)
    print("Let's begin!\n")
    time.sleep(1)
    enter_house()

def enter_house():
    print("You step inside the house.")
    time.sleep(1)
    print("It is dark and eerie. You can see three doors ahead.")
    time.sleep(1)
    print("Which door will you choose?")
    print("1. Door on the left")
    print("2. Door in the middle")
    print("3. Door on the right")
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        door_left()
    elif choice == '2':
        door_middle()
    elif choice == '3':
        door_right()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        enter_house()

def door_left():
    print("\nYou chose the door on the left.")
    time.sleep(1)
    print("You enter a dusty library.")
    time.sleep(1)
    print("There's a bookshelf with a hidden switch.")
    time.sleep(1)
    print("Pull the switch or leave?")
    choice = input("Enter 'pull' or 'leave': ")
    
    if choice.lower() == 'pull':
        print("\nYou pull the switch and hear a mechanical sound.")
        time.sleep(1)
        print("A secret passage opens!")
        time.sleep(1)
        explore_secret_room()
    elif choice.lower() == 'leave':
        print("\nYou decide to leave the library.")
        time.sleep(1)
        enter_house()
    else:
        print("Invalid choice. Please enter 'pull' or 'leave'.")
        door_left()

def door_middle():
    print("\nYou chose the door in the middle.")
    time.sleep(1)
    print("You find yourself in a creepy dining hall.")
    time.sleep(1)
    print("There's a table set for a meal with a covered dish.")
    time.sleep(1)
    print("Open the dish or leave?")
    choice = input("Enter 'open' or 'leave': ")
    
    if choice.lower() == 'open':
        print("\nYou lift the cover and find a key!")
        time.sleep(1)
        print("The key might be useful.")
        time.sleep(1)
        enter_house()
    elif choice.lower() == 'leave':
        print("\nYou decide to leave the dining hall.")
        time.sleep(1)
        enter_house()
    else:
        print("Invalid choice. Please enter 'open' or 'leave'.")
        door_middle()

def door_right():
    print("\nYou chose the door on the right.")
    time.sleep(1)
    print("You enter a spooky bedroom.")
    time.sleep(1)
    print("There's a large wardrobe against the wall.")
    time.sleep(1)
    print("Search the wardrobe or leave?")
    choice = input("Enter 'search' or 'leave': ")
    
    if choice.lower() == 'search':
        print("\nYou search the wardrobe and find a creepy doll.")
        time.sleep(1)
        print("The doll's eyes seem to follow you.")
        time.sleep(1)
        enter_house()
    elif choice.lower() == 'leave':
        print("\nYou decide to leave the bedroom.")
        time.sleep(1)
        enter_house()
    else:
        print("Invalid choice. Please enter 'search' or 'leave'.")
        door_right()

def explore_secret_room():
    print("\nYou enter the secret room.")
    time.sleep(1)
    print("It's filled with cobwebs and old chests.")
    time.sleep(1)
    print("You open a chest and find the hidden treasure!")
    time.sleep(1)
    print("Congratulations! You win!")
    play_again()

def play_again():
    print("\nDo you want to play again?")
    choice = input("Enter 'yes' or 'no': ")
    
    if choice.lower() == 'yes':
        game_start()
    elif choice.lower() == 'no':
        print("Thank you for playing!")
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")
        play_again()

if __name__ == "__main__":
    game_start()
