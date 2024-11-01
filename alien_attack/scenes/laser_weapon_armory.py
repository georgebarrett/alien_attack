from random import randint
from .base_scene import Scene

class LaserWeaponArmory(Scene):
    def __init__(self):
        super().__init__()
        self.armory_code = f'{randint(1, 9)}{randint(1, 9)}{randint(1, 9)}'
        self.attempts_remaining = 10

    def enter(self, guess=None):
        if guess is None:
            return {
                "scene": "laser_weapon_armory",
                "message": "You dive roll into the Laser Armory. Dripping in sweat and drowning in adrenaline, "
                           "you quickly close and lock all the doors. You reach the last door, and it is jammed. "
                           "A code needs to be entered into the door's keypad to force it shut. "
                           "You have ten attempts to close the door. The code is three digits long and the keypad range is 1-9.",
                "prompt": "Enter the code:",
                "attempts_remaining": self.attempts_remaining,
                "code_feedback": []
            }

        feedback = []
        for i in range(len(guess)):
            if i < len(self.armory_code):
                correct = guess[i] == self.armory_code[i]
                feedback.append({'digit': guess[i], 'correct': correct})
            else:
                feedback.append({'digit': '', 'correct': False})

        if guess == self.armory_code:
            return {
                "scene": "the_bridge",
                "message": "The door slams shut and a millisecond later the facehugger smashes against the reinforced glass. "
                           "You sit in a corner of the armory, rocking back and forth. It dawns on you that you need to reach "
                           "The Bridge and activate the escape pods. You blast open a vent cover and start crawling toward The Bridge. "
                           "Hold on... If I can fit up here, so can that alien. Don't think, MOVE."
            }
        else:
            self.attempts_remaining -= 1
            if self.attempts_remaining > 0:
                return {
                    "scene": "laser_weapon_armory",
                    "message": "BZZZZZEDDDDDD! The code is incorrect.",
                    "prompt": "Enter the code:",
                    "attempts_remaining": self.attempts_remaining,
                    "code_feedback": feedback
                }
            else:
                return {
                    "scene": "death",
                    "message": "You entered the code for the last time. The door is fixed open. "
                               "The facehugger scuttles into the armory. You unload your laser gun but can't hit the sporadic target. "
                               "The facehugger leaps up. You feel its legs wrap around your face, its tail tighten around your neck, "
                               "and then an alien tube enters your mouth. Later, while making tea, you hear the first crunch of your chest bones breaking."
                }
