from alien_attack.scenes.central_corridor import CentralCorridor
from alien_attack.scenes.death import Death
from alien_attack.scenes.escape_pod import EscapePod
from alien_attack.scenes.finished import Finished
from alien_attack.scenes.laser_weapon_armory import LaserWeaponArmory
from alien_attack.scenes.the_bridge import TheBridge


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    
    def opening_scene(self):
        return self.next_scene(self.start_scene)