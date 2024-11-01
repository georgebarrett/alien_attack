class Engine:
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            scene_data = current_scene.enter()
            print(scene_data["message"])

            if "choices" in scene_data:
                action = input(f"Choose an action {scene_data['choices']}: ")
            else:
                action = None

            scene_data = current_scene.enter(action)
            next_scene_name = scene_data["scene"]
            current_scene = self.scene_map.next_scene(next_scene_name)

        final_scene_data = current_scene.enter()
        print(final_scene_data["message"])
        