import pokemon
import item

class Player():
    alive = True
    def __init__(self):
        self.name = "Pokemon Trainer"
        self.poke_list = []
        self.items = []
        self.primary = 0
