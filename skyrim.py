
#Basics classes to start game and make scenes
class Scene(object):

    def enter(self):
        print('Scene has not been completed')
        exit(1)

class WagonRide(Scene):

    def enter(self):
        print('WagonScene')
        return 'training'

class TraingingGround(Scene):

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

    def enter(self):
        print('Death')
        exit(1)

class End(Scene):

    def enter(self):
        print('End')
        return 'end'
