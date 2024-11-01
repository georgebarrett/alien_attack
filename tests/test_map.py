from alien_attack.map import Map
from alien_attack.scenes.central_corridor import CentralCorridor
from alien_attack.scenes.death import Death
from alien_attack.scenes.finished import Finished

def test_map_initialization():
    game_map = Map('central_corridor')
    assert game_map.start_scene == 'central_corridor'

def test_map_opening_scene():
    game_map = Map('central_corridor')
    opening_scene = game_map.opening_scene()
    assert isinstance(opening_scene, CentralCorridor)

def test_map_next_scene():
    game_map = Map('central_corridor')
    assert isinstance(game_map.next_scene('death'), Death)
    assert isinstance(game_map.next_scene('finished'), Finished)