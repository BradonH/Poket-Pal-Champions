

class Poke():
    def __init__(self, name, element, hp, atk, defense, P):
        self.name = name
        self.element = element
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.P = P
        #P stands for Power Points, essentially the stamina a pokemon has
        #it usually knows as PP but to avoid that we'll just call it P
        self.move_set = []
        self.buff_debuff = []
        #this is where we will keep our buffs or debuffs so we can apply them to the pokemon

    def attacks(self):
        pass

    #def swap_pokemon(self): this is here just incase