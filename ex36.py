from sys import exit
import random

#Zork style game with a World of Warcraft theme
def start():
    print("Welcome to Lord of the Haywars!")
    print("Press 'q' to end the game and 'a' to see abilities.")
    print("Press 'z' to start game.")


    while True:
        choice = input('> ')
        if choice == 'z':
            character_select()
        elif choice == 'a':
            print("No abilites yet..")
        elif choice == 'q':
            exit(0)
        else:
            print("Thats not a command. Try 'a' 'q' or 'z'")

#Character selection function
def character_select():
    print("You open your eyes and see three stones floating in front of you.")
    print("A red stone, blue stone, and a green stone.")
    print("What do you do?")

    #Initial class choice
    choice = input('> ')
    classChoice = ''
    if 'take' in choice and 'red' in choice:
        print("You pick up the stone and feel incredibly strong!")
        print("You start to feel the power grow in your arms!")
        classChoice = 'Warrior'
    elif 'take' in choice and 'blue' in choice:
        print("You pick up the stone and feel a surge of knowledge!")
        print("You start to feel the power grow in you mind!")
        classChoice = 'Mage'
    elif 'take' in choice and 'green' in choice:
        print("You pick up the stone and feel a surge deftness")
        print("You start to feel the power grow in you hands and eyes!")
        classChoice = 'Hunter'
    elif choice == 'q':
        exit(0)
    else:
        print("Try taking a stone instead")
    #Space buffer for text
    num = 5
    i = 0
    while i < num:
        print('*')
        i += 1

    #Option to follow and start training() or ....
    print("After taking the stone a hooded figure comes to you.")
    print("'The time has come...' he says, and starts to walk away.'")
    choice2 = input('> ')

    if 'follow' in choice2:
        training(classChoice)
    else:
        print("We knew you wouldnt be a hero...")
        exit(0)

#Training function and intro to abilities list
def training(userClass):
    abilities = []
    print(f"Welcome, {userClass}. Here we will hone our skills.")
    newClass = userClass

    if newClass == 'Warrior':
        abilities.append('Attack')
        abilities.append('Slam')
        abilities.append('Jump')
        print(f"Your abilities are {abilities[0]}, {abilities[1]}, and {abilities[2]}")
    elif newClass == 'Mage':
        abilities.append('Attack')
        abilities.append('Teleport')
        abilities.append('Fireball')
        print(f"Your abilities are {abilities[0]}, {abilities[1]}, and {abilities[2]}")

    else:
        abilities.append('Attack')
        abilities.append('Call Animal')
        abilities.append('Poison Shot')
        print(f"Your abilities are {abilities[0]}, {abilities[1]}, and {abilities[2]}")

    print('The city guard comes running in!')
    print(f"{newClass}! We need your help now!")
    print("Miners have gone missing in the mine and we need help!")
    print("What do you do?")

    choice = input('> ')


start()
