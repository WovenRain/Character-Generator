import common
import random

class BladesITD:
    def __init__(self):
        self.Aliases = common.getListFile("Earth/Entity/Human/BladesITD/Aliases")
        self.Forenames = common.getListFile("Earth/Entity/Human/BladesITD/Forenames")
        self.Surnames = common.getListFile("Earth/Entity/Human/BladesITD/Surnames")

        self.Goals = common.getListFile("Earth/Entity/Human/BladesITD/Goals")

        self.Looks = common.getListFile("Earth/Entity/Human/BladesITD/Looks")
        self.Clothes = common.getListFile("Earth/Entity/Human/BladesITD/Clothes")

        self.Jobs = common.getListFile("Earth/Entity/Human/BladesITD/Jobs")

        self.Quirks = common.getListFile("Earth/Entity/Human/BladesITD/Quirks")
        self.Traits = common.getListFile("Earth/Entity/Human/BladesITD/Traits")
        self.Interests = common.getListFile("Earth/Entity/Human/BladesITD/Interests")
        self.PreferredMethod = common.getListFile("Earth/Entity/Human/BladesITD/PreferredMethod")

        self.Countries = ["Akoros", "Severos", "Iruvia", "The Dagger Isles", "Skovlan", "Tycheros"]

        self.Vices = ["Faith", "Gambling", "Luxury", "Obligation", "Pleasure", "Stupor", "Weird"]

        self.Backgrounds = ["Academic", "Labor", "Law", "Trade", "Military", "Noble", "Underworld"]

        self.Playbooks = ["Cutter", "Hound", "Leech", "Lurk", "Slide", "Spider", "Whisper"]

        self.Attributes = {
            "Hunt": 0, "Study": 0, "Survey": 0, "Tinker": 0,
            "Attune": 0, "Command": 0, "Consort": 0, "Sway": 0, 
            "Finesse": 0, "Prowl": 0, "Skirmish": 0, "Wreck": 0
        }

    def blades(self, char):
        # clear irrelevant
        char["BirthYear"] = 0
        char["BirthDate"] = ""

        # name
        name = common.returnMultipleTwoPart(1, self.Forenames, self.Surnames)[0]
        char["Name"] = name
        char["Alias"] = common.getRandom(self.Aliases)
        
        # Job
        char["Employment"] = common.getRandom(self.Jobs)
        
        # Birthplace and Heritage
        char["BirthPlace"] = common.possibleAlteration(3, self.Countries[0], self.Countries)
        char["Heritage"] = common.possibleAlteration(5, char["BirthPlace"], self.Countries)
        # clothes and looks
        char["Clothes"] = common.returnMultiple(random.randint(1,4), self.Clothes)
        char["Looks"] = common.getRandom(self.Looks)

        # goals and methods
        char["Goals"] = common.getRandom(self.Goals)
        char["Preferred Methods"] = common.returnMultiple(random.randint(1,3), self.PreferredMethod)

        # Traits, Quirks, Interests
        char["Traits"] = common.returnMultiple(random.randint(1,3), self.Traits)
        char["Quirk"] = common.getRandom(self.Quirks)
        char["Interests"] = common.getRandom(self.Interests)

        # Vice
        char["Vice"] = common.getRandom(self.Vices)

        # Playbook
        char["Playbook"] = common.getRandom(self.Playbooks)
        char["Attributes"] = self.Attributes
        if char["Playbook"] == "Cutter":
            char["Attributes"]["Skirmish"] = 2
            char["Attributes"]["Command"] = 1
        elif char["Playbook"] == "Hound":
            char["Attributes"]["Hunt"] = 2
            char["Attributes"]["Survey"] = 1
        elif char["Playbook"] == "Leech":
            char["Attributes"]["Tinker"] = 2
            char["Attributes"]["Wreck"] = 1   
        elif char["Playbook"] == "Lurk":
            char["Attributes"]["Prowl"] = 2
            char["Attributes"]["Finesse"] = 1
        elif char["Playbook"] == "Slide":
            char["Attributes"]["Sway"] = 2
            char["Attributes"]["Consort"] = 1    
        elif char["Playbook"] == "Spider":
            char["Attributes"]["Consort"] = 2
            char["Attributes"]["Study"] = 1 
        elif char["Playbook"] == "Whisper":
            char["Attributes"]["Attune"] = 2
            char["Attributes"]["Study"] = 1
        
        # Buffs need to be different
        attri = list(char["Attributes"].keys())
        random.shuffle(attri)

        # No Attributes higher than 2
        # Heritage
        settling = True
        while(settling):
            heritageBuff = attri.pop()
            if char["Attributes"][heritageBuff] < 2:
                char["HeritageBuff"] = [char["Heritage"], heritageBuff]
                char["Attributes"][heritageBuff] = char["Attributes"][heritageBuff] + 1
                settling = False

        # Background
        settling = True
        while(settling):
            backgroundBuff = attri.pop()
            if char["Attributes"][backgroundBuff] < 2:
                char["Background"] = [common.getRandom(self.Backgrounds), backgroundBuff]
                char["Attributes"][backgroundBuff] = char["Attributes"][backgroundBuff] + 1
                settling = False

        # Chosen
        attri = list(char["Attributes"].keys())
        settling = 2
        char["Chosen Buff"] = []
        while(settling > 0):
            chosenBuff = common.getRandom(attri)
            if char["Attributes"][chosenBuff] < 2:
                char["Chosen Buff"].append(chosenBuff)
                char["Attributes"][chosenBuff] = char["Attributes"][chosenBuff] + 1
                settling = settling - 1
