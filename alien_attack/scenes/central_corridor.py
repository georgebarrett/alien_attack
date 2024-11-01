from .base_scene import Scene
from textwrap import dedent

class CentralCorridor(Scene):
    
    def enter(self):
        print(dedent("""
            You hear the sound of your hibernation pod opening and drowsily clamber out. 
            You vomit all over the floor and then start to calibrate with reality. 
            A metallic, slimy egg catches your eye.
            Will you shoot, run, or inspect?
        """))

        action = input('Choose an action (shoot, run, inspect)> ').strip()

        if action == 'shoot':
            return self.shoot()
        elif action == 'run':
            return self.run()
        elif action == 'inspect':
            return self.inspect()
        else:
            print('DOES NOT COMPUTE! Try again.')
            return 'central_corridor'
    
    def shoot(self):
        print(dedent("""
            You fire at the egg, but acid sprays over you. You’re done for.
        """))
        return 'death'

    def run(self):
        print(dedent("""
            You try to run, but the alien catches up to you.
        """))
        return 'death'
    
    def inspect(self):
        print(dedent("""
            You carefully inspect the egg, then head toward the weapon armory.
        """))
        return 'laser_weapon_armory'
