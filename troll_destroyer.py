import cfg as x
from build import *
from menus import *
from encounters import *

#creates an empty class instance in cfg.py that will be used for basically
#every action the player makes in the game
x.player = CharacterBuild(None, None, None, x.backpack)

#these methods, collectively, make up the character creation process
#provide summary of player's stats
def print_stats():
    print("\n########### YOUR STATS ###########\n")
    print("Your class: " + x.player.stats.spread)
    print("Current HP: " + str(x.player.stats.hp))
    print("Max HP: " + str(x.player.stats.hp))
    print("Toughness: " + str(x.player.stats.toughness))
    print("Strength: " + str(x.player.stats.strength))
    print("Dexterity: " + str(x.player.stats.dexterity))
    print("Intelligence: " + str(x.player.stats.intelligence))
    print("Charisma: " + str(x.player.stats.charisma))

#selects a starting stat spread
def stat_select():
    print("\n########### STAT SELECT ###########\n")
    print("Please select a starting stat spread:\n")
    print("1. Warrior\n2. Rogue\n3. Wizard\n4. Cleric")
    choice = input(">  ")

    if choice == "1":
        x.player.stats = warrior
    elif choice == "2":
        x.player.stats = rogue
    elif choice == "3":
        x.player.stats = wizard
    elif choice == "4":
        x.player.stats = cleric
    else:
        print("Invalid input. Please try again.")
        stat_select()

    print("\n\nYou have selected: " + x.player.stats.spread)
    print_stats()

    print("\n\nConfirm selection:\n1.Yes\n2.No")
    choice = input(">  ")

    if choice == "1":
        pass
    elif choice == "2":
        stat_select()

#provides summary of currently equipped weapon
def print_weapon():
    print("\n########### EQUIPPED WEAPON ###########\n")
    print("\nCurrent weapon: " + x.player.weapon.name)
    print("Description: " + x.player.weapon.desc)
    print("Hit Rating: " + str(x.player.weapon.hit))
    print("Base Damage: " + str(x.player.weapon.dmg))
    print("Spell Rating: " + str(x.player.weapon.spell_power))

#selects a starting weapon
def weapon_select():
    print("\n########### WEAPON SELECT###########\n")
    print("\nPlease select a starting weapon:")
    print("1. Sword\n2. Dagger\n3. Staff\n4. Mace")
    choice = input(">  ")

    if choice == "1":
        x.player.weapon = sword
    elif choice == "2":
        x.player.weapon = dagger
    elif choice == "3":
        x.player.weapon = staff
    elif choice == "4":
        x.player.weapon = mace
    else:
        print("Invalid input. Please try again.")
        weapon_select()

    print("\n\nYou have selected: " + x.player.weapon.name)
    print_weapon()

    print("\n\nConfirm selection:\n1.Yes\n2.No")
    choice = input(">  ")

    if choice == "1":
        pass
    elif choice == "2":
        weapon_select()

#provides summary of current accessory (off hand item)
def print_accessory():
    print("\n########### EQUIPPED ACCESSORY ###########\n")
    print("Current accessory: " + x.player.accessory.name)
    print("Description: " + x.player.accessory.desc)
    print("Physical Hit Bonus: " + str(x.player.accessory.phys_hit_up))
    print("Physical Damage Bonus: " + str(x.player.accessory.phys_dmg_up))
    print("Toughness Bonus: " + str(x.player.accessory.tough_up))
    print("Magic Hit Bonus: " + str(x.player.accessory.mag_hit_up))
    print("Magic Damage Bonus: " + str(x.player.accessory.mag_dmg_up))

#selects a starting accessory
def accessory_select():
    print("\n########### ACCESSORY SELECT ###########\n")
    print("Please select a starting accessory:\n")
    print("1. Shield\n2. Spellbook\n3. Holy Symbol\n4. Poison Kit")
    choice = input(">  ")

    if choice == "1":
        x.player.accessory = shield
    elif choice == "2":
        x.player.accessory = spellbook
    elif choice == "3":
        x.player.accessory = holy_symbol
    elif choice == "4":
        x.player.accessory = poison_kit
    else:
        print("Invalid input. Please try again.")
        accessory_select()

    print("\n\nYou have selected: " + x.player.accessory.name)
    print_accessory()

    print("\n\nConfirm selection:\n1.Yes\n2.No")
    choice = input(">  ")

    if choice == "1":
        pass
    elif choice == "2":
        accessory_select()
    else:
        print("Invalid input. Please try again.")
        accessory_select()

#shows player a rundown of the items in their inventory
def print_backpack():
    print("\n########### INVENTORY ###########\n")
    i = 0
    while i < len(x.backpack):
        print(str(i + 1) + ". " + x.backpack[i].name + " (" +
        str(x.backpack[i].uses) + " uses remaining.)")
        print(x.backpack[i].desc)
        i += 1

#uses above method to print item inventory, prompts for a selection, and then
#uses said item
def use_consumable():
    print_backpack()
    print("\n")
    print("Select an item to use, or press 0 to return to the previous screen.")
    choice = input(">  ")

    if int(choice) > 0 and int(choice) <= len(x.backpack):
        print("\nYou have selected: " + x.backpack[int(choice) - 1].name)
        print("\nWould you like to use this item?\n1.Yes\n2.No")
        confirm = input(">  ")

        if confirm == "1":
            if x.backpack[int(choice) - 1].uses > 0:
                x.backpack[int(choice) - 1].uses -= 1
                x.backpack[int(choice) - 1].item_method()
                print("\nYou have " + str(x.backpack[int(choice) - 1].uses) +
                " uses remaining of " + str(x.backpack[int(choice) - 1].name))
            else:
                print("\nYou don't have any more uses of that item.")
                use_consumable()
        else:
            print("Invalid selection. Please try again.")
            use_consumable()
    elif choice == "0":
        pass
    else:
        print("Invalid input. Please try again.")
        use_consumable()



#selects a starting piece of consumable equipment
def consumable_select():
    print("\nSelect your starting consumable:")
    print("\n1. Potion\n2. Bomb")
    choice = input(">  ")

    if choice == "1":
        x.backpack.append(potion)
    elif choice == "2":
        x.backpack.append(bomb)

    print("You have selected: " + x.backpack[0].name)
    print_backpack()

    print("\n\nConfirm selection:\n1.Yes\n2.No")
    choice = input(">  ")

    if choice == "1":
        pass
    elif choice == "2":
        x.backpack.remove(x.backpack[0])
        consumable_select()

#finally, this method runs all the above in order, allowing for custom character
#creation
def character_creation():
    print("########### CHARACTER CREATION ###########")
    stat_select()
    weapon_select()
    accessory_select()
    consumable_select()


#this shows a complete rundown of the player character's details
def character_sheet():
    print("\n########### CHARACTER SHEET ###########\n")
    print_stats()
    print_weapon()
    print_accessory()
    print_backpack()

#this prompts the player to either select a preset or create their own character
def character_selection():
    print("\n############ CHARACTER SELECTION ###########\n")
    print("\nChoose a preset character, or create a custom character:\n")
    print("1. A warrior who fights with sword and shield.\n")
    print("2. A cleric who fights with a mace and holy symbol.\n")
    print("3. A wizard who slings spells with a staff and spellbook.\n")
    print("4. A rogue who fights with a dagger and poisons.\n")
    print("0. Enter Character Creation\n")

    choice = input(">  \n")

    if choice == "1":
        x.player = CharacterBuild(warrior, sword, shield,
        x.backpack.append(potion))
        character_confirm()
    elif choice == "2":
        x.player = CharacterBuild(cleric, mace, holy_symbol,
        x.backpack.append(bomb))
        character_confirm()
    elif choice == "3":
        x.player = CharacterBuild(wizard, staff, spellbook,
        x.backpack.append(potion))
        character_confirm()
    elif choice == "4":
        x.player = CharacterBuild(rogue, dagger, poison_kit,
        x.backpack.append(bomb))
        character_confirm()
    elif choice == "0":
        character_creation()
        character_confirm()
    else:
        print("I'm not sure what to do with this. Come back when you're ready.")

#used in character_selection() to print a summary of the player's character,
#sending them back to the start if they say no
def character_confirm():
    print("Here's a summary of your character:")
    character_sheet()
    print("\n\nEverything look good?\n1. Yes, let's go!\n2. No, hold on!")
    choice = input(">  ")

    if choice == "1":
        pass
    elif choice == "2":
        x.backpack = []
        character_selection()
    else:
        print("Invalid input. Please try again.")
        character_confirm()



#now that that's out of the way, we can actually start the game. hooray!
print("Welcome to troll destroyer.")
print("What is your name?")
name = input("> ")

x.player_name = name

print(f"\n\nWelcome, {x.player_name}.")

character_selection()

print(f"\nThanks, {x.player_name}. You're all set. By the way, you can also fight with \
just your fists, if you're into that kind of thing.\n")
x.unequipped_weapons.append(fists)

print("Received weapon: " + x.unequipped_weapons[-1].name)

#prints x.unequipped_weapons in numbered list, asks for input, and if new weapon
#is chosen, adds current weapon to x.unequipped_weapons, changes current weapon
#to selection, and then removes selection from list

def change_weapon():
    print("\n########### WEAPON SELECT ###########\n")
    print("Currently equipped: " + x.player.weapon.name)
    print("Select the weapon you'd like to switch to:\n")

    #this while loop makes a numbered list of all unequipped_weapons in the
    #player's possession
    i = 0
    while i < len(x.unequipped_weapons):
        print(str(i + 1) + ". " + x.unequipped_weapons[i].name)
        i += 1
    #they also have the option to back out of the menu
    print("0. Nevermind.")
    choice = input(">  \n")

    #player types the number corresponding to the item they want, that gets
    #turned into an int. if it's in the list, it keeps going
    if int(choice) > 0 and int(choice) <= len(x.unequipped_weapons):
        #tell them which item they chose from the menu and confirm the switch
        print("You have selected " + x.unequipped_weapons[int(choice) - 1].name)
        print(x.unequipped_weapons[int(choice) - 1])
        print("Unequip " + x.player.weapon.name + " and equip " +
        x.unequipped_weapons[int(choice) - 1].name + "?\n1.Yes\n2.No")
        confirm = input(">  ")
        #if they confirm the switch...
        if confirm == "1":
            #their current weapon is added to the list of unequipped_weapons
            x.unequipped_weapons.append(x.player.weapon)
            #their weapon is updated to the weapon they chose
            x.player.weapon = x.unequipped_weapons[int(choice) - 1]
            #and their newly equipped weapon is taken from the list
            x.unequipped_weapons.remove(x.unequipped_weapons[int(choice) - 1])
        elif confirm == "2":
            #if they select no, they're brought to the switch menu
            change_weapon()
        else:
            #this also brings them back to the start, but tells them why
            print("Invalid input. Please try again.")
            change_weapon()
    elif choice == "0":
        #if they say "Nevermind," they leave this menu
        print("You decide not to change your weapon.")
        pass
    else:
        #if they do something they're not supposed to, they go back to the top
        print("Invalid input. Please try again.")
        change_weapon()


#this is the menu that players will see after character creation, and outside
#of encounters

def health_bar(life, max):
    print(("█" * life) + ("-" * (max - life)))
    return None

def main_menu():
    print("\n########### MAIN MENU ###########\n")
    print(x.player_name)
    health_bar(int(x.player.stats.hp), int(x.player.stats.max_hp))
    print("You currently have " + str(x.player.stats.hp) + "/" +
    str(x.player.stats.max_hp) + "HP.")

    print("You have: " + str(x.gold) + " gold.")
    print("You have killed " + str(x.trolls_killed) + " trolls.\n")
    print("What would you like to do next?\n")
    print("1. Next encounter.")
    print("2. View my inventory.")
    print("3. Change my weapon.")
    print("4. View my stats.")
    print("5. Punch yourself in the head.")
    print("0. Die on purpose.")

    choice = input(">  ")

    if choice == "1":
        #the idea right now is for another method, encounter(), to keep track
        #of the players progress. i envision three main kinds of encounter
        # 1. Fights with trolls (obviously)
        # 2. Visiting a merchant (maybe every 5th encounter?)
        # 3. Boss fights (probably every 10th encounter)
        # each of these is likely to require its own method. the method in this
        # option will move the player to the appropriate encounter method
        next_encounter()
    elif choice == "2":
        #going to have to make another method that uses items. i'm thinking it
        #needs to be separate from the print_backpack() method to avoid players
        #using items in character creation. maybe this new method starts by
        #printing the backpack. that probably makes more sense
        use_consumable()
        main_menu()
    elif choice == "3":
        #i think this is already working as intended. players will also need to
        #be able to do this in combat, but in combat this action incurs an
        #opportunity cost of being attacked. outside of encounters, this move
        #is free
        change_weapon()
        main_menu()
    elif choice == "4":
        character_sheet()
        print("Press any button to return to main menu")
        choice = input(">  ")
        main_menu()
    elif choice == "5":
        x.player.stats.hp -= 5
        print("\n\nWell that hurt.")
        main_menu()
    elif choice == "0":
        print("\nWhat? really?")
        print("\n1. Yes\n\n2. Just kidding.")
        confirm = input(">  ")
        if confirm == "1":
            print("Oh. Damn, ok. You died. Bye.")
            exit()
        else:
            print("Whew. Okay. You had me worried for a second.")
            main_menu()
    else:
        print("Invalid input. Please try again.")
        main_menu()


main_menu()
