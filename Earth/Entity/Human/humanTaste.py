import random
import common

class humanTaste:
    def __init__(self):
        self.bookGenres = common.getListFile("Earth/Entity/Human/Lists/LiteratureGenres")
        self.Colours = common.getListFile("Earth/Entity/Human/Lists/Colours")
        
        self.drugTypes = ["Stimulants", "Depressants", "Narcotic Analgesics", "Hallucinogenics", 
            "Dissociatives", "Cannabis", "Fully Sober"]

    def musicSpectrum(self, x):
        if x < 45:
            return "/100 Low"
        elif x < 55:
            return "/100 Mid"
        else:
            return "/100 High"

    def makeTaste(self, char):
        # music
        # Arousal, Valence, Depth, Interest
        a = random.randint(0,100)
        v = random.randint(0,100)
        d = random.randint(0,100)
        i = random.randint(0,100)
        char["Music Taste"] = {
            "Arousal/Energy" : str(a) + self.musicSpectrum(a),
            "Valence/Emotionality" : str(v) + self.musicSpectrum(v),
            "Depth/Complexity": str(d) + self.musicSpectrum(d),
            "Interest" : str(i) + self.musicSpectrum(i)
        }

        #books/magazines
        char["Literature Taste"] = common.returnMultiple(random.randint(-2,6), self.bookGenres)

        #favourite colour
        char["Favourite Colours"] = common.returnMultiple(random.randint(1,4), self.Colours)

        #clothes

        #jewelry

        #crowds/groups

        #food

        #drugs
        char["Preferred Drug Type"] = common.getRandom(self.drugTypes)

        #idols/peers
