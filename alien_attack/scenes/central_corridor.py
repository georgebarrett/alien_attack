from alien_attack.scenes.base_scene import Scene
class CentralCorridor(Scene):
    
    def enter(self, action=None):
        if action is None:
            return {
                "scene": "central_corridor",
                "message": "You hear the sound of your hibernation pod opening and drowsily clamber out. You vomit all over the floor and then start to callibrate with reality. A scan of the ship is necessary to make sure that everything is in order and that the cargo is safe. You enter into the cargo room, relieved to finally be off the mining planet 31-XCT. Something catches your eye. You rub your eyes to make sure you aren't hallucinating. A metalic slimy egg is in the corner of the bay. You walk over to inspect the anomaly. As you get closer, you see something move inside. You pull out your laser gun and approach with caution. When you reach the mysterious egg, the top begins to fold open.",
                "choices": ["shoot", "run", "inspect"]
            }

        if action == 'shoot':
            return {
                "scene": "death",
                "message": "You run over to the egg and fire your laser gun at the creature inside. When the laser hits the alien, acid sprays all over your head. You scream and writhe around on the floor before turning into a headless corspe."
            }

        elif action == 'run':
            return {
                "scene": "death",
                "message": "Fear takes over and you sprint out of the cargo bay. You run to where your crew are still in hibernation and try to wake them up. As you approach their pods, you see that all of your crew mates have spider like aliens wrapped around their faces. You stagger back in shock. What was that... you turn around and the facehugger leaps onto you. You feel its legs wrap around your head, tail tighten around your neck and then an alien tube enters your mouth. You pass out."
            }

        elif action == 'inspect':
            return {
                "scene": "laser_weapon_armory",
                "message": "You keep edging towards the slimy metalic egg. You peer inside the egg, laser gun shaking in your hand. You see a spider like alien begin to emerge from the egg. It's time to think fast. Where can you hide and stay safe. You remember the Lasor Amory can be totally sealed off and begin sprinting towards it"
            }

        else:
            return {
                "scene": "central_corridor",
                "message": "DOES NOT COMPUTE! Try again.",
                "choices": ["shoot", "run", "inspect"]
            }