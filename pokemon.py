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
        self.buff_list = []
        self.debuff_list = []
        #this is where we will keep our buffs and debuffs so we can apply them to the pokemon


    def calc_value_atk(self):
        new_atk = self.atk
        for buffs in self.buff_list:
            if buffs.buff == "SWRD_DNC":
                new_atk += round((self.atk * 0.15),0)
                self.buff_list.remove(buffs)
        return new_atk

    def calc_value_defense(self):
        new_defense = self.defense
        for buffs in self.buff_list:
            if buffs.buff == "HRDN":
                new_defense += round((self.defense * 0.15),0)
                self.buff_list.remove(buffs)
        return new_defense

    def calc_value_hp(self):
        new_hp = self.hp
        for buffs in self.buff_list:
            if buffs.buff == "POSN":
                new_hp -= round((self.hp * 0.10),0)
            elif buffs.buff == "BURN":
                new_hp -= round((self.hp * 0.07),0)
        return new_hp


    #def attacks(self): idk if this should be here
        

    #def swap_pokemon(self): this is here just incase
    #Fire Water Grass Electric Water Normal
    # def moves(self):
        # if self.element == "Normal":
