import pytest
from alien_attack.scenes.base_scene import Scene

def test_scene_enter_not_implemented(capsys):
    scene = Scene()
    with pytest.raises(SystemExit):
        scene.enter()

    captured = capsys.readouterr()
    assert 'This scene is not configured yet.' in captured.out
    assert 'Subclass it and implement enter().' in captured.out