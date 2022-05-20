from sys import exit
from random import randint
from textwrap import dedent

#Basics classes to start game and make scenes
class Scene(object):

    def enter(self):
        print('Scene has not been completed')
        exit(1)

class WagonRide(Scene):

    def enter(self):
        print(dedent("""
                    From black your eyes start to focus on your feet.
                    What happened? "Hey you. You're finally awake." You look
                    and see a man bound at the hands and notice you are as well.
                    """))

        print(dedent("""
                    You arrive at a small city crawling with guards and they
                    start to unload you and the others from the wagon you were
                    riding in. "Who are you?" a guard asks holding a scroll.
                    """))

        name = input('Name: ')
        race = input('Race: ')

        print(dedent("""
                    We dont have any {race}'s on the list. Send {name} to the
                    block. We keep no prisoners today. You see the man who talked to
                    you in the wagon take off running.
                    """))

        print(dedent("""
                    PHEWWWW! An arrow slings past your head into the mans back.
                    you start being escorted to the chopping block. What do you do?

                    - run
                    - fight the guards
                    - nothing
                    """))
        action1 = input('> ')
        if action1 != 'nothing':
            print(dedent("""
                        You start to struggle and at first sign the guards throw
                        you to the ground and put their foot on your back. "The
                        block would hurt less." They say as they slowly shove a
                        sword into your ribs.
                        """))
            return 'death'
        else:
            print(dedent("""
                        You slowly walk to the block and kneel. As the headsman
                        raises his axe the ground shakes... "DRAGON!", yell the
                        guards as they all scatter. What do you do?

                        - nothing
                        - help them fight
                        - run
                        """))

        action2 = input('> ')

        if action2 != 'run':
            print(dedent("""
                        The dragons fire sets the whole town ablaze almost
                        instantly. The gaurds scream for their lives as you can
                        do almost nothing to help. The dragon lands and crushes
                        your body doing so...
                        """))
            return 'death'
        else:
            print(dedent("""
                        You sieze the opportunity of distracted and fear filled
                        guards to run toward a broken part of the wall escaping
                        the city with nobody noticing. The road is split. Do
                        you go left or right?
                        """))

        direction = input('> ')

        if direction == 'right':
            print(dedent("""
                        You run as fast as you can for what seems like 7 minutes.
                        You see what looks like a rustic village in the distance.
                        Shedding your bindings you slow you pace and walk in
                        pretending you know exactly whats going on.
                        """))
        else:
            print(dedent("""
                        You are so scared and confused by whats going on you start
                        running straight toward a pack of wolves and then realize
                        your hands are still bound. The wolves eat well...
                        """))
            return 'death'


        return 'riverrun'

class Riverrun(Scene):

    def enter(self):
        print('Traiging')
        return 'whiterun'

class Whiterun(Scene):

    def enter(self):
        print('Whiterun')
        return 'bandits'

class BanditFight(Scene):

    def enter(self):
        print('Bandit')
        return 'dragon'

class DragonFight(Scene):

    def enter(self):
        print('Dragon')
        return 'death'

class Death(Scene):

    quotes = [
        'The dragonborn is no more....',
        'Only a fool dies in such a manner.',
        'You are really bad at this huh?',
        'FUS-ROH-DEAD!',
        'Now who is going to take care of Lydia?',
    ]
    def enter(self):
        print(Death.quotes[randint(0, len(self.quotes)-1)])
        exit(1)

class End(Scene):

    def enter(self):
        print('End')
        return 'end'
