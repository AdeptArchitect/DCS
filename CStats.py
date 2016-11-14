





class Player:
    def __init__(self, Race=0, PClass=0, Name=0):
        print("Please choose a Race, Class, and Name to begin."
              " You will start at level 1 with 0 experience.")
        self.Race = input("1. Race\n Choose: Dwarf, Elf, Human")
        self.PClass = input("2. Class\n Choose: Fighter, Wizard, Cleric, Rogue")
        self.Name = input("3. Name\n What is your name?")
        self.level = 1
        self.xp = 0
        self.plane = "Material Plane"
        '''return print(str(self.Name + ", the " + self.Race + " " + self.PClass + ". " +"Level: " +
                         str(self.level) +" Experience: "+ str(self.xp)))'''

print("Saving...")
print("Saving...")
print("Saving...")
print("Stats have been saved for " + "Player(Name)" + ".")
print("")

print("Available characters: ")

CSL1 = Player(Race, PClass, Name)


class Account:
    def __init__(self, name=0, money=0):
        self.name = name
        self.money = money


UI = input("What's your name? -->")
account = Account(UI, 10000)



