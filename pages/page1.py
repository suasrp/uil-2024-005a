import streamlit as st
import requests
from navigation import make_sidebar, check_user_inactivity  # Import necessary functions and sidebar functions

# Check for inactivity and logout if necessary
check_user_inactivity()

# Add sidebar
make_sidebar()

# Example words list (Replace with your dynamic word list)
ALPHABET_TESTS = {
    'a': ["abbreviate", "abnormality"],
    'b': ["badminton", "balky"],
    'c': ["calculate", "calendar"],
    'd': ["damask", "dauntless"],
    # Add more letters and words...
}


## Fetch pronunciation using ResponsiveVoice (JavaScript approach)
#def play_pronunciation_responsivevoice(word):
    ## Embed the ResponsiveVoice script into Streamlit using components
    #st.components.v1.html("""
    #<script src="https://code.responsivevoice.org/responsivevoice.js?key=Ytp4Wvua"></script>
    #<script>
        #// Use the responsiveVoice JavaScript function to speak the word
        #responsiveVoice.speak("{0}", "UK English Male");
    #</script>
    #""".format(word), height=0)  # Set height=0 to hide the script output


# Streamlit interface for the test
st.write(
    """
 #📝 5th-6th Grade - List of Words
    'a': ["abbreviate", "abnormality"],
    'b': ["badminton", "balky"],
    'c': ["calculate", "calendar"],
    'd': ["damask", "dauntless"],
    """
)

st.title("Alphabet Spelling Test")

#################################################################################

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

def view_words(self):
    st.title("List of Words")
    for letter, word_list in tests.items():
        st.subheader(f"Words starting with '{letter.upper()}':")
        st.write(", ".join(word_list))
    st.button("Back to Main Menu", on_click=self.display_main_menu)

#################################################################################

#letter = st.selectbox("Choose a letter", list(ALPHABET_TESTS.keys()))
#word_list = ALPHABET_TESTS[letter]

#word = st.selectbox("Choose a word", word_list)

## Pronounce word using ElevenLabs
#if st.button("Pronounce word (ElevenLabs)"):
    #play_pronunciation_elevenlabs(word)

## Pronounce word using ResponsiveVoice
#if st.button("Pronounce word (ResponsiveVoice)"):
    #play_pronunciation_responsivevoice(word)

## Get definition
#if st.button("Get Definition"):
    #definition = get_definition(word)
    #st.write(definition)

## Get example sentence
#if st.button("Get Example Sentence"):
    #example_sentence = get_example_sentence(word)
    #st.write(example_sentence)
