import pytest
from alien_attack.scenes.finished import Finished

@pytest.fixture
def finished_scene():
    return Finished()

def test_finished_enter_output(finished_scene, capsys):
    result = finished_scene.enter()
    captured = capsys.readouterr()

    assert "You survived!" in captured.out, "Output should contain 'You survived!'"
    assert result == 'finished', "Return value should be 'finished'"
