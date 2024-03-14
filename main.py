import abilities
import item
import pokemon
import player

#create pokemon objects
charmander = pokemon.Poke("Charmander", "Fire", 45, 53, 45)

squirtle = pokemon.Poke("Squirtle", "Water", 50, 48, 65)

#bulbasaur = pokemon.Poke("Bulbasuar", "Grass", 50, 50, 50)

#pikachu = pokemon.Poke("Pikachu", "Electric", 40, 65, 40)

#snorlax = pokemon.Poke("Snorlax", "Normal", 85, 30, 45)

#magikarp = pokemon.Poke("Magikarp", "Water", 60, 20, 50)

#create abilities object
#Normal
tackle = abilities.Abilities(20, 95, None, None)
bite = abilities.Abilities(30, 75, None, None)
slash = abilities.Abilities(25, 85, None, None)
slam = abilities.Abilities(35, 70, None, None)
bash = abilities.Abilities(25, 80, None, None)

#buffs
sword_dance = abilities.Abilities(0, 100, "SWRD_DNC", None)
harden = abilities.Abilities(0, 100, None, "HRDN")

#Debuffs
poison = abilities.Abilities(0, 100, None, "POSN")
drowsy = abilities.Abilities(0, 100, None, "DRSY")

#specials
# thunderbolt
# water_jet
vine_whip = abilities.Abilities(25, 90, None, None)
ember = abilities.Abilities(25, 85, None, "BURN")

#append
charmander.move_set.append(tackle)
charmander.move_set.append(bite)
charmander.move_set.append(sword_dance)
charmander.move_set.append(ember)

squirtle.move_set.append(bite)
squirtle.move_set.append(bash)
squirtle.move_set.append(poison)
squirtle.move_set.append(vine_whip)


#create item object
# moo_moo_milk
# cure

#create player object
play_1 = player.Player()
play_2 = player.Player()

play_1.name = input("WELCOME TO POKET PAL CHAMPIONS please input name: ")

print(play_1.name)