import random
import common

class humanExperience:
    def __init__(self):
        self.initials = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
            "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.monthLengths = [31,28,31,30,31,30,31,31,30,31,30,31]
        self.bloodTypes = ["A+", "B+", "AB+", "O+", "A-", "B-", "AB-", "O-"]
        self.eyeColours = ["Amber", "Blue", "Brown", "Gray", "Green", "Hazel", "Red"]
        self.countries = common.getListFile("Earth/Countries")
        self.bodyParts = common.getListFile("Earth/Entity/Human/BodyParts")
        self.phobias = common.getListFile("Earth/Phobias")
        self.Traumas = common.getListFile("Earth/Entity/Human/Traumas")
        self.Crimes = common.getListFile("Earth/Entity/Human/Crimes")

        self.parents = ["Orphaned, Foster", "Mother and Father", "Mother", "Father", "Mother, Father and Step Mother",
                    "Mother, Step Father, Father and Step Mother", "Mother, Step Father and Father", "Adopted"]

        self.visualCategory = ["Category 0: No or mild visual impairment",
                "Category: 1 Moderate visual impairment, presenting visual acuity worse than 6/18 and better than 6/60",
                "Category: 2 Severe visual impairment, presenting visual acuity worse than 6/60 and better than 3/60",
                "Category: 3 Blindness, presenting visual acuity worse than 3/60 and better than 1/60",
                "Category: 4 Blindness, presenting visual acuity worse than 1/60 with light perception",
                "Category: 5 Blindness, irreversible blindness with no light perception"]
        self.visualImpairments = ["Vision Impairment: Cataracts",
            "Glaucoma",
            "Macular degeneration",
            "Corneal opacification",
            "Childhood blindness",
            "Refractive error",
            "Trachoma",
            "Diabetic retinopathy",
            "Undetermined"]
        self.economicStatus = ["Ultra Wealthy",
            "Wealthy",
            "Well off",
            "Middle Class",
            "Poor",
            "Poverty"]

    def makeHuman(self, year, country):
        #birthplace
        char = {"BirthPlace": common.possibleAlteration(5, country, self.countries)}

        #heritage
        char["Heritage"] = common.possibleAlteration(5, char["BirthPlace"], self.countries)

        #family Name
        familyNames = common.findFile("Earth/Entity/Human/Common Surnames", char["Heritage"], "United Kingdom")
        fName = common.getRandom(familyNames)

        #Generate first initial
        initial = common.getRandom(self.initials)
        #print(initial + " " + fName)

        #write name
        handle = initial + " " + fName
        char["Name"] = handle

        #get age
        #age range = 18-60
        birthMonth = random.randint(1,12)
        birthDate = random.randint(1,self.monthLengths[birthMonth-1])
        age = random.randint(18,50)
        birthYear = year - age

        #write birthdate, easer to have separate birthYear
        char["BirthDate"] = str(birthDate) + "/" + str(birthMonth) + "/" + str(birthYear)
        char["BirthYear"] = birthYear
        char["Age"] = str(age)

        #bloodType
        char["Bloodtype"] = common.getRandom(self.bloodTypes)
        
        #Sex at birth
        s = random.randint(0,100)
        if s < 49:
            sex = "Male"
        elif s < 98:
            sex = "Female"
        else: 
            sex = "Intersex"
        #write Sex at birth
        char["Sex at Birth"] = sex

        #Gender
        g = random.randint(0, 100)
        if g < 10:
            if sex == "Male":
                gender = "Female"
            elif sex == "Female":
                gender = "Male"
        elif g < 20:
            gender = "Non-Binary"
        else:
            gender = sex
            if sex == "Intersex":
                if g < 30:
                    gender = "Male"
                elif g < 60:
                    gender = "Female"
                else: 
                    gender = "Non-Binary"
        #write Gender
        char["Gender"] = gender
        char["Gender Conformity"] = str(random.randint(0,100)) + "/100"

        #sexuality
        s = random.randint(0,100)
        if s < 8:
            sexuality = "Asexual"
        elif s < 33:
            sexuality = "Heterosexual"
        elif s < 55:
            sexuality = "Bi/pansexual, prefers Masc"
        elif s < 77:
            sexuality = "Bi/pansexual, prefers Femme"
        else:
            sexuality = "Bi/pansexual"
        #write sexuality
        char["Sexuality"] = sexuality

        #eye colour
        eyeColour = common.getRandom(self.eyeColours)
        char["Eye Colour"] = eyeColour

        #height difference from 163cm
        #this height is average for all humans born after 1960
        height = 165 + random.randint(-20,15)
        char["Height"] = str(height)

        #weight is taken from ideal weight wth variance in kg
        weight = 48 + 0.9 * (height - 152) + random.randint(-5,5)
        char["Weight"] = str(weight) + "kg"
        
        #handed
        h = random.randint(0,100)
        if h < 10:
            handed = "Ambidextrous"
        elif h < 85:
            handed = "Right Handed"
        else:
            handed = "Left Handed"
        #write handed
        char["Dominant Hand"] = handed

        #employment
        #fetch list of job files
        possibleJobs = common.findFilesInRange("Earth/Entity/Human/Jobs/", year)
        #grab random job from long list
        job = common.getRandom(possibleJobs)
        char["Employment"] = job

        #visual impairment
        v = random.randint(0,100) + int(age/5)
        if v < 75:
            vImpairment = 0
        elif v < 80:
            vImpairment = 1
        elif v < 85:
            vImpairment = 2
        elif v < 90:
            vImpairment = 3
        elif v < 95:
            vImpairment = 4
        else:
            vImpairment = 5
        #write out type of blindness
        if vImpairment == 0:
            char["Sight"] = self.visualCategory[vImpairment]
        elif vImpairment < 3:
            #visual impairment
            char["Sight"] = self.visualCategory[vImpairment-1]
            t = random.randint(0,100)
            if t < 42:
                char["Vision Impairment"] = self.visualImpairments[5]
            elif t < 75:
                char["Vision Impairment"] = self.visualImpairments[0]
            elif t < 77:
                char["Vision Impairment"] = self.visualImpairments[3]
            elif t < 78:
                char["Vision Impairment"] = self.visualImpairments[2]
            elif t < 79:
                char["Vision Impairment"] = self.visualImpairments[7]
            elif t < 80:
                char["Vision Impairment"] = self.visualImpairments[4]
            elif t < 81:
                char["Vision Impairment"] = self.visualImpairments[6]
            else:
                char["Vision Impairment"] = self.visualImpairments[8]
        else:
            #blindness
            char["Sight"] = self.visualCategory[vImpairment-1]
            t = random.randint(0,100)
            if t < 51:
                char["Vision Impairment"] = self.visualImpairments[0]
            elif t < 59:
                char["Vision Impairment"] = self.visualImpairments[1]
            elif t < 64:
                char["Vision Impairment"] = self.visualImpairments[2]
            elif t < 68:
                char["Vision Impairment"] = self.visualImpairments[3]
            elif t < 72:
                char["Vision Impairment"] = self.visualImpairments[4]
            elif t < 75:
                char["Vision Impairment"] = self.visualImpairments[5]
            elif t < 78:
                char["Vision Impairment"] = self.visualImpairments[6]
            elif t < 79:
                char["Vision Impairment"] = self.visualImpairments[7]
            else:
                char["Vision Impairment"] = self.visualImpairments[8]

        #voice
        vSpeed = random.randint(0,20)
        if vSpeed < 5:
            voiceSpeed = "Slow"
        elif vSpeed < 15:
            voiceSpeed = "Usual"
        else:
            voiceSpeed = "Fast"
        vPitch = random.randint(0,20)
        if vPitch < 5:
            voicePitch = "Low"
        elif vPitch < 15:
            voicePitch = "Usual"
        else:
            voicePitch = "High"
        vtone = random.randint(0,50)
        if vtone < 5:
            voiceTone = "Sarcastic"
        elif vtone < 10:
            voiceTone = "Soft"
        elif vtone < 15:
            voiceTone = "Kind"
        elif vtone < 20:
            voiceTone = "Measured"
        elif vtone < 25:
            voiceTone = "Harsh"
        elif vtone < 30:
            voiceTone = "Accented"
        elif vtone < 35:
            voiceTone = "Sad"
        elif vtone < 40:
            voiceTone = "Tired"
        else:
            voiceTone = "Normal"
        char["Voice"] = {"Speed": voiceSpeed, "Pitch": voicePitch, "Tone": voiceTone}

        #other sense impairments
        senses = ["Hearing", "Taste", "Smell", "Touch"]
        levels = ["Lesser/Numbed", "Confused", "Noisy", "No"]
        if random.randint(0,100) < 20:
            char["Other Sense Impairment"] = common.returnMultipleTwoPart(1, levels, senses)

        #skin marks
        s = random.randint(1,8)
        mark = ["Scar on", "Burn on", "Birthmark on"]
        char["Skin Marks"] = common.returnMultipleTwoPart(s, mark, self.bodyParts)

        #Physical distinction
        s = random.randint(-10,5)
        mark = ["Big", "Small", "Strong", "Weak", "Missing"]
        char["Physical Distinctions"] = common.returnMultipleTwoPart(s, mark, self.bodyParts)

        #family, parents
        char["Parents"] = common.getRandom(self.parents)

        #siblings
        p = random.randint(0,4)
        rela = ["Older", "Younger", "Older", "Younger", "Twin"]
        siblings = ["Brother", "Sister"]
        char["Siblings"] = common.returnMultipleTwoPart(p, rela, siblings)

        #phobias
        p = random.randint(1,6)
        char["Phobias"] = common.returnMultiple(p, self.phobias)

        #Formative Trauma
        p = random.randint(-1,5)
        char["Formative Traumas"] = common.returnMultiple(p, self.Traumas)

        #Economic Status
        #Poverty/Poor/Middle/Well Off/Wealthy/Rich/Ultra Rich Spectrum, Known/Unknown Family Name
        s = random.randint(0,100)
        if s < 10:
            status = "known Family Name"
            char["Family Status"] = "Known"
        else:
            status = "Unknown Family Name"
            char["Family Status"] = "Unknown"
        e = random.randint(0,1000)
        if e < 2:
            char["Economic Status"] = self.economicStatus[0]
        elif e < 80:
            char["Economic Status"] = self.economicStatus[1]
        elif e < 300:
            char["Economic Status"] = self.economicStatus[2]
        elif e < 550:
            char["Economic Status"] = self.economicStatus[3]
        elif e < 800:
            char["Economic Status"] = self.economicStatus[4]
        else:
            char["Economic Status"] = self.economicStatus[5]

        #criminal record
        #based off wealth level, more likely with less money
        c = random.randint(0, e)
        cr = []
        if c > 200:
            #criminal record
            p = random.randint(1,4)
            cr = common.returnMultiple(p, self.Crimes)
        char["Criminal Record"] = cr

        #Abilities/Talents/Natural Strengths
        
        #Other Medical History

        return char