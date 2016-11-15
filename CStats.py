

class Player:
    def __init__(self):
        print("Please choose a race, class, and name to begin."
              " You will start at level 1 with 0 experience.")
        self.Race = input("1. Race\n Choose: Dwarf, Elf, Human \n")
        self.PClass = input("2. Class\n Choose: Fighter, Wizard, Cleric, Rogue\n")
        self.Name = input("3. Name\n What is your name?\n")
        self.Level = 1
        self.XP = 0
        self.Plane = "Material Plane"
        print(str(self.Name + ", the " + self.Race + " " + self.PClass + ". " +"Level: " +
                         str(self.Level) +" Experience: "+ str(self.XP)))


CSL1 = Player()
CSL2 = "Empty"
CSL3 = "Empty"

print("Saving...")
print("Saving...")
print("Saving...")
print("Stats have been saved for " + str(CSL1.Name) + ".")
print("")

print("Available characters: ")
print(CSL1.Name)
print(CSL2)
print(CSL3)


CSL1.Level+=1
MajorInfo =(str(CSL1.Name +" " + CSL1.Race + " " + CSL1.PClass + ". " +"Level: " +
                         str(CSL1.Level) +" Experience: "+ str(CSL1.XP)))
print("\n" + MajorInfo)
