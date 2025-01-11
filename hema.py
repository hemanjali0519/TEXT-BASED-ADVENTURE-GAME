
def show_intro():
    print("Welcome to the Castle Adventure!")
    print("You stand at the gates of a mysterious castle.")
    print("You can enter the castle, go to the stables, or explore the gardens.")
    print("Where would you like to go?")

def get_choice(options):
    choice = ""
    while choice not in options:
        choice = input(f"Enter your choice ({', '.join(options)}): ").lower()
    return choice

def castle(inventory):
    print("You enter the castle and find a grand hall.")
    print("There are stairs leading up to the tower and a door to the basement.")
    print("Do you want to go to the tower or the basement?")
    choice = get_choice(["tower", "basement"])
    
    if choice == "tower":
        print("You climb the stairs to the tower and find a sleeping dragon guarding a treasure.")
        print("Do you want to fight the dragon or sneak past it?")
        choice = get_choice(["fight", "sneak"])
        
        if choice == "fight":
            print("You fight the dragon bravely but realize you need a special weapon.")
            if "magic sword" in inventory:
                print("Using the magic sword, you defeat the dragon and claim the treasure!")
            else:
                print("Without the magic sword, you are defeated by the dragon.")
        elif choice == "sneak":
            print("You successfully sneak past the dragon and find a treasure chest filled with gold!")
    
    elif choice == "basement":
        print("You enter the dark basement and find an old library.")
        print("Do you want to search the library or leave?")
        choice = get_choice(["search", "leave"])
        
        if choice == "search":
            print("You find a hidden compartment with a magic sword inside!")
            inventory.append("magic sword")
        elif choice == "leave":
            print("You decide not to risk it and leave the basement.")

def stables(inventory):
    print("You go to the stables and find a beautiful horse.")
    print("The horse seems to be missing its saddle.")
    print("Do you want to search the stables or leave?")
    choice = get_choice(["search", "leave"])
    
    if choice == "search":
        print("You find the horse's saddle and place it on the horse.")
        print("The horse is now ready to ride!")
        inventory.append("horse")
    elif choice == "leave":
        print("You decide not to disturb the horse and leave the stables.")

def gardens(inventory):
    print("You explore the beautiful gardens and find a fountain.")
    print("There is something sparkling at the bottom of the fountain.")
    print("Do you want to reach into the fountain or ignore it?")
    choice = get_choice(["reach", "ignore"])
    
    if choice == "reach":
        print("You reach into the fountain and find a golden key!")
        inventory.append("golden key")
    elif choice == "ignore":
        print("You decide not to get wet and leave the gardens.")

def main():
    inventory = []
    show_intro()
    choice = get_choice(["castle", "stables", "gardens"])
    
    if choice == "castle":
        castle(inventory)
    elif choice == "stables":
        stables(inventory)
    elif choice == "gardens":
        gardens(inventory)
    
    print("Your adventure comes to an end.")
    print("Inventory:", inventory)
    print("Thank you for playing the Castle Adventure!")

if __name__ == "__main__":
    main()