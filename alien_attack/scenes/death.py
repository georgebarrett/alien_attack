from random import randint
from .base_scene import Scene

class Death(Scene):
    quips = [
        'GAME OVER \n',
        'THE ALIEN HAS GOT YOU \n',
        'YOU HAVE DIED \n'
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips) - 1)])
        raise SystemExit
