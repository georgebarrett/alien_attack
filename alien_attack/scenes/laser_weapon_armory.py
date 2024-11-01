from random import randint
from .base_scene import Scene
from textwrap import dedent

class LaserWeaponArmory(Scene):
    def __init__(self):
        self.armory_code = f"{randint(1, 5)}{randint(1, 5)}{randint(1, 5)}"

    def enter(self):
        print(dedent("""
            You dive roll into the Laser Armory. Dripping in sweat and drowning in adrenaline, 
            you quickly close and lock all the doors. You reach the last door, and it is jammed.
            A code needs to be entered into the door's keypad to force it shut.
            You have ten attempts to close the door. The code is three digits long.
        """))

        max_attempts = 10
        guesses = 0
        current_guess = ['_'] * len(self.armory_code)

        while guesses < max_attempts:
            print(f"Current guess: {''.join(current_guess)}")
            guess = input("Enter your 3-digit guess: ")

            if len(guess) != len(self.armory_code) or not guess.isdigit():
                print("Invalid input! Enter exactly three digits.")
                continue

            correct_guess = False

            for i in range(len(self.armory_code)):
                if current_guess[i] == '_' and guess[i] == self.armory_code[i]:
                    current_guess[i] = guess[i]
                    correct_guess = True

            if ''.join(current_guess) == self.armory_code:
                print(dedent("""
                    The door slams shut and a millisecond later the facehugger smashes against the reinforced glass.
                    You sit in a corner of the armory, rocking back and forth. It dawns on you that you need to reach
                    The Bridge and activate the escape pods. You blast open a vent cover and start crawling toward The Bridge.
                    Hold on... If I can fit up here, so can that alien. Don't think, MOVE.
                """))
                return 'the_bridge'

            guesses += 1
            if not correct_guess:
                print("BZZZZZEDDDDDD! Incorrect code.")

        print(dedent("""
            You entered the code for the last time. The door is fixed open.
            The facehugger scuttles into the armory. You unload your laser gun but can't hit the sporadic target.
            The facehugger leaps up. You feel its legs wrap around your face, its tail tighten around your neck,
            and then an alien tube enters your mouth. Later, while making tea, you feel in your chest that something is wrong.
        """))
        return 'death'
