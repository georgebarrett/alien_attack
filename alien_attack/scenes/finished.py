from alien_attack.scenes.base_scene import Scene

class Finished(Scene):
    
    def enter(self):
        print('You survived!')
        return 'finished'
