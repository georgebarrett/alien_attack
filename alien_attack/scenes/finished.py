from alien_attack.scenes.base_scene import Scene

class Finished(Scene):
    
    def enter(self):
        return {
            "scene": "finished",
            "message": "You made it!"
        }