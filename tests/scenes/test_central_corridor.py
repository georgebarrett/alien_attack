import pytest
from unittest.mock import patch
from alien_attack.scenes.central_corridor import CentralCorridor  # Update with your actual module path

@pytest.fixture
def central_corridor():
    return CentralCorridor()

def test_shoot_action(central_corridor, capsys):
    with patch('builtins.input', return_value='shoot'):
        result = central_corridor.enter()
        captured = capsys.readouterr()
        assert "You fire at the egg, but acid sprays over you. You’re done for." in captured.out
        assert result == 'death'

def test_run_action(central_corridor, capsys):
    with patch('builtins.input', return_value='run'):
        result = central_corridor.enter()
        captured = capsys.readouterr()
        assert "You try to run, but the alien catches up to you." in captured.out
        assert result == 'death'

def test_inspect_action(central_corridor, capsys):
    with patch('builtins.input', return_value='inspect'):
        result = central_corridor.enter()
        captured = capsys.readouterr()
        assert "You carefully inspect the egg, then head toward the weapon armory." in captured.out
        assert result == 'laser_weapon_armory'

def test_invalid_action(central_corridor, capsys):
    with patch('builtins.input', return_value='invalid'):
        result = central_corridor.enter()
        captured = capsys.readouterr()
        assert "DOES NOT COMPUTE! Try again." in captured.out
        assert result == 'central_corridor'
