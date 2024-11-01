from alien_attack.scenes.base_scene import Scene
class TheBridge(Scene):
    
    def enter(self, action=None):
        if action is None:
            return {
                "scene": "the_bridge",
                "message": "You crawl through the vent shafts for what feels like eternity. You are covered in sweat and stink of fear. After three hours of scrabbling along vents, you reach The Bridge. You blast a vent cover off and then jump down. There, before you, is a metalic alien monstrosity. Its forehead is long and its metalic skin reflects the clinical lights of The Bridge. The alien is eight feet tall and is connected to some sort of organic sack. You realise that this alien is a queen and she is laying eggs. You stand there in horror at the sight of her. Your jaw drops as you see that Earth is not far away. The alien screams and prepares to fight. She detaches herself from her sack, her tail is lashing and her tongue is out. You freeze and can't decide what to do. Do you shoot the alien or run to the control panel to activate the escape pods. You scream.",
                "choices": ["shoot", "activate the escape pods"]
            }

        if action == 'shoot':
            return {
                "scene": "death",
                "message": "You unload your laser gun into the alien queen. Acid sprays all over your body and you can feel it burning through you. The Queen picks you up with her metalic arms. she looks at you sqaure in face. She can sense you fear and wants to bask in it. Once she is satisfied she launches her tongue into your head"
            }

        elif action == 'activate the escape pods':
            return {
                "scene": "escape_pod",
                "message": "You fire your laser gun at the fire detectors. Loud noises and flashing lights fill the spaceship. The Queen is disorientated. You sprint to the control panel and activate the escape pods. You begin to run to the pods but then realise that the Queen will land on Earth. You sprint back and activate the self-destruct sequence"
            }
        else:
            return {
                "scene": "the_bridge",
                "message": "DOES NOT COMPUTE! Try again.",
                "choices": ["shoot", "activate the escape pods"]
            }