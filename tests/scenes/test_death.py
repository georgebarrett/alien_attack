import pytest
from unittest.mock import patch
from alien_attack.scenes.death import Death

@pytest.fixture
def death_scene():
    return Death()

def test_enter_outputs_quip(death_scene, capsys):
    with patch("alien_attack.scenes.death.exit", side_effect=SystemExit):
        with pytest.raises(SystemExit):
            death_scene.enter()
        
        captured = capsys.readouterr()
        assert any(quip in captured.out for quip in Death.quips), "Output should contain a quip from the list"

def test_enter_random_quip(death_scene, capsys):
    quip_set = set()
    
    with patch("alien_attack.scenes.death.exit", side_effect=SystemExit):
        for _ in range(10):
            with pytest.raises(SystemExit):
                death_scene.enter()
            captured = capsys.readouterr()
            quip_set.update([quip for quip in Death.quips if quip in captured.out])

    assert len(quip_set) >= 2, "At least two unique quips should appear over multiple runs"
