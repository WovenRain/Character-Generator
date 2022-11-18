# Generates a text file containing details about the character
# Takes World, Year, and Animal inputs - with Possible age range, resides and gender

# Proof of concept is: Human, Britain, 2022
import common
from Earth.Entity.Human.humanExperience import humanExperience
from Earth.Entity.Human.humanPersonality import humanPersonality
from Earth.Entity.Human.humanTaste import humanTaste
from Earth.Entity.Human.BladesITD.BladesITD import BladesITD

class generator:
    def __init__(self):
        pass

    def makeChar(self, universe = "Earth",
                    year = 2022,
                    animal = "Human",
                    country = "United Kingdom",
                    extra = "NA"):
        #create character from the ground up
        #create experience, dependant on universe, animal, country
        #create personality - refined from experience
        #create taste - refined from personality
        char = {}
        if universe == "Earth":
            if animal == "Human":
                experience = humanExperience()
                char = experience.makeHuman(year, country)

                personality = humanPersonality()
                personality.makePersonality(char)

                taste = humanTaste()
                taste.makeTaste(char)
                

        if extra == "BladesITD":
            bladesITD = BladesITD()
            bladesITD.blades(char)

        common.saveToJSON(char)
        print(char["Name"])

if __name__ == '__main__':
    gen = generator()
    gen.makeChar(country="Ireland")#, extra="BladesITD")