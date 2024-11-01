from alien_attack.scenes.central_corridor import CentralCorridor

def test_central_corridor_shoot_action():
    scene = CentralCorridor()
    result = scene.enter(action="shoot")
    assert result["scene"] == "death"
    assert "You fire at the egg, but acid sprays over you. You’re done for." in result["message"]

def test_central_corridor_run_action():
    scene = CentralCorridor()
    result = scene.enter(action="run")
    assert result["scene"] == "death"
    assert "You try to run, but the alien catches up to you." in result["message"]

def test_central_corridor_inspect_action():
    scene = CentralCorridor()
    result = scene.enter(action="inspect")
    assert result["scene"] == "laser_weapon_armory"
    assert "You carefully inspect the egg, then head toward the weapon armory." in result["message"]
