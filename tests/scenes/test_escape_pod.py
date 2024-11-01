import pytest
from alien_attack.scenes.escape_pod import EscapePod

def test_escape_pod_initial_state():
    scene = EscapePod()
    result = scene.enter()
    assert result["scene"] == "escape_pod"
    assert "You rush through the ship desperately trying to make it to the escape pod" in result["message"]
    assert "pod_numbers" in result
    assert result["pod_numbers"] == list(range(1, 6))

def test_escape_pod_correct_guess(monkeypatch):
    scene = EscapePod()
    monkeypatch.setattr(scene, "good_pod", 3)
    result = scene.enter(guess="3")
    assert result["scene"] == "finished"
    assert "You jump into pod 3 and hit the eject button" in result["message"]

def test_escape_pod_incorrect_guess(monkeypatch):
    scene = EscapePod()
    monkeypatch.setattr(scene, "good_pod", 3)
    result = scene.enter(guess="2")
    assert result["scene"] == "death"
    assert "You jump into pod 2 and hit the eject button" in result["message"]
