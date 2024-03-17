import abilities
import random
class Poke():
    def __init__(self, name, element, hp, atk, defense):
        self.name = name
        self.element = element
        self.hp = hp
        self.atk = atk
        self.defense = defense
        #self.P = P
        #P stands for Power Points, essentially the stamina a pokemon has
        #it usually knows as PP but to avoid that we'll just call it P
        #on second thought we wont use P
        self.move_set = []
        self.buff = []
        self.debuff = []
        #this is where we will keep our buffs and debuffs so we can apply them to the pokemon

    #def attacks(self): idk if this should be here
        

    #def swap_pokemon(self): this is here just incase
    #Fire Water Grass Electric Water Normal
    # def moves(self):
        # if self.element == "Normal":
