from sys import exit
from random import randint
from textwrap import dedent

#Basics classes to start game and make scenes
class Scene(object):

    def enter(self):
        print('Scene has not been completed')
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('end')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

#The game runner that will reference all of the above scenes.
class Map(object):

    scenes = {
        'wagon': WagonRide(),
        'training': TrainginGround(),
        'whiterun': Whiterun(),
        'bandits': BanditFight(),
        'dragon': DragonFight(),
        'death': Death(),
        'end': End(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self, start_scene):
        return self.next_scene(self.start_scene)
