import cfg as x

#weapon attacks

def attack():
    pass

def sword_spec():
    pass

def dagger_spec():
    pass

def staff_spec():
    pass

def mace_spec():
    pass

#artifact moves

shield_moves = None

spells = None

prayers = None

poisons = None


#consumable effects

def use_potion():
    print("\nYou use a potion.")
    if x.player.stats.hp == x.player.stats.max_hp:
        print("You drink the potion despite being at max health.")
        print("Hope that was worth it.")
    elif (x.player.stats.hp + 25) >= x.player.stats.max_hp:
        x.player.stats.hp = x.player.stats.max_hp
        print("\nYou are healed to full health.")
    else:
        x.player.stats.hp += 25
        print("You drink the potion and regain 25 HP. Nice.")

def use_bomb():
    pass
