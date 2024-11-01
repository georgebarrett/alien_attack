from alien_attack.scenes.laser_weapon_armory import LaserWeaponArmory

def test_laser_weapon_armory_initial_state():
    scene = LaserWeaponArmory()
    result = scene.enter()
    assert result["scene"] == "laser_weapon_armory"
    assert "You dive roll into the Laser Armory" in result["message"]
    assert "Enter the code:" in result["prompt"]
    assert result["attempts_remaining"] == scene.attempts_remaining
    assert result["code_feedback"] == []

def test_laser_weapon_armory_correct_code(monkeypatch):
    scene = LaserWeaponArmory()
    monkeypatch.setattr(scene, "armory_code", "123")
    result = scene.enter(guess="123")
    assert result["scene"] == "the_bridge"
    assert "The door slams shut" in result["message"]

def test_laser_weapon_armory_incorrect_code(monkeypatch):
    scene = LaserWeaponArmory()
    monkeypatch.setattr(scene, "armory_code", "123")
    result = scene.enter(guess="999")
    assert result["scene"] == "laser_weapon_armory"
    assert "BZZZZZEDDDDDD! The code is incorrect." in result["message"]
    assert result["attempts_remaining"] == 9

def test_laser_weapon_armory_run_out_of_attempts(monkeypatch):
    scene = LaserWeaponArmory()
    monkeypatch.setattr(scene, "armory_code", "123")
    scene.attempts_remaining = 1  # Set attempts to 1 for quick test
    result = scene.enter(guess="999")
    assert result["scene"] == "death"
    assert "You entered the code for the last time" in result["message"]
