import pytest
from alien_attack.scenes.death import Death
import re

def test_death_quip(monkeypatch, capsys):
    monkeypatch.setattr("alien_attack.scenes.death.randint", lambda x, y: 0)
    scene = Death()
    
    with pytest.raises(SystemExit):
        scene.enter()
    
    captured = capsys.readouterr()
    assert re.search(r'Look what you have done', captured.out) 