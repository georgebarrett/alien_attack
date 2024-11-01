from alien_attack.engine import Engine
from alien_attack.map import Map

if __name__ == "__main__":
    game_map = Map('central_corridor')
    game_engine = Engine(game_map)
    game_engine.play()
