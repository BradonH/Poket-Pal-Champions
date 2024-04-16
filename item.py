class Item():
    def __init__(self, name, heal, buff, debuff):
        self.name = name
        self.heal = heal
        #these were buff_list and debuff_list and were stored as lists but that seemed unneccesary as one item likely wont going to have a list of affects, liekly just one effect
        self.buff = buff
        self.debuff = debuff
