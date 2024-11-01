import pytest
from unittest.mock import patch
from alien_attack.scenes.escape_pod import EscapePod

@pytest.fixture
def escape_pod():
    return EscapePod()

def test_correct_pod_choice(escape_pod, capsys):
    with patch("alien_attack.scenes.escape_pod.randint", return_value=1):
        with patch("builtins.input", return_value="1"):
            result = escape_pod.enter()
            captured = capsys.readouterr()

            assert "You jump into pod 1 and hit the eject button." in captured.out
            assert "The pod easily slides out into space heading to Earth" in captured.out
            assert result == 'finished'

def test_incorrect_pod_choice(escape_pod, capsys):
    with patch("alien_attack.scenes.escape_pod.randint", return_value=1):
        with patch("builtins.input", return_value="2"):
            result = escape_pod.enter()
            captured = capsys.readouterr()
            
            assert "You jump into pod 2 and hit the eject button. Nothing happens." in captured.out
            assert "The Queen reaches you, and you pass out from fear." in captured.out
            assert result == 'death'

def test_invalid_input_then_correct_choice(escape_pod, capsys):
    with patch("alien_attack.scenes.escape_pod.randint", return_value=1):
        with patch("builtins.input", side_effect=["invalid", "1"]):
            result = escape_pod.enter()
            captured = capsys.readouterr()
            
            assert "DOES NOT COMPUTE! Please enter a valid pod number." in captured.out
            assert "You jump into pod 1 and hit the eject button." in captured.out
            assert result == 'finished'

def test_invalid_input_then_incorrect_choice(escape_pod, capsys):
    with patch("alien_attack.scenes.escape_pod.randint", return_value=1):
        with patch("builtins.input", side_effect=["invalid", "2"]):
            result = escape_pod.enter()
            captured = capsys.readouterr()
            
            assert "DOES NOT COMPUTE! Please enter a valid pod number." in captured.out
            assert "You jump into pod 2 and hit the eject button. Nothing happens." in captured.out
            assert result == 'death'
