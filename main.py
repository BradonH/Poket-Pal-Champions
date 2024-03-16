import abilities
import item
import pokemon
import player
import time

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
print()
print("Welcome to...")
time.sleep(1)
print(
"""
░█▀█░█▀█░█░█░█▀▀░▀█▀░░░░░█▀█░█▀█░█░░░░░█▀▀░█░█░█▀█░█▄█░█▀█░▀█▀░█▀█░█▀█░█▀▀
░█▀▀░█░█░█▀▄░█▀▀░░█░░▄▄▄░█▀▀░█▀█░█░░░░░█░░░█▀█░█▀█░█░█░█▀▀░░█░░█░█░█░█░▀▀█
░▀░░░▀▀▀░▀░▀░▀▀▀░░▀░░░░░░▀░░░▀░▀░▀▀▀░░░▀▀▀░▀░▀░▀░▀░▀░▀░▀░░░▀▀▀░▀▀▀░▀░▀░▀▀▀
""")
time.sleep(3)

#create player object
play_1 = player.Player()
play_2 = player.Player()

play_1.name = input("Player 1 please enter your name: ")
time.sleep(1)

play_2.name = input("Player 2 please enter your name: ")
print()
time.sleep(1)

print("Welcome", play_1.name, "and", play_2.name + "!!")
print(
"""
⠸⣷⣦⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⠀⠀⠀
⠀⠙⣿⡄⠈⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠔⠊⠉⣿⡿⠁⠀⠀⠀
⠀⠀⠈⠣⡀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠁⠀⠀⣰⠟⠀⠀⠀⣀⣀
⠀⠀⠀⠀⠈⠢⣄⠀⡈⠒⠊⠉⠁⠀⠈⠉⠑⠚⠀⠀⣀⠔⢊⣠⠤⠒⠊⠉⠀⡜
⠀⠀⠀⠀⠀⠀⠀⡽⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠩⡔⠊⠁⠀⠀⠀⠀⠀⠀⠇
⠀⠀⠀⠀⠀⠀⠀⡇⢠⡤⢄⠀⠀⠀⠀⠀⡠⢤⣄⠀⡇⠀⠀⠀⠀⠀⠀⠀⢰⠀
⠀⠀⠀⠀⠀⠀⢀⠇⠹⠿⠟⠀⠀⠤⠀⠀⠻⠿⠟⠀⣇⠀⠀⡀⠠⠄⠒⠊⠁⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⡆⠀⠰⠤⠖⠦⠴⠀⢀⣶⣿⣿⠀⠙⢄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢻⣿⠃⠀⠀⠀⠀⠀⠀⠀⠈⠿⡿⠛⢄⠀⠀⠱⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⠈⠓⠦⠀⣀⣀⣀⠀⡠⠴⠊⠹⡞⣁⠤⠒⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⠃⠀⠀⠀⠀⡌⠉⠉⡤⠀⠀⠀⠀⢻⠿⠆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠰⠁⡀⠀⠀⠀⠀⢸⠀⢰⠃⠀⠀⠀⢠⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢶⣗⠧⡀⢳⠀⠀⠀⠀⢸⣀⣸⠀⠀⠀⢀⡜⠀⣸⢤⣶⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠻⣿⣦⣈⣧⡀⠀⠀⢸⣿⣿⠀⠀⢀⣼⡀⣨⣿⡿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠻⠿⠿⠓⠄⠤⠘⠉⠙⠤⢀⠾⠿⣿⠟⠋
"""
)
time.sleep(3)
print()
print("Greetings, fellow trainers! Welcome to the arena of Poket-Pal Champions, where epic battles await.")
print("In this thrilling two-player showdown, each trainer will carefully choose thier Pokemon and strategically aquire items from the shop. These formidable creatures will clash in epic battles until one succums to defeat by fainting.")
print("In the heat of battle, players will have the option to strategically swap Pokemon (available in future versions) and employ items for tatical advantage (also forthcoming). Once all of a player's Pokemon are exhausted, victory will be claimed by the remaining trainer!!")
print()