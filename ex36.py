from sys import exit
import random

#Zork style game with a World of Warcraft theme
def start():
    print("Welcome to Lord of the Haywars!")
    print("Press 'q' to end the game and 'a' to see abilities.")
    print("Press 'z' to start game.")

    choice = ''
    while choice == '':
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
    print("'The time has come... he says, and starts to walk away")
    print("What do you do?")
    print("Follow, run, leave...")
    choice2 = input('> ')

    if 'follow' in choice2:
        training(classChoice)
    else:
        print("We knew you wouldnt be a hero...")
        exit(0)

#Training function and intro to abilities list
def training(userClass):
    abilities = []
    print("The hooded figure leads you to a savage looking man with a sword")

    print(f"Welcome, {userClass}. I am the Gaurd Captian. Here we will hone our skills.")
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

    #Ability input test
    print('Type in 1, 2, or 3 to use the abilites. Lets try.')
    usedAbility = int(input('Ability: '))
    print(f"You used {abilities[usedAbility - 1]}!")
    print("Ready for more? Y/N")
    ready = input('> ')
    if ready == 'y':
        print('The city guard comes running in!')
        print(f"{newClass}! We need your help now!")
        print("Miners have gone missing in the mine and we need help!")
        dungeonPrep(newClass, abilities)
    else:
        print('All done..')
        exit(0)

#First stage of the dungeon giving opportunity to grab an items
# and get ready to leave for the adventure
def dungeonPrep(userClass, classAbilities):
    userClass = userClass
    abilities = classAbilities
    inventory = []
    print(f"Gather your courage {userClass}, we leave now.")
    print("As you get ready to leave you look around and find a bag.")
    print("What do you do?")
    print("Look around, leave")
    d_choice = input('> ')


    if d_choice == 'look around':
        print('You see a potion, bread, and an old amulet.')
        d_choice1 = input('> ')
        if 'take' in d_choice1 and 'potion' in d_choice1:
            print('You put the potion in your bag.')
            inventory.append('potion')
            print('-' * 10)
            dungeonStart(userClass, abilities, inventory)
        elif 'take' in d_choice1 and 'bread' in d_choice1:
            print('You put the bread in your bag.')
            inventory.append('bread')
            print('-' * 10)
            dungeonStart(userClass, abilities, inventory)
        elif 'take' in d_choice1 and 'amulet' in d_choice1:
            print('You put the amulet in your bag.')
            inventory.append('amulet')
            print('-' * 10)
            dungeonStart(userClass, abilities, inventory)
    elif d_choice == 'leave':
            dungeonStart(userClass, abilities, inventory)
    else:
        print(f'Cmon {userClass}, hurry up!')
        d_choice = input('> ')

#Start monster encounters
def dungeonStart(userClass, classAbilities, inventory):
    userClass = userClass
    classAbilities = classAbilities
    inventory = inventory
    print(f"Keep your wits about you {userClass}")
    print('There is a torch on the wall and two dark tunnels. One left'
            ' and one to the right.')
    choice1 = ''
    while choice1 != 'move left' and choice1 != 'move right':
        choice1 = input('> ')
        if 'take' in choice1 and 'torch' in choice1:
            inventory.append('torch')
            print('Now what?')
            choice1 = input('> ')
        elif 'move' in choice1 and 'left' in choice1:
            print('Its so dark...')
            dungeonPartA(userClass, classAbilities, inventory)
        elif 'move' in choice1 and 'right' in choice1:
            print('WHOA! There is a huge spider here!')
            dungeonPartB(userClass, classAbilities, inventory)
        else:
            print("That doesnt seem like a good idea")
            choice1 = input('> ')

#Has to guess a code. to go to part b
def dungeonPartA(userClass, classAbilities, inventory):
    action = input('What do you do? > ')
#Has to defeat spider to go to A
def dungeonPartB(userClass, classAbilities, inventory):
    action = input('What do you do? > ')
#both a and b compelte and fight final boss and get and game
def dungeonEnd(userClass, classAbilities, inventory):
    action = input('What do you do? > ')
start()
