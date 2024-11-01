from random import randint
from .base_scene import Scene
from textwrap import dedent

class EscapePod(Scene):

    def enter(self):
        print(dedent("""
            You rush through the ship desperately trying to make it to the escape pod
            before the whole ship explodes or the Queen tears you apart. You reach the pods but can't
            remember which one you activated. Which one will you choose? You only have time to pick one.
            The Queen is rampaging towards you.
            """))

        good_pod = randint(1, 3)
        
        while True:
            guess = input('You have one chance. [pod#] (1, 2 or 3)> ')
            
            try:
                if int(guess) == good_pod:
                    print(dedent(f"""
                        You jump into pod {guess} and hit the eject button. 
                        The pod easily slides out into space heading to Earth. 
                        As it flies to our home planet, you look back and see your ship implode 
                        and then explode like a bright star. You breathe deeply and your body turns to jelly.
                        You survived. WHAT... you look out of the window and see another escape pod heading to earth. 
                        You check the computer system and an alien life form is detected in the other pod. 
                        Over the next twenty years humanity will be eradicated.
                    """))
                    return 'finished'
                else:
                    print(dedent(f"""
                        You jump into pod {guess} and hit the eject button. Nothing happens. 
                        The Queen reaches you, and you pass out from fear. You come around and are plastered to a wall with an unknown alien goo. 
                        You can't move, and no one can hear you scream. You look down and see an egg slowly open. The facehugger knows its prey is helpless.
                        It slowly crawls out of the egg and up your body. You feel its legs wrap around your face, tail tighten around your neck, and a slimy alien tube enter your mouth.
                    """))
                    return 'death'
            except ValueError:
                print("DOES NOT COMPUTE! Please enter a valid pod number.")
