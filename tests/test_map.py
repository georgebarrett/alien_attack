import pytest
from alien_attack.map import Map
from alien_attack.scenes.central_corridor import CentralCorridor
from alien_attack.scenes.death import Death
from alien_attack.scenes.escape_pod import EscapePod
from alien_attack.scenes.finished import Finished
from alien_attack.scenes.laser_weapon_armory import LaserWeaponArmory
from alien_attack.scenes.the_bridge import TheBridge

@pytest.fixture
def map_instance():
    return Map("central_corridor")

def test_opening_scene(map_instance):
    opening_scene = map_instance.opening_scene()
    assert isinstance(opening_scene, CentralCorridor), "Opening scene should be CentralCorridor"

def test_next_scene(map_instance):
    assert isinstance(map_instance.next_scene("central_corridor"), CentralCorridor), "Should return CentralCorridor instance"
    assert isinstance(map_instance.next_scene("laser_weapon_armory"), LaserWeaponArmory), "Should return LaserWeaponArmory instance"
    assert isinstance(map_instance.next_scene("the_bridge"), TheBridge), "Should return TheBridge instance"
    assert isinstance(map_instance.next_scene("escape_pod"), EscapePod), "Should return EscapePod instance"
    assert isinstance(map_instance.next_scene("death"), Death), "Should return Death instance"
    assert isinstance(map_instance.next_scene("finished"), Finished), "Should return Finished instance"

def test_invalid_scene_name(map_instance):
    assert map_instance.next_scene("nonexistent_scene") is None, "Should return None for invalid scene names"
