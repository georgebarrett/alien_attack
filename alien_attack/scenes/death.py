from random import randint
from .base_scene import Scene

class Death(Scene):
    quips = [
        'Look what you have done \n',
        'You have gone and got yourself dead \n',
        'Who is going to pay the extortionate energy bills now \n'
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips) - 1)])
        exit(1)