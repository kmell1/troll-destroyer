from troll_destroyer import *

def main_menu():
    print("\n########### MAIN MENU ###########\n")
    print("What would you like to do next?\n")
    print("1. Next encounter.")
    print("2. View my inventory.")
    print("3. Change my weapon.")
    print("4. View my stats.")

    choice = input(">  ")

    if choice == "1":
        #the idea right now is for another method, encounter(), to keep track
        #of the players progress. i envision three main kinds of encounter
        # 1. Fights with trolls (obviously)
        # 2. Visiting a merchant (maybe every 5th encounter?)
        # 3. Boss fights (probably every 10th encounter)
        # each of these is likely to require its own method. the method in this
        # option will move the player to the appropriate encounter method
        print("There's nothing to fight yet. Sorry.")
        #this is the only option that will not have main_menu at the end. but,
        #since there is no encounter loop to speak of yet, it's here for the
        #time being
        main_menu()
    elif choice == "2":
        #going to have to make another method that uses items. i'm thinking it
        #needs to be separate from the print_backpack() method to avoid players
        #using items in character creation. maybe this new method starts by
        #printing the backpack. that probably makes more sense
        print_backpack()
        print("Press any button to return to main menu")
        choice = input(">  ")
        main_menu()
    elif choice == "3":
        #i think this is already working as intended. players will also need to
        #be able to do this in combat, but in combat this action incurs an
        #opportunity cost of being attacked. outside of encounters, this move
        #is free
        weapon_select()
        main_menu()
    elif choice == "4":
        character_sheet()
        print("Press any button to return to main menu")
        choice = input(">  ")
        main_menu()
