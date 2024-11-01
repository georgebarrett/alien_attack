from alien_attack.scenes.finished import Finished

def test_finished_scene():
    scene = Finished()
    result = scene.enter()
    assert result["scene"] == "finished"
    assert result["message"] == "You made it!"