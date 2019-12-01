#aim is to create two player digipet battle simulator by creating original digipets.


class DigiPet:
    def __init__(self, name, pettype, level, hp, power, stamina, endurance, xp):
        self.name = name
        self.pettype = pettype
        self.level = level
        self.hp = hp
        self.power = power
        self.stamina = stamina
        self.endurance = endurance
        self.xp = xp
        

    #digipet functions used in story mode
    def level_up(self):
        print("Write a level up function. Create XP property")
        print("write increase xp function here")
    def increaseStats(self):
        print("Increase power endurance and stamina when level increases.")


global digipetlist
digipetlist = []#fill list with digipet objects
basestats = {}

def BattleLoop(digiPet1, digiPet2):
    #create objects pet 1 and pet 2  which will battle
    #initialize digipet fields with base stats
    print("Write battle functions and create battle loop")
