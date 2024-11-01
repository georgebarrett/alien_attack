from alien_attack.scenes.the_bridge import TheBridge

def test_the_bridge_initial_state():
    scene = TheBridge()
    result = scene.enter()
    assert result["scene"] == "the_bridge"
    assert "You crawl through the vent shafts for what feels like eternity" in result["message"]
    assert "choices" in result
    assert result["choices"] == ["shoot", "activate the escape pods"]

def test_the_bridge_shoot_action():
    scene = TheBridge()
    result = scene.enter(action="shoot")
    assert result["scene"] == "death"
    assert "You unload your laser gun into the alien queen" in result["message"]

def test_the_bridge_activate_escape_pods_action():
    scene = TheBridge()
    result = scene.enter(action="activate the escape pods")
    assert result["scene"] == "escape_pod"
    assert "You fire your laser gun at the fire detectors" in result["message"]

def test_the_bridge_invalid_action():
    scene = TheBridge()
    result = scene.enter(action="invalid_action")
    assert result["scene"] == "the_bridge"
    assert result["message"] == "DOES NOT COMPUTE! Try again."
    assert result["choices"] == ["shoot", "activate the escape pods"]