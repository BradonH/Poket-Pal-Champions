import abilities
class Poke():
    def __init__(self, name, element, hp, atk, defense):
        self.name = name
        self.element = element
        self.max_hp = hp
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.move_set = []
        #this is where we will keep our buffs and debuffs so we can apply them to the pokemon
        self.buff_list = []
        self.debuff_list = []


#gives new atk stat for the pokemon based on what buffs and debuffs the have
    def calc_value_atk(self):
        new_atk = self.atk
        for buffs in self.buff_list:
            if buffs == None:
                continue
            if buffs == "SWRD_DNC":
                new_atk += round((self.atk * 0.18),0)
                self.buff_list.remove(buffs)
            if buffs == "AGLTY":
                new_atk += round((self.atk * 0.1),0)
                self.buff_list.remove(buffs)
            if buffs == "FSTRIN":
                new_atk += round((self.atk * 0.04))
        for debuffs in self.debuff_list:
            if debuffs == None:
                continue
            if debuffs == "DRSY":
                new_atk -= round((self.atk * 0.12),0)
                self.debuff_list.remove(debuffs)
        return new_atk


#gives new defense stat for the pokemon based on what buffs and debuffs the have
    def calc_value_defense(self):
        new_defense = self.defense
        for buffs in self.buff_list:
            if buffs == None:
                continue
            if buffs == "HRDN":
                new_defense += round((self.defense * 0.15),0)
                self.buff_list.remove(buffs)
            if buffs == "FSTRIN":
                new_defense += round((self.defense * 0.04),0)
        return new_defense


#gives new hp stat for the pokemon based on what buffs and debuffs the have
    def calc_value_hp(self):
        new_hp = self.hp
        for debuffs in self.debuff_list:
            if debuffs == None:
                continue
            if debuffs == "POSN":
                new_hp -= round((self.base_hp * 0.10),0)
            elif debuffs == "BURN":
                new_hp -= round((self.base_hp * 0.07),0)
        return new_hp

