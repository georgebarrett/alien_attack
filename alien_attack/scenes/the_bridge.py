from .base_scene import Scene
from textwrap import dedent

class TheBridge(Scene):
    
    def enter(self):
        print(dedent("""
            You crawl through the vent shafts for what feels like eternity. 
            You are covered in sweat and stink of fear. After three hours of 
            scrabbling along vents, you reach The Bridge. You blast a vent cover off and then jump down. 
            There, before you, is a metallic alien monstrosity. Its forehead is long and its metallic skin 
            reflects the clinical lights of The Bridge. The alien is eight feet tall and is connected to 
            some sort of organic sack. You realize that this alien is a queen and she is laying eggs. 
            You stand there in horror at the sight of her. Your jaw drops as you see that Earth is not far 
            away. The alien screams and prepares to fight. She detaches herself from her sack, her tail is 
            lashing and her tongue is out. You freeze and can't decide what to do. 
            Do you shoot the alien or run to the control panel to activate the escape pods? You scream.
        """))

        while True:
            action = input("Choose an action (shoot or activate)> ").strip()
            if action == 'shoot':
                return self.shoot()
            elif action == 'activate':
                return self.activate()
            else:
                print('DOES NOT COMPUTE! Try again.')

    def shoot(self):
        print(dedent("""
            You unload your laser gun into the alien queen. Acid sprays all over you. 
            The Queen picks you up with her metallic arms. She looks at you square in the face. 
            She can sense your fear and wants to bask in it. Once she is satisfied she launches her tongue.
        """))
        return 'death'

    def activate(self):
        print(dedent("""
            You fire your laser gun at the fire detectors. Loud noises and flashing lights fill 
            the spaceship. The Queen is disoriented. You sprint to the control panel and activate 
            the escape pods. You begin to run to the pods but then realize that the Queen will also escape.
            You slam the self-destruct button and sprint to the pods.
        """))
        return 'escape_pod'
