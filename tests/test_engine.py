import pytest
from unittest.mock import MagicMock
from alien_attack.engine import Engine
from alien_attack.scenes.finished import Finished
from alien_attack.scenes.death import Death

def test_engine_stops_on_death(capsys):
    mock_map = MagicMock()
    central_corridor = MagicMock(enter=MagicMock(return_value='death'))
    death_scene = Death()
    
    mock_map.opening_scene.return_value = central_corridor
    mock_map.next_scene.side_effect = lambda name: {
        'central_corridor': central_corridor,
        'death': death_scene,
        'finished': Finished()
    }[name]

    engine = Engine(mock_map)
    with pytest.raises(SystemExit):
        engine.play()

    captured = capsys.readouterr()
    assert any(quip in captured.out for quip in Death.quips), "The output should contain a death message."
