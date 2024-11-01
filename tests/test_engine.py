import pytest
from alien_attack.engine import Engine
from alien_attack.map import Map
from alien_attack.scenes.finished import Finished
from alien_attack.scenes.central_corridor import CentralCorridor

def test_engine_initialization():
    game_map = Map('central_corridor')
    engine = Engine(game_map)
    assert engine.scene_map == game_map

def test_engine_play(monkeypatch):
    game_map = Map('central_corridor')
    engine = Engine(game_map)

    monkeypatch.setattr("alien_attack.scenes.central_corridor.CentralCorridor.enter", lambda x=None, action=None: {"scene": "finished", "message": "You made it!"})
    monkeypatch.setattr("alien_attack.scenes.finished.Finished.enter", lambda x=None, action=None: {"scene": "finished", "message": "You made it!"})

    monkeypatch.setattr("builtins.input", lambda _: "inspect")
    
    engine.play()

    assert isinstance(game_map.next_scene("finished"), Finished)

def test_engine_play_multiple_scenes(monkeypatch):
    game_map = Map('central_corridor')
    engine = Engine(game_map)

    monkeypatch.setattr("alien_attack.scenes.central_corridor.CentralCorridor.enter", lambda x=None, action=None: {"scene": "laser_weapon_armory", "message": "You proceed to the weapon armory."})
    monkeypatch.setattr("alien_attack.scenes.laser_weapon_armory.LaserWeaponArmory.enter", lambda x=None, action=None: {"scene": "the_bridge", "message": "You reach the bridge."})
    monkeypatch.setattr("alien_attack.scenes.the_bridge.TheBridge.enter", lambda x=None, action=None: {"scene": "escape_pod", "message": "You get to the escape pod."})
    monkeypatch.setattr("alien_attack.scenes.escape_pod.EscapePod.enter", lambda x=None, action=None: {"scene": "finished", "message": "You made it!"})
    monkeypatch.setattr("alien_attack.scenes.finished.Finished.enter", lambda x=None, action=None: {"scene": "finished", "message": "You made it!"})

    monkeypatch.setattr("builtins.input", lambda _: "inspect")

    engine.play()

    assert isinstance(game_map.next_scene("finished"), Finished)
