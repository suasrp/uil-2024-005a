from navigation import make_sidebar
import streamlit as st

make_sidebar()

st.write(
    """
# 👍 6th Grade - Spelling Game

Let's have some spelling fun!

"""

)


# Updated list of words
words = [
    "abbreviate", "abnormality", "abode", "abrasion", "abundantly", "academic",
    "accessory", "accordion", "acidic", "acne", "acrobat", "adhesive",
    "admirable", "adoption", "adversary", "affected", "affliction", "affordable",
    "agenda", "airport", "alimony", "allergic", "alliance", "alpaca",
    "alphabetical", "amateur", "amplify", "amusing", "animate", "anklebone",
    "annex", "antibacterial", "antibiotic", "anxiety", "apparition", "appease",
    "applause", "aptitude", "aquamarine", "arcade", "arrangement", "assortment",
    "athletic", "attractive", "auditory", "avalanche", "avocado",
    "badminton", "balky", "Ballyhoo", "barbarian", "bareback", "bargain", "barrette",
    "bashfulness", "beacon", "bedazzle", "bedridden", "beforehand", "behavior",
    "believable", "beneficial", "benevolent", "biannual", "bicultural", "bicycle",
    "billionaire", "bimonthly", "biodiversity", "bionics", "birthmark", "blamable",
    "blarney", "blissful", "blistering", "bluebonnet", "bolster", "bonfire",
    "boomerang", "botulism", "boulevard", "bountiful", "braggart", "braille",
    "brainstorm", "brilliance", "brisket", "brooch", "buffered", "buffoonery",
    "bulbous", "bureau", "burglarize",
    "calculate", "calendar", "canopy", "capitalism", "cardiac", "carnation", "cartridge",
    "cataract", "cavernous", "centimeter", "ceremony", "chaplain", "charitable", "choppiness",
    "cinema", "circulation", "circumstance", "clearance", "clergy", "clincher", "closure",
    "cohesion", "coincidence", "colander", "columnist", "combustion", "commercial",
    "communicable", "commute", "complaint", "concentrate", "concerto", "confirmed",
    "congratulate", "connection", "connive", "consultation", "convention", "convoy", "corrode",
    "corruption", "cramming", "creative", "critical", "curiosity", "currency", "curtail",
    "damask", "dauntless", "debonair", "debt", "decagon", "deceit", "declining", "deductible",
    "deflate", "deformity", "dehydrate", "delivery", "democracy", "deodorant", "desperate", 
    "detestable", "development", "devotion", "diagram", "dictation", "dietary", "diligent",
    "diorama", "discipline", "discreet", "disembark", "disinfect", "dispensable", "disregard",
    "district", "divergence", "doleful", "domain", "dominance", "dosage", "downcast", 
    "draftsman", "drone", "dumpling", "dwindle", "dynasty",
    "earliest", "earphone", "earsplitting", "editorial", "effective", "egoism", "elaborate", 
    "elapse", "elasticity", "electromagnet", "eligible", "emanate", "embroidery", "emergency", 
    "emotional", "employee", "encore", "endear", "endurance", "energetic", "engagement", 
    "enjoyably", "enormity", "entirety", "environment", "episode", "equate", "erase", 
    "escapism", "estimate", "ethical", "everglade", "evict", "evidence", "excel", "exercising", 
    "exhale", "existence", "expenditure", "experience", "exploration", "expound", "extremity",
    "fabulous", "facedown", "factorization", "famish", "fanciful", "fatalism", "fattened", 
    "federalist", "feminine", "ferocious", "fiberglass", "fictionalize", "fidelity", "fiercely",
    "filbert", "filtration", "flagrant", "flatterer", "flounce", "food chain", "footbridge", 
    "foreclose", "foreign", "forerunner", "forgery", "forgetfulness", "formative", "fortitude",
    "foyer", "fraction", "fragile", "fragrance", "frankfurter", "fraternity", "freebie",
    "freedbee", "freedom", "frontier", "functional", "funeral", "furlough", "fuzziness",
    "gangplank", "gasoline", "gaudy", "gauze", "gearless", "gemstone", "generality", 
    "generation", "genetic", "geographical", "geometric", "giddy", "gingerly", "glacier", 
    "gloominess", "gluttony", "goldenrod", "good-humored", "goodwill", "gooseneck", 
    "gorgeous", "govern", "gradually", "graffiti", "granola", "graphic", "gravitation", 
    "greasier", "greatness", "greengrocer", "griminess", "grinning", "grizzled", "grouchy", 
    "guidance", "guidebook", "gumbo", "gurgle",
    "habitable", "haggard", "hamstring", "handicapped", "handily", "handlebar", "happiness",
    "happy-go-lucky", "harmfully", "hatchery", "hauntingly", "heatedly", "heather",
    "heatstroke", "hedgehog", "heighten", "henceforth", "hepatitis", "herbicide","hexagon", 
    "hibachi", "hideous", "hindrance", "hoist", "hominid", "homophone", "honeycomb", 
    "hoopskirt", "horoscope", "hotheaded", "hovercraft", "humidity", "hummingbird", 
    "husbandry", "hydrology", "hyena", "hygienic", "hyphen", "hypnosis", "hysterics",
    "icicle", "idealism", "identical", "ideology", "ignoring", "illegal", "imaginable", 
    "imitative", "immense", "immodest", "immovable", "impassable", "impeach", "impossible", 
    "improper", "improvise", "incidence", "incision", "inconvenience", "indecision", 
    "independent", "indicator", "inedible", "infatuate", "inferior", "inherent", 
    "injustice", "innovative", "instructor", "insulation", "insurance", "interesting", 
    "intermittent", "internist", "intrusive", "inventory", "invigorate", "invitation", 
    "irrational", "irrigation", "issue",
    "jaguar", "jamboree", "jawbreaker", "jellyfish", "jetty", "jitterbug", "jobholder", 
    "joggled", "joist", "jubilation", "juniper", "justify",
    "kelp", "kernel", "kidney", "kindhearted", "kinship", "Kleenex", "knighthood", 
    "knitting", "knockabout",
    "laboratory", "lacerate", "lamentation", "laminate", "landline", "languid", "larceny", 
    "lattice", "lawlessly", "layette", "league", "leastwise", "leathery", "lectern", 
    "leeway", "legality", "legislature", "leisure", "lemon", "levelheaded",
    "licorice", "lifeline", "light-year", "limerick", "lineage", "liquefy",
    "listener", "lobbyist", "locality", "loneliness", "loose", "lottery", "loudmouth",
    "lumberyard", "luminescent", "luxurious", "lynx",
    "magnetic", "magnolia", "mainstream", "maize", "malefactor", "malformation", 
    "malicious", "manageable", "marathon", "mascara", "masterful", "materialize", 
    "maturity", "maximum", "Maya", "meaningful", "medication", "meditative", "melodrama", 
    "membrane", "memorial", "mercenary", "merchant", "metallic", "meteorologist", 
    "migratory", "miniature", "minivan", "minority", "misconception", "misguidance", 
    "misspend", "mistletoe", "mistrust", "monitor", "monotone", "mosquito", "motley", 
    "multitude", "murmur", "mutate",
    "nape", "narcotic", "narrator", "nationalism", "natural resource", "navigable", 
    "navigator", "necessitate", "needful", "neglectful", "negotiate", "neighborhood", 
    "nervy", "nethermost", "nettle", "neutralize", "newcomer", "newspaperman", "nifty", 
    "nightly", "ninepin", "nitpick", "noiseless", "nonchalant", "nonprofit", "nonsense", 
    "nonverbal", "nonviolence", "normalize", "northeasterly", "nostalgic", "notoriety", 
    "nougat", "novitiate", "nozzle", "nuisance", "numeral", "nurturant", "nuthatch", 
    "nutlet", "nutriment",
    "obese", "obeying", "obituary", "oblivious", "obscure", "observant", "obviously",
    "occupation", "odometer", "Offertory", "officiate", "olive", "ominous", "onslaught", 
    "opacity", "openhearted", "operating", "opposable", "optimal", "optometry", "orate", 
    "orbiter", "orderliness", "ordinary", "oregano", "organic", "original", "ornery", 
    "outburst", "outlying", "outwardly", "outweigh", "overestimate", "override", 
    "oversupply", "oxygen",
    "packaging", "palpitate", "panhandle", "paradise", "paradox", "parakeet", "paralysis",
    "pathogen", "patriotic", "pedestal", "pedicure", "penalize", "penetrate", "penitence", 
    "pepperoni", "percentage", "perfection", "perilous", "perplexity", "pesticide", 
    "petroleum", "pictorial", "pineapple", "pinkie", "pinky", "plaintiff", "plasticity", 
    "poisonous", "policyholder", "polyester", "portable", "portfolio", "possession", 
    "practical", "precinct", "predestine", "predicament", "proactive", "problematic", 
    "proceed", "profession", "prosperous", "puzzling",
    "quaintness", "qualm", "quarantine", "quarterback", "queasier", "quick bread",
    "quince", "quitting", "quizzes",
    "racketeer", "radiantly", "radical", "railroad", "ramshackle", "raspy", "rationale", 
    "realistic", "reasoning", "reassure", "rebroadcast", "rebuttal", "receive", 
    "recession", "reconcile", "reconstruct", "rectangular", "reference", "refrigerate", 
    "regardless", "regiment", "relentless", "relevant", "reluctantly", "remnant", 
    "replacement", "replica", "reptilian", "respectable", "restaurant", "retort", 
    "retriever", "revenue", "review", "ricotta", "ridiculous", "roadrunner", "rodent", 
    "rollicking", "roughneck", "rowdiness", "rubella", "russet",
    "sabotage", "salsa", "sarcasm", "satisfactory", "scandal", "scarcely", "schedule", 
    "scorekeeper", "scourge", "seasonable", "seclusion", "sectional", "sedative", 
    "seizure", "semiarid", "sensational", "seriously", "seventh", "shrewd", "siesta", 
    "simplicity", "singular", "situation", "skittish", "sociable", "solidify", "solstice",
    "specific", "spectacle", "spectrum", "splendid", "squirm", "statement", "stationary", 
    "stereotype", "strategy", "stubborn", "subjective", "substantial", "summary", 
    "supplement", "survive", "syllabicate", "symbolism", "synthetic",
    "taffeta", "talkative", "tastefully", "taxation", "technician", "telescopic", 
    "temperament", "tension", "terrier", "terrific", "textual", "theatrical", "thermometer", 
    "thesis", "threaten", "thwart", "tightwad", "timberline", "tincture", "tinsel", 
    "toilsome", "tollgate", "tomorrow", "topical", "tousle", "toxemia", "tragedy", 
    "translate", "treasurer", "tremendous", "triangular", "trophy", "trustworthy", 
    "tunnel", "turbojet", "twentieth", "typewriter", "typify",
    "ultima", "unaffected", "unaligned", "unbearable", "unblemished", "unclassified", 
    "underpass", "unenclosed", "uneventful", "uniformity", "university", "unlined", 
    "unplug", "unravel", "unutterable", "uproarious", "usage", "uttermost",
    "vaccinate", "validity", "vandalism", "vanquish", "vaporize", "vegetative", "velocity", 
    "vendetta", "veneer", "venture", "Venus", "version", "veterinarian", "victimize", 
    "vigilant", "vindicate", "visitation", "vitality", "vivid", "vocation", "volcanic", 
    "volume",
    "waistband", "wallaby", "warehouse", "warrant", "wash-and-wear", "waspish", "wearable",
    "web-footed", "wharf", "wheelchair", "wherefore", "white blood cell", "whitening", 
    "wireless", "wisecrack", "wittingly", "woozy", "workmanship",
    "xylophone",
    "yacht", "yearling",
    # ... add all other words here ...
    "zealous", "zestfully"
]

# Create tests
def create_tests(words_list):
    tests = {}
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        filtered_words = [word for word in words_list if word.startswith(letter)]
        tests[letter] = filtered_words
    return tests

tests = create_tests(words)

class SpellingApp:
    def __init__(self):
        self.score = 0
        self.incorrect_words = set()
        self.current_word = None
        self.words_to_test = []
        self.current_index = 0

    def display_main_menu(self):
        st.title("Spelling Test")
        st.button("Start Test", on_click=self.select_test)
        st.button("View Words", on_click=self.view_words)

    def select_test(self):
        letter = st.selectbox("Select a letter for the test:", list(tests.keys()))
        self.words_to_test = tests[letter]
        self.current_index = 0
        self.score = 0
        self.start_test()

    def start_test(self):
        if self.current_index < len(self.words_to_test):
            self.current_word = self.words_to_test[self.current_index]
            st.write(f"Spell the word: **{self.current_word}**")
            self.play_audio(self.current_word)
            user_input = st.text_input("Your answer:", "")
            if st.button("Submit"):
                self.check_spelling(user_input)
        else:
            st.write(f"Test complete! Your score: {self.score} / {len(self.words_to_test)}")
            self.display_main_menu()

    def check_spelling(self, user_input):
        if user_input.lower() == self.current_word.lower():
            self.score += 1
            st.success("Correct!")
        else:
            self.incorrect_words.add(self.current_word)
            st.error(f"Incorrect! The correct spelling is: {self.current_word}")
        
        self.current_index += 1
        self.start_test()

    def play_audio(self, text):
        tts = gTTS(text=text, lang='en')
        audio_file = io.BytesIO()
        tts.save(audio_file)
        audio_file.seek(0)
        st.audio(audio_file, format='audio/mp3')

# Initialize the application
app = SpellingApp()
app.display_main_menu()

