import abilities
#import item
import pokemon
import player
import time
import random

#items do not work yet and each player only has one pokemon in each battle

#create functions
def play_start(current_turn):
    print()
    print(f"It is currently {current_turn.name}'s turn")
    print()
    print("Please input id number of action wanted")
    print("""1.Attack          2.Items (unavaliable)
          3.Swap Pokemon (unavalible)""")
    selection = int(input())
    if selection == 1:
        attack()
    else:
        print("input not defined please input an avaliable id number")
        play_start()


def attack():
    print()
    print("Please input id number of attack wanted")
    print(f"""1.{current_turn.poke_list[current_turn.primary].move_set[0].name}          2.{current_turn.poke_list[current_turn.primary].move_set[1].name}
3.{current_turn.poke_list[current_turn.primary].move_set[2].name}           4.{current_turn.poke_list[current_turn.primary].move_set[3].name}
5. Return to action selection menu""")
    print()
    selection = int(input())
    #HERES THE PROBLEM
    if selection != 1 and selection != 2 and selection != 3 and selection != 4:
        if selection == 5:
            play_start()
        else:
            print("please select an available id")
            attack()
    else:
        dmg = current_turn.poke_list[current_turn.primary].move_set[int(selection-1)].damage
        acy = current_turn.poke_list[current_turn.primary].move_set[int(selection-1)].accuracy
        buf = current_turn.poke_list[current_turn.primary].move_set[int(selection-1)].buff
        dbf = current_turn.poke_list[current_turn.primary].move_set[int(selection-1)].debuff
        if current_turn == play_1:
            opp = play_2
        else:
            opp = play_1
        if random.randint(0,100) < acy:
            coefficient = (1 + (int(current_turn.poke_list[current_turn.primary].atk))/100)
            def_coefficient = (1 + (int(current_turn.poke_list[current_turn.primary].defense))/100)
            opp.poke_list[opp.primary].hp -= (dmg * coefficient)/def_coefficient
            opp.poke_list[opp.primary].debuff.append(dbf)
            current_turn.poke_list[current_turn.primary].buff.append(buf)
            if opp.poke_list[opp.primary].hp <= 0:
                opp.alive = False
                pass
            else:
                pass
        else:
            print("The attack missed!")




def play_swap(current_turn):
    if current_turn == play_1:
        return play_2
    else:
        return play_1




#create pokemon objects
charmander = pokemon.Poke("Charmander", "Fire", 45, 53, 45)

squirtle = pokemon.Poke("Squirtle", "Water", 50, 48, 65)

#bulbasaur = pokemon.Poke("Bulbasuar", "Grass", 50, 50, 50)

#pikachu = pokemon.Poke("Pikachu", "Electric", 40, 65, 40)

#snorlax = pokemon.Poke("Snorlax", "Normal", 85, 30, 45)

#magikarp = pokemon.Poke("Magikarp", "Water", 60, 20, 50)

poke_dict = {1: charmander,
             2: squirtle}
#create abilities object
#Normal
tackle = abilities.Abilities(20, 95, None, None, "tackle")
bite = abilities.Abilities(30, 75, None, None, "bite")
slash = abilities.Abilities(25, 85, None, None, "slash")
slam = abilities.Abilities(35, 70, None, None, "slam")
bash = abilities.Abilities(25, 80, None, None, "bash")

#buffs
sword_dance = abilities.Abilities(0, 100, "SWRD_DNC", None, "sword dance")
harden = abilities.Abilities(0, 100, None, "HRDN", "harden")

#Debuffs
poison = abilities.Abilities(0, 100, None, "POSN", "poison")
drowsy = abilities.Abilities(0, 100, None, "DRSY", "drowsy")

#specials
# thunderbolt
# water_jet
vine_whip = abilities.Abilities(25, 90, None, None, "vine whip")
ember = abilities.Abilities(25, 85, None, "BURN", "ember")

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

play_1.name = input("Player 1 please enter your name: ")

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
print("To continue hit enter...")

input()

print(f"{play_1.name}, please select a pokemon, the first pokemon selected will be your primary pokemon (enter id number of pokemon wanted)")
print()
count = 0
#print list of pokemon that are available for selection
for i in poke_dict:
    count += 1
    print(f"{count}. {str(poke_dict[count].name)}, press {count} to select this pokemon")

play_1.poke_list.append(poke_dict[int(input("Please enter desired Pokemon: "))])
print(f"{play_2.name}, please select a pokemon, the first pokemon selected will be your primary pokemon (enter id number of pokemon wanted)")
print()
count = 0
for i in poke_dict:
    count += 1
    print(f"{count}. {str(poke_dict[count].name)}, press {count} to select this pokemon")

play_2.poke_list.append(poke_dict[int(input("Please enter desired Pokemon: "))])

current_turn = play_1

print()
print("The contests have chosen and the stage is set may, the best contestant win!")
time.sleep(3)


while play_1.alive == True and play_2.alive == True:
    play_start(current_turn)
    current_turn = play_swap(current_turn)

print()
print("We have a winner!")
time.sleep(3)
if play_1.alive == True:
    print(f"Congratulations {play_1.name}, you are the pokemon champion!")
else:
    print(f"Congratulations {play_2.name}, you are the pokemon champion!")
time.sleep(2)
print("Thank you for playing Poket-Pal Champions, we hope to better this game and add more customization and polish to it in the near future!")

