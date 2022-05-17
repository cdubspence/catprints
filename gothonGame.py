from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
    #All other Scene objects have an enter() function that ovverride this
    #one. This one will print if a class that is-a Scene() does not have an
    #enter() funtion
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

            tell a joke

            dodge

            shoot
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

class LaserWeaponArmory(Scene):
    def enter(self):
        print(dedent("""
            You do a dive roll into the armory, crouch and scan
            the room for more Gothons. Its dead quiet. You stand up
            and run to the far side of the room and find the neutron
            bomb in its container. Theres a keypad on the lock and you need
            the code to get the bomb out. If you get the code wrong 10 times
            then lock will close forever. The code is 3 digits.
            """))

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 9:
            print("BZZZZEDD")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
                The container clicks open and the seal breaks, letting
                gas out. You grab the neutron bomb and run as fast as you
                can to the bridge where you must place it in the right spot.
                """))
            return 'the_bridge'

        else:
            print(dedent("""
                The lock buzzes one last time and then you hear a
                sickening melting sound as the mechanism is fused together.
                You decide to sit there, and finally the Gothons blow up
                the ship from their ship and you cry...this is the end.
                """))

            return 'death'

class TheBridge(Scene):
    def enter(self):
        print(dedent("""
            You burst onto the bridge with the bomb under your arm and surprise
            5 Gothons who are trying to take control of the ship. Each of them
            has an even uglier clown costume than the last. They havent
            pulled thier weapons out yet, as they see the active bomb under
            your arm and dont want to set it off.

            throw the bomb

            slowly place the bomb
            """))

        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
                In panic you throw the bomb at the group of Gothons
                and make a leap for the door. Right as you  drop it a Gothon
                shoots you in the back killing you. As you die you see another
                Gothon frantically trying to difuse the bomb. You die knowing
                they will probably blow up when it goes off.
                """))

            return 'death'

        elif action == 'slowly place the bomb':
            print(dedent("""
                You point your blaster at the bomb under your arm and
                the Gothons put their hands up and start to sweat. You inch
                backward to the door, open it, and then carefully place
                the bomb on the floow, pointing your blaster at it. You
                then jump back through the door, punch the close button
                and blast the lock so the Gothons cant get out. Now that
                the bomb is placed you run to the escape pods.
                """))

            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE")
            return 'the_bridge'

class EscapePod(Scene):
    def enter(self):
        print(dedent("""
            You rush through the ship desperately trying to make it to
            the escape pod before the whole ship explodes. It seems like
            hardly any Gothons are on the ship, so your run is free and
            clear. You get to the chamber with the pods and need to pick one.
            Some of them could be damaged but you dont have time to check.
            There are 5, which one do you take?
            """))

        good_pod = randint(1,5)
        guess = input("[pod #]> ")

        if guess != good_pod:
            print(dedent("""
                You jump into pod {guess} and hit the eject button,
                The pod escapes out into the void of space, then
                implodes as the hull ruptures, crushing your body into
                jam jelly.
                """))
            return 'death'
        else:
            print(dedent("""
                You jump into the pod {guess} and hit the eject button,
                The pod easily slides out into space heading to the
                planet below. As it flies to the planet, you look back
                and see your ship implode then explode like a bright star,
                taking out the Gothon ship at the same time. You WON!
                """))

            return 'finished'

class Finished(Scene):
    def enter(self):
        print('You Won! GOod Job!')
        return 'finished'

class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armor': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
