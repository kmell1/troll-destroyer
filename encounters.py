import cfg as x

def troll_fight():
    troll_hp = 50

def merchant():
    pass

def boss_fight():
    pass


def next_encounter():
    x.encounter += 1
    print(x.encounter)
    if x.encounter % 10 == 0:
        print("It's time to fight a boss.")
        boss_fight()
    elif x.encounter % 5 == 0:
        print("You find a merchant.")
        merchant()
    else:
        print("You press on and discover a troll.")
        troll_fight()
