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
    
    monkeypatch.setattr("alien_attack.scenes.central_corridor.CentralCorridor.enter", lambda x: 'finished')
    monkeypatch.setattr("alien_attack.scenes.finished.Finished.enter", lambda x: "finished")

    engine.play()

    assert isinstance(game_map.next_scene('finished'), Finished)
