from .base_scene import Scene

class CentralCorridor(Scene):
    
    def enter(self, action=None):
        if action is None:
            return {
                "scene": "central_corridor",
                "message": (
                    "You hear the sound of your hibernation pod opening and drowsily clamber out. "
                    "You vomit all over the floor and then start to calibrate with reality. "
                    "A metallic, slimy egg catches your eye. "
                    "Will you shoot, run, or inspect?"
                ),
                "choices": ["shoot", "run", "inspect"]
            }
        
        if action == 'shoot':
            return {
                "scene": "death",
                "message": "You fire at the egg, but acid sprays over you. You’re done for."
            }
        elif action == 'run':
            return {
                "scene": "death",
                "message": "You try to run, but the alien catches up to you."
            }
        elif action == 'inspect':
            return {
                "scene": "laser_weapon_armory",
                "message": "You carefully inspect the egg, then head toward the weapon armory."
            }
        else:
            return {
                "scene": "central_corridor",
                "message": "DOES NOT COMPUTE! Try again.",
                "choices": ["shoot", "run", "inspect"]
            }
