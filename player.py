import pokemon
import item

class Player():
    alive = True
    def __init__(self):
        self.name = "Pokemon Trainer"
        self.poke_list = []
        self.items = []
        self.primary = 0

    #def swap_pokemon(self): use this to update the number of the primary pokemon
    def use_item(self, index):
        if len(self.items) < index or type(index) != "int":
            print("that is not a usable item!")
            