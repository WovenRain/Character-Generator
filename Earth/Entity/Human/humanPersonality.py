from operator import truediv
import common
import random

class humanPersonality:
    def __init__(self):
        f = open("Earth/Entity/Human/SchoolsOfThought", "r", encoding='iso-8859-15')
        self.SchoolsOfThought = f.read().split("\n")
        f.close()
        
        self.naturalHairColours = ["Black", "Brown", "Blonde", "White", "Gray", "Red"]
        self.naturalHairTypes = ["Straight", "Naturally Wavy", "Curly", "Kinky"]
        self.naturalHairTextures = ["Thick/Coarse Hair", "Medium Hair", "Fine Hair"]
        self.hairLengths = ["Ear", "Chin", "Neck", "Shoulder", "CollarBone", "Armpit", "Nipple", "Mid Back"]

        self.fightingStyles = ["Boxing", "Kickboxing", "Karate", "Wrestling", "Taekwondo", "Judo", "Jiu-Jitsu", "Kung-fu"]

        self.pets = common.getListFile("Earth/Entity/Human/Pets")
        self.allHobbies = common.getListFile("Earth/Entity/Human/Hobbies")
        self.eInterests = common.getListFile("Earth/Entity/Human/EducationalInterests")
        self.languages = common.getListFile("Earth/Entity/Human/Languages")
        self.bodyParts = common.getListFile("Earth/Entity/Human/BodyParts")

        self.coreSkills = ["decision-making", "problem-solving", "creative thinking", "critical thinking",
                "communication", "interpersonal skills", "self-awareness", "empathy", "assertiveness",
                "equanimity", "resilience"]
        
        self.englishWordlist = common.getListFile("Earth/Entity/Human/EnglishWordlist")
    
    def makePersonality(self, char):
        #nickname
        
        #Natural hair, More experiential/innate
        #makes more sense to put it here as they get to style it
        naturalHairColour = common.getRandom(self.naturalHairColours)
        naturalHairType = common.getRandom(self.naturalHairTypes)
        naturalHairTexture = common.getRandom(self.naturalHairTextures)
        char["Natural Hair"] = {"Colour": naturalHairColour, 
                    "Type": naturalHairType, 
                    "Texture": naturalHairTexture}
        
        #hair length
        char["Hair Length"] = common.getRandom(self.hairLengths)
        
        #Core Skills, and Core weakness
        skills = self.coreSkills
        char["Core Skills"] = [skills.pop(random.randint(0,len(skills)-1)),
                                skills.pop(random.randint(0,len(skills)-1))]
        char["Core Weakness"] = skills.pop(random.randint(0,len(skills)-1))

        #Philosophy
        p = random.randint(1,8)
        char["Philosophical Influences/Interests"] = common.returnMultiple(p, self.SchoolsOfThought)
        
        #personality traits overview
        Hopeful = random.randint(0,100)
        traits = {"Hopefulness": common.traitMeasure(Hopeful) + ", " + str(Hopeful) + "/100"}
        
        Hardworking = random.randint(0,100)
        traits["Hardworking"] = common.traitMeasure(Hardworking) + ", " + str(Hardworking) + "/100"
        
        Kindness = random.randint(0,100)
        traits["Kindness"] = common.traitMeasure(Kindness) + ", " + str(Kindness) + "/100"
        
        Egotistical = random.randint(0,100)
        traits["Egotistical"] = common.traitMeasure(Egotistical) + ", " + str(Egotistical) + "/100"
        
        Selfish = random.randint(0,100)
        traits["Selfish"] = common.traitMeasure(Selfish) + ", " + str(Selfish) + "/100"
        
        Active = random.randint(0,100)
        traits["Active"] = common.traitMeasure(Active) + ", " + str(Active) + "/100"
        
        Cheerful = random.randint(0,100)
        traits["Cheerful"] = common.traitMeasure(Cheerful) + ", " + str(Cheerful) + "/100"
        
        Violent = random.randint(0,100)
        traits["Violent"] = common.traitMeasure(Violent) + ", " + str(Violent) + "/100"
        
        Humorous = random.randint(0,100)
        traits["Humorous"] = common.traitMeasure(Humorous) + ", " + str(Humorous) + "/100"
        
        Expressive = random.randint(0,100)
        traits["Expressive"] = common.traitMeasure(Expressive) + ", " + str(Expressive) + "/100"

        Curiosity = random.randint(0,100)
        traits["Curiosity"] = common.traitMeasure(Curiosity) + ", " + str(Curiosity) + "/100"
        char["Personality Traits"] = traits

        #fighting skill/style
        #violence, hardworking, active
        f = random.randint(0,int((Violent + Hardworking + Active)/3))
        if f < 20:
            char["Fighting Style"] = ["Untrained"]
        else:
            char["Fighting Style"] = common.returnMultiple(f, self.fightingStyles, 15)

        #Education
        #curiosity
        e = random.randint(0,Curiosity)
        if e < 30:
            char["Educational Interests"] = ["Listless"]
        elif e < 60:
            char["Educational Interests"] = [common.getRandom(self.eInterests)]
        else:
            char["Educational Interests"] = common.returnMultiple(e, self.eInterests, 15)

        #languages
        #hardworking
        l = random.randint(0,Hardworking + Curiosity)
        la = ["Native Language"]
        if l < 40:
            pass
        else:
            la.extend(common.returnMultiple(l, self.languages, 30))
        char["Languages"] = la

        #pets
        #kindness
        p = random.randint(0,Kindness)
        if p < 30:
            char["Pets"] = []
        else:
            char["Pets"] = common.returnMultiple(p, self.pets, 25)

        #hobbies, including collections
        #active, curiosity
        p = random.randint(0,Active + Curiosity)
        if p < 10:
            char["Hobbies"] = []
        else:
            char["Hobbies"] = common.returnMultiple(p, self.allHobbies, 20)

        #goals/achievements
        #hopeful
        
        #awards
        #egotistical, hardworking
        
        #sayings/Favourite words
        fw = random.randint(12,24)
        char["Favourite Words"] = common.returnMultiple(fw, self.englishWordlist)
        #char["Weird Sayings"] = common.returnMultipleTwoPart(5, self.englishWordlist, self.englishWordlist)
        
        #Habits

        #tattoos
        char["Tattoos"] = common.returnMultiple(random.randint(0,int(Expressive/8)), self.bodyParts)
        
        #religion
        
        #hopes/dreams/aspirations
