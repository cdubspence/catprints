from sys import exit
from random import randint
from textwrap import dedent
import skyrim

#game runner. taking scene_map as a Map() object argument
# play() sets current_scene as a map object and calls opening_scene
# and next_scene.
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('end')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        #print out last scene
        current_scene.enter()

#Contains a dict of scenes defined in skyrim.py and we give it the starting
# scene as an argument. next_scene() returns the class assigned in the dict
class Map(object):

    scenes = {
        'wagon': skyrim.WagonRide(),
        'training': skyrim.TraingingGround(),
        'whiterun': skyrim.Whiterun(),
        'bandits': skyrim.BanditFight(),
        'dragon': skyrim.DragonFight(),
        'death': skyrim.Death(),
        'end': skyrim.End(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('wagon')
a_game = Engine(a_map)
a_game.play()
