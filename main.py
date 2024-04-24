import abilities
import item
import pokemon
import player
import time
import random

#items and buffs now work and multiple pokemon are on each team

#before going through code, yes we know lots of this is badly coded, yes we know some stuff doesnt make sense such as it it redundant 
#or one line in a function might not doing anything. this is due to errors that might have popped up and were fixed, leaving artifacts
#of old code that we were unsure wether getting rid of it wouldve broken the code or not.
#we had some stuff planned that we didnt get to and other stuff not planned that we ended up adding because it made sense at the time.
#ultimately we believe that while the code is a mess we did make a suprisingly decent version of a pokemon battler especially for our skill level
#thats our whole talk though, we had lots of fun and stress doing this
# - Bradon & Jay

#objects are instaciated here

#create pokemon objects
charmander = pokemon.Poke("Charmander", "Fire", 47, 53, 50)
squirtle = pokemon.Poke("Squirtle", "Water", 50, 48, 65)
bulbasaur = pokemon.Poke("Bulbasuar", "Grass", 53, 50, 50)
pikachu = pokemon.Poke("Pikachu", "Electric", 45, 65, 40)
snorlax = pokemon.Poke("Snorlax", "Normal", 85, 30, 45)
magikarp = pokemon.Poke("Magikarp", "Water", 55, 25, 50)

#Put all pokemon objects into a dictionary to be called
poke_dict = {1: charmander,
             2: squirtle,
             3: bulbasaur,
             4: pikachu,
             5: snorlax,
             6: magikarp
             }


#create abilities object
#Normal                     dmg| acy| buff| debuff| name
tackle = abilities.Abilities(20, 95, None, None, "tackle")
bite = abilities.Abilities(30, 75, None, None, "bite")
slash = abilities.Abilities(25, 85, None, None, "slash")
slam = abilities.Abilities(35, 70, None, None, "slam")
bash = abilities.Abilities(25, 80, None, None, "bash")
tail_whip = abilities.Abilities(25, 90, None, None, "tail whip")

#buffs
sword_dance = abilities.Abilities(0, 100, "SWRD_DNC", None, "sword dance") #raise damage
harden = abilities.Abilities(0, 100, "HRDN", None, "harden") #raise defense
agility = abilities.Abilities(0, 100,"AGLTY", None, "agility") #raise damage
frustration = abilities.Abilities(0, 100, "FSTRIN", None, "frustration") #slightly raise damage and defense

#Debuffs
poison = abilities.Abilities(0, 100, None, "POSN", "poison") #adds a consitantly dealt damage
drowsy = abilities.Abilities(0, 100, None, "DRSY", "drowsy") #lowers opponent damage
burn = abilities.Abilities(0, 100, None, "BURN", "burn") #adds a smaller consitantly dealt damage


#specials moves
vine_whip = abilities.Abilities(25, 90, None, "POSN", "vine whip")
ember = abilities.Abilities(25, 85, None, "BURN", "ember")
thunder_shock = abilities.Abilities(30, 75, None, None, "thunder shock")
aqua_jet = abilities.Abilities(30, 80, None, None, "aqua jet")
pulverizing_pancake = abilities.Abilities(25, 90, None, None, "pulverizing pancake")
splash = abilities.Abilities(500, 2, None, None, "splash")

#append
charmander.move_set.append(tackle)
charmander.move_set.append(bite)
charmander.move_set.append(sword_dance)
charmander.move_set.append(ember)

squirtle.move_set.append(bite)
squirtle.move_set.append(bash)
squirtle.move_set.append(harden)
squirtle.move_set.append(aqua_jet)

bulbasaur.move_set.append(slash)
bulbasaur.move_set.append(bite)
bulbasaur.move_set.append(poison)
bulbasaur.move_set.append(vine_whip)

pikachu.move_set.append(tackle)
pikachu.move_set.append(tail_whip)
pikachu.move_set.append(agility)
pikachu.move_set.append(thunder_shock)

snorlax.move_set.append(bash)
snorlax.move_set.append(slam)
snorlax.move_set.append(drowsy)
snorlax.move_set.append(pulverizing_pancake)

magikarp.move_set.append(tackle)
magikarp.move_set.append(tail_whip)
magikarp.move_set.append(frustration)
magikarp.move_set.append(splash)

#create item object
moo_moo_milk = item.Item("Moo Moo Milk", 100, None, None)
# cure
pure_water = item.Item("Pure Water", 20, None, None)
# revive


#create player object
play_1 = player.Player()
play_2 = player.Player()


### THIS IS WHERE THE FUNCTIONS ARE ###

#gives the player the predetermined items
def give_player_items():
    play_1.items.append(moo_moo_milk)
    play_1.items.append(pure_water)
    play_1.items.append(pure_water)
    play_2.items.append(moo_moo_milk)
    play_2.items.append(pure_water)
    play_2.items.append(pure_water)

#Current turn is defined here
current_turn = play_1
#Play swap changes the value of current turn, allowing a turn based game loop
def play_swap(current_turn):
    if current_turn == play_1:
        return play_2
    else:
        return play_1

#prints the available selection of pokemon from a dictionary
def pick_poke(player):
    print(f"{player.name}, please select a pokemon, the first pokemon selected will be your primary pokemon (enter id number of pokemon wanted)\n")
    for num_poke in range(1,4):
        print(f"please select pokemon in spot \"{str(num_poke)}\"")
        for i in range(len(poke_dict)):
            print(f"{i+1}. {str(poke_dict[i+1].name)}, press {i+1} to select this pokemon")
        test = input("\nPlease enter desired Pokemon: ")

        try:
            test = int(test)
        except:
            print("Please enter a valid id number")
            pick_poke(player)
            return

        if test > len(poke_dict) or test < 1:
            print("Please enter a valid id number")
            pick_poke(player)
            return
        player.poke_list.append(poke_dict[test])


#This is gives the player a selection of actions available at the start of each turn
def play_start(current_turn):
    print()
    print(f"It is currently {current_turn.name}'s turn")
    print()
    print("Please input id number of action wanted")
    print("""1.Attack          2.Items 
3.Swap Pokemon""")
    selection = input()
    try:
        selection = int(selection)
    except:
        print("input not defined please input an avaliable id number")
        play_start(current_turn)
    if selection == 1:
        attack()
    elif selection == 2:
        item_selection()
    elif selection == 3:
        swap_pokemon(current_turn)
    else:
        print("input not defined please input an avaliable id number")
        play_start(current_turn)


#if items are chosen during play_start, this will show what items are available
def item_selection():
    if len(current_turn.items) == 0:
        print("\nYou have no items!\n")
        time.sleep(2)
        play_start(current_turn)
    else:
        counter = 0
        print("\nPlease select item to use\n")
        for item in current_turn.items:
            counter += 1
            print(f"{str(counter)}. {str(item.name)}")
        picked_item = input("\nEnter item id: \n")
        try:
            picked_item = int(picked_item)
        except:
            print("\nThis is not a valid item!\n")
            play_start(current_turn)
        use_item(picked_item)




#this USES the selected item and applies the effects of it
def use_item(selection):
    if selection > len(current_turn.items) or selection <= 0:
        print("This is not a valid item!")
        time.sleep(1)
        play_start(current_turn)
    else:
        chosen_item = current_turn.items[selection-1]
        hp_check = current_turn.poke_list[current_turn.primary].hp + chosen_item.heal
        if chosen_item.heal != 0:
            if hp_check > current_turn.poke_list[current_turn.primary].max_hp:
                current_turn.poke_list[current_turn.primary].hp = current_turn.poke_list[current_turn.primary].max_hp
            else:
                current_turn.poke_list[current_turn.primary].hp += chosen_item.heal
        elif chosen_item.buff != None:
            current_turn.poke_list[current_turn.primary].buff_list.append(item.buff)
        elif chosen_item.debuff != None:
            current_turn.poke_list[current_turn.primary].debuff_list.append(item.debuff)
        current_turn.items.remove(chosen_item)



#the idea is that this will recalculate a pokemons stats at the begining of each turn to account for any new buffs or debuffs
def buff_debuff_value_calculations(current_turn):
    current_turn.poke_list[current_turn.primary].atk = current_turn.poke_list[current_turn.primary].calc_value_atk()
    current_turn.poke_list[current_turn.primary].defense = current_turn.poke_list[current_turn.primary].calc_value_defense()
    current_turn.poke_list[current_turn.primary].hp = current_turn.poke_list[current_turn.primary].calc_value_hp()


#lists available attack options,and takes selection

def attack():
    print()
    print("Please input id number of attack wanted")
    print(f"""1.{current_turn.poke_list[current_turn.primary].move_set[0].name}          2.{current_turn.poke_list[current_turn.primary].move_set[1].name}
3.{current_turn.poke_list[current_turn.primary].move_set[2].name}           4.{current_turn.poke_list[current_turn.primary].move_set[3].name}
5. Return to action selection menu""")
    print()
    selection = input()
    try:
        selection = int(selection)
    except:
        print("please select an available id")
        attack()
    if selection != 1 and selection != 2 and selection != 3 and selection != 4:
        if selection == 5:
            play_start(current_turn)
        else:
            print("please select an available id")
            attack()
    else:
        print()
        damage_calc(selection)


#values are calcated and damges are applied to opponents pokemon

def damage_calc(selection):
    dmg = current_turn.poke_list[current_turn.primary].move_set[int(selection-1)].damage
    acy = current_turn.poke_list[current_turn.primary].move_set[int(selection-1)].accuracy
    buf = current_turn.poke_list[current_turn.primary].move_set[int(selection-1)].buff
    dbf = current_turn.poke_list[current_turn.primary].move_set[int(selection-1)].debuff
    if current_turn == play_1:
        opp = play_2
    else:
        opp = play_1

    if random.randint(0,100) <= acy:
        coefficient = (1 + (int(current_turn.poke_list[current_turn.primary].atk))/100)
        def_coefficient = (1 + (int(current_turn.poke_list[current_turn.primary].defense))/100)
        opp.poke_list[opp.primary].hp -= round((dmg * coefficient)/def_coefficient,0)
        if opp.poke_list[opp.primary].hp <= 0:
            print(f"Hit! {opp.poke_list[opp.primary].name} has fainted!")
        else:
            print(f"Hit! {opp.poke_list[opp.primary].name} now has {str(opp.poke_list[opp.primary].hp)} remaining!")
        opp.poke_list[opp.primary].debuff_list.append(dbf)
        current_turn.poke_list[current_turn.primary].buff_list.append(buf)
        if opp.poke_list[opp.primary].hp <= 0:
            check_poke_list()
            swap_pokemon(opp)
    else:
        print("The attack missed!")


#a function to swap pokemon during battle or when one pokemon fainted
def swap_pokemon(current_player):
    if play_1.alive == False or play_2.alive == False:
        return
    available_pokemon = []

    for i in range(len(current_player.poke_list)):
        if current_player.poke_list[i].hp <= 0:
            continue
        elif i == current_player.primary:
            continue
        else:
            available_pokemon.append(i+1)
            print("Your available pokemon:")
            print(f'{i+1}. {str(current_player.poke_list[i].name)}')
    new_primary = input("\nPlease select desire pokemon to switch to:")

    try:
        new_primary = int(new_primary)
    except:
        print("Enter a valid id")
        swap_pokemon(current_player)
        return 

    if new_primary not in available_pokemon:
        print("Enter a valid id")
        swap_pokemon(current_player)
        return
    else:
        current_player.primary = (new_primary - 1)


#I run through every pokemon in the lists of both players here to determine if one player loses
def check_poke_list():
    play_1_poke = len(play_1.poke_list)
    play_2_poke = len(play_2.poke_list)
    count1 = 0
    count2 = 0

    for poke in play_1.poke_list:
        if poke.hp <= 0:
            count1 += 1
    if count1 == play_1_poke:
        play_1.alive = False
        return play_1.alive

    for poke in play_2.poke_list:
        if poke.hp <= 0:
            count2 += 1
    if count2 == play_2_poke:
        play_2.alive = False
        return play_2.alive

#Intro to game begins here

print("\nWelcome to...")
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
print("In this thrilling two-player showdown, each trainer will carefully choose their three Pokemon and strategically aquire items from the shop. These formidable creatures will clash in epic battles until one succums to defeat by fainting.")
print("In the heat of battle, players will have the option to strategically swap Pokemon (available in future versions) and employ items for tatical advantage (also forthcoming). Once all of a player's Pokemon are exhausted, victory will be claimed by the remaining trainer!!")
print()
print("To continue hit enter...")

input()

#Dictionary is displayed and selection of pokemon happens here

pick_poke(play_1)
pick_poke(play_2)

give_player_items()

print("\nThe contestants have chosen and the stage is now set, may the best contestant win!")
time.sleep(3)

#Game-play loop happens here,breaks when one player loses
while play_1.alive == True and play_2.alive == True:
    buff_debuff_value_calculations(current_turn)
    play_start(current_turn)
    check_poke_list()
    current_turn = play_swap(current_turn)

#Closeing remarks, happens after gamplay loop finishes and winner is determined
print("\nWe have a winner!")
time.sleep(3)

if play_1.alive == True:
    print(f"Congratulations {play_1.name}, you are the pokemon champion!")
else:
    print(f"Congratulations {play_2.name}, you are the pokemon champion!")

time.sleep(2)
print("Thank you for playing Poket-Pal Champions, we hope to better this game and add more customization and polish to it in the near future!")