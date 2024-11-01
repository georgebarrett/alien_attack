from alien_attack.scenes.central_corridor import CentralCorridor

def test_central_corridor_initial_state():
    scene = CentralCorridor()
    result = scene.enter()
    assert result["scene"] == "central_corridor"
    assert "You hear the sound of your hibernation pod opening" in result["message"]
    assert "choices" in result
    assert result["choices"] == ["shoot", "run", "inspect"]

def test_central_corridor_shoot_action():
    scene = CentralCorridor()
    result = scene.enter(action="shoot")
    assert result["scene"] == "death"
    assert "You run over to the egg and fire your laser gun" in result["message"]

def test_central_corridor_run_action():
    scene = CentralCorridor()
    result = scene.enter(action="run")
    assert result["scene"] == "death"
    assert "Fear takes over and you sprint out of the cargo bay" in result["message"]

def test_central_corridor_inspect_action():
    scene = CentralCorridor()
    result = scene.enter(action="inspect")
    assert result["scene"] == "laser_weapon_armory"
    assert "You keep edging towards the slimy metalic egg" in result["message"]

def test_central_corridor_invalid_action():
    scene = CentralCorridor()
    result = scene.enter(action="invalid_action")
    assert result["scene"] == "central_corridor"
    assert result["message"] == "DOES NOT COMPUTE! Try again."
    assert result["choices"] == ["shoot", "run", "inspect"]