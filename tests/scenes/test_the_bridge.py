import pytest
from unittest.mock import patch
from alien_attack.scenes.the_bridge import TheBridge

@pytest.fixture
def the_bridge():
    return TheBridge()

def test_shoot_action(the_bridge, capsys):
    with patch("builtins.input", return_value="shoot"):
        result = the_bridge.enter()
        captured = capsys.readouterr()

        assert "You unload your laser gun into the alien queen" in captured.out
        assert result == 'death'

def test_activate_action(the_bridge, capsys):
    with patch("builtins.input", return_value="activate"):
        result = the_bridge.enter()
        captured = capsys.readouterr()

        assert "You fire your laser gun at the fire detectors" in captured.out
        assert result == 'escape_pod'

def test_invalid_action_then_shoot(the_bridge, capsys):
    with patch("builtins.input", side_effect=["invalid", "shoot"]):
        result = the_bridge.enter()
        captured = capsys.readouterr()

        assert "DOES NOT COMPUTE! Try again." in captured.out
        assert "You unload your laser gun into the alien queen" in captured.out
        assert result == 'death'

def test_invalid_action_then_activate(the_bridge, capsys):
    with patch("builtins.input", side_effect=["invalid", "activate"]):
        result = the_bridge.enter()
        captured = capsys.readouterr()

        assert "DOES NOT COMPUTE! Try again." in captured.out
        assert "You fire your laser gun at the fire detectors" in captured.out
        assert result == 'escape_pod'
