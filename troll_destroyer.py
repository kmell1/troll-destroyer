import cfg as x
from build import *

#creates an empty class instance in cfg.py that will be used for basically
#every action the player makes in the game
x.player = CharacterBuild(None, None, None, x.backpack)

#these methods, collectively, make up the character creation process
#provide summary of player's stats
def print_stats():
    print("\nYour class: " + x.player.stats.spread)
    print("Current HP: " + str(x.player.stats.hp))
    print("Max HP: " + str(x.player.stats.hp))
    print("Toughness: " + str(x.player.stats.toughness))
    print("Strength: " + str(x.player.stats.strength))
    print("Dexterity: " + str(x.player.stats.dexterity))
    print("Intelligence: " + str(x.player.stats.intelligence))
    print("Charisma: " + str(x.player.stats.charisma))

#selects a starting stat spread
def stat_select():
    print("\nPlease select a starting stat spread:")
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
    print("\nCurrent weapon: " + x.player.weapon.name)
    print("Description: " + x.player.weapon.desc)
    print("Hit Rating: " + str(x.player.weapon.hit))
    print("Base Damage: " + str(x.player.weapon.dmg))
    print("Spell Rating: " + str(x.player.weapon.spell_power))

#selects a starting weapon
def weapon_select():
    print("\nPlease select a starting weapon:")
    print("1. Sword\n2. Dagger\n3. Staff")
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
    print("\nCurrent accessory: " + x.player.accessory.name)
    print("Description: " + x.player.accessory.desc)
    print("Physical Hit Bonus: " + str(x.player.accessory.phys_hit_up))
    print("Physical Damage Bonus: " + str(x.player.accessory.phys_dmg_up))
    print("Toughness Bonus: " + str(x.player.accessory.tough_up))
    print("Magic Hit Bonus: " + str(x.player.accessory.mag_hit_up))
    print("Magic Damage Bonus: " + str(x.player.accessory.mag_dmg_up))

#selects a starting accessory
def accessory_select():
    print("\nPlease select a starting accessory:")
    print("1. Shield\n2. Spellbook\n3. Holy Symbol")
    choice = input(">  ")

    if choice == "1":
        x.player.accessory = shield
    elif choice == "2":
        x.player.accessory = spellbook
    elif choice == "3":
        x.player.accessory = holy_symbol

    print("\n\nYou have selected: " + x.player.accessory.name)
    print_accessory()

    print("\n\nConfirm selection:\n1.Yes\n2.No")
    choice = input(">  ")

    if choice == "1":
        pass
    elif choice == "2":
        accessory_select()

#shows player a rundown of the items in their inventory
def print_backpack():
    print("\n----INVENTORY----\n")
    i = 0
    while i < len(x.backpack):
        print(str(i + 1) + ". " + x.backpack[i].name + " (" +
        str(x.backpack[i].uses) + " uses remaining.)")
        print(x.backpack[i].desc)
        i += 1

    # for item in x.backpack:
    #     print(item.name + " (" + str(item.uses) + " uses remaining.)")
    #     print(item.desc)

#selects a starting piece of consumable equipment
def consumable_select():
    print("\nSelect your starting consumable:")
    print("1. Potion\n2. Bomb")
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
    stat_select()
    weapon_select()
    accessory_select()
    consumable_select()

def character_sheet():
    print_stats()
    print_weapon()
    print_accessory()
    print_backpack()


#now that that's out of the way, we can actually start the game. hooray!
print("Welcome to troll destroyer.")
print("What is your name?")
name = input("> ")

print(f"\n\nWelcome, {name}.")

def character_selection():
    print("\nChoose a preset character, or create a custom character:")
    print("1. A warrior who fights with sword and shield.")
    print("2. A cleric who fights with a mace and holy symbol.")
    print("3. A wizard who slings spells with a staff and spellbook.")
    print("4. A rogue who fights with a dagger and poisons.")
    print("0. Enter Character Creation")

    choice = input(">  ")

    if choice == "1":
        x.player = CharacterBuild(warrior, sword, shield,
        x.backpack.append(potion))
    elif choice == "2":
        x.player = CharacterBuild(cleric, mace, holy_symbol,
        x.backpack.append(bomb))
    elif choice == "3":
        x.player = CharacterBuild(wizard, staff, spellbook,
        x.backpack.append(potion))
    elif choice == "4":
        x.player = CharacterBuild(rogue, dagger, poison_kit,
        x.backpack.append(bomb))
    elif choice == "0":
        character_creation()
    else:
        print("I'm not sure what to do with this. Come back when you're ready.")

def character_confirm():
    print("Here's a summary of your character:")
    character_sheet()
    print("\n\nEverything look good?\n1. Yes, let's go!\n2. No, hold on!")
    choice = input(">  ")

    if choice == "1":
        pass
    else:
        x.backpack = []
        character_selection()

character_selection()
character_confirm()

print(f"Thanks, {name}. You're all set. By the way, you can also fight with\
just your fists, if you're into that kind of thing. Try changing to them now.")
x.unequipped_weapons.append(fists)

print("Received weapon: " + x.unequipped_weapons[-1].name)
print("\nTry switching to it now:\n")

#prints x.unequipped_weapons in numbered list, asks for input, and if new weapon
#is chosen, adds current weapon to x.unequipped_weapons, changes current weapon
#to selection, and then removes selection from list

def change_weapon():
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
    choice = input(">  ")

    #player types the number corresponding to the item they want, that gets
    #turned into an int. if it's in the list, it keeps going
    if int(choice) > 0 and int(choice) <= len(x.unequipped_weapons):
        #tell them which item they chose from the menu and confirm the switch
        print("You have selected " + x.unequipped_weapons[int(choice) - 1].name)
        print("Unequip " + x.player.weapon.name + "?\n1.Yes\n2.No")
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


change_weapon()
print("Nice. Probably shouldn't just punch things though. Let's switch back to\
a real weapon.")
change_weapon()

print("Great! Unfortunately there's nothing to fight yet. So I guess you win!")
print("GAME OVER")
