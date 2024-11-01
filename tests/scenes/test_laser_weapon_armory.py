import pytest
from unittest.mock import patch
from alien_attack.scenes.laser_weapon_armory import LaserWeaponArmory

@pytest.fixture
def laser_weapon_armory():
    armory = LaserWeaponArmory()
    armory.armory_code = "123"
    return armory

def test_correct_code(laser_weapon_armory, capsys):
    with patch("builtins.input", side_effect=["123"]):
        result = laser_weapon_armory.enter()
        captured = capsys.readouterr()
        
        assert "The door slams shut and a millisecond later" in captured.out
        assert result == 'the_bridge'

def test_incorrect_code_all_attempts(laser_weapon_armory, capsys):
    with patch("builtins.input", side_effect=["000"] * 10):
        result = laser_weapon_armory.enter()
        captured = capsys.readouterr()

        assert "BZZZZZEDDDDDD! Incorrect code." in captured.out
        assert "You entered the code for the last time." in captured.out
        assert result == 'death'

def test_partial_correct_code(laser_weapon_armory, capsys):
    with patch("builtins.input", side_effect=["100", "120", "123"]):
        result = laser_weapon_armory.enter()
        captured = capsys.readouterr()

        assert "Current guess: 1__" in captured.out
        assert "Current guess: 12_" in captured.out
        assert "The door slams shut and a millisecond later" in captured.out
        assert result == 'the_bridge'

def test_invalid_input_handling(laser_weapon_armory, capsys):
    with patch("builtins.input", side_effect=["12", "abc", "123"]):
        result = laser_weapon_armory.enter()
        captured = capsys.readouterr()

        assert "Invalid input! Enter exactly three digits." in captured.out
        assert "The door slams shut and a millisecond later" in captured.out
        assert result == 'the_bridge'
