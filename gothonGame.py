from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
    def enter(self):
        print('This scene is not yet configured.')
        print('Subclass it and implent enter()')
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        #be sure to print out last scene
        current_scene.enter()

class Death(Scene):
    quips = [
        "You Died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter",
        "Such a loser",
        "I have a small puppy thats better at this.",
        "You're worse than your dads jokes"
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
            The Gothons of Plant Percal #25 have invaded your ship and
            destroyed your entire crew. You are the last surviving
            member and your last mission is to get the neutron destruct
            bomb from the Weapons Armory, put it in the bridge, and
            blow up the ship after getting into an escape pod.

            You're running down the central corrido to the Weapons
            Armory when a Gothon jumps out, red scaly skin, dark grimy
            filled body. He is blocking the door to the Armory append
            about to pull a weapon to blast you.
            """))

            action = input('> ')

            if action == 'shoot':
                print(dedent("""
                    Quick on the draw you yank out your blaster and fire
                    it at the Gothon. His clown costume is flowing and moving
                    around his body, which throws off your aim. You laser
                    hits his costume but misses him entirely.
                    This completely ruins his brand new costume his mother
                    made him which makes him fly into an insane rage and blast
                    you repeatedly in the face until you are dead.
                    """))

                return 'death'

            elif action == 'dodge':
                print(dedent("""
                    Like a world class boxer you dodge, weave, and slip around
                    each shot from the blaster. In the middle of the artful
                    dodge your foot slips and you bang your head into a metal
                    wall and pass out. You wake up shortly after only to die
                    as the Gothon stomps on your head and eats you.
                    """))
                return 'death'

            elif action == 'tell a joke':
                print(dedent("""
                    Lucky for you they made you leanr Gothon insults in
                    the academy. You tell the on Gothon joke you know:
                    Lbhe zuber vf fb sng, jurnan jforrun. The Gothon stops,
                    tries not to laugh, then busts out laughing and cant move.
                    Whiles he is laughing you run up and shoot him in the
                    head putting him down, then jump through the Weapon
                    Armory Door.
                    """))
                return 'laser_weapon_armor'

            else:
                print('DOES NOT COMPUTE!')
                return 'central_corridor'
