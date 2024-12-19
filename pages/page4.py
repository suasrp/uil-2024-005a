import streamlit as st
import requests
from navigation import make_sidebar, check_user_inactivity  # Import necessary functions

# Check for inactivity and logout if necessary
check_user_inactivity()

# Add sidebar
make_sidebar()

########################################################################################

# Updated list of words
words = [
    "abandon", "absent", "absolute", "academy", "ache",
    "address", "adult", "afterglow", "against", "airliner", "alley", "allspice", "almond", "already", "alter",
    "ambition", "amusement", "ancestor", "annual", "apology", "appetite", "argue", "artist", "assign", "astronomer",
    "athlete", "autograph", "autumn", "awesome". "backpack", "badger", "bagel", "bait", "banana", "barefoot",
    "bark", "barley", "barrier", "baste", "beaver", "beehive", "beige", "beverage", "beware", "biology",
    "black hole", "blade", "blockage", "blueberry", "blurt", "blush", "borrow", "bottom", "bravery", "bridesmaid",
    "bridle", "bronco", "brownie", "building", "built-in", "buttermilk". "calm", "camel", "canine", "capsule", "California", 
    "cashew", "caterpillar", "catwalk", "cautious", "cement", "century", "champion", "charming", "cheerful", "childish",
    "chuckle", "circuit", "circulate", "citizenship", "climate", "coconut", "collection", "comma", "company", "compel",
    "computer", "concern", "condone", "copy", "cousin", "creakier", "creepy", "cricket", "curtsy", "custard".
    "dairy", "dazzled", "deaden", "decaf", "decent", "decimal", "decline", "dentist", "dependable", "desktop",
    "dessert", "develop", "diary", "dipper", "direction", "disappoint", "disease", "dishonest", "dismiss", "dispute",
    "distrust", "dizzy", "doggy", "dose", "downwind", "dramatic", "dribble", "drinkable", "drudge", "duet".
    "eagle", "earnings", "easiest", "easygoing", "echo", "economical", "edition", "educate", "eggplant", "either",
    "elderly", "electrify", "element", "elevator", "elude", "emotion", "empower", "enable", "ending", "energy",
    "entirely", "entrap", "entry", "error", "essay", "esteem", "ever", "example", "exchange", "exercise",
    "export", "eye-catching", "eyelash". "factual", "falcon", "famous", "farmstead", "faucet", "fearless", "ferret",
    "festival", "fidget", "field", "filmstrip", "fizzling", "flavor", "fleece", "foliage", "footstep", "foresight",
    "forestry", "formula", "forthright", "framed", "frank", "freaky", "frightful", "frown", "fudge", "funnel".
    "furry". "gadget", "gala", "galaxy", "garden", "garment", "garnish", "gathering", "generous", "genius",
    "gentlefolk", "geology", "German", "germfree", "giggle", "giraffe", "glassblower", "glimpse", "gloomy", "goalpost", "goggles",
    "gosling", "grader", "granite", "graph", "gravity", "gravy", "greedy", "griddle", "grime", "grungy",
    "guardian", "guide", "guitar", "gummy", "gusto". "hairdresser", "hallway", "halt", "handful", "handsaw",
    "hapless", "harmonica", "harp", "harvest", "hateful", "hawk", "headfirst", "healer", "heavenly", "hefty",
    "hemline", "heritage", "hipbone", "Hispanic", "history", "hoarse", "honorable", "hotel", "hottest", "housemaid", "humid",
    "hurricane", "hurried". "igloo", "illness", "image", "immune", "impact", "imprint", "imprison", "incoming",
    "index", "indigo", "infest", "inform", "inherit", "injury", "inkling", "inland", "inquest", "inscribe",
    "insertion", "insulate", "interest", "intrude", "inventive", "Irish", "iron", "irritate". "jabbed", "jacket", "jailbird",
    "janitor", "jawbone", "jelly", "journal", "June", "junior". "kennel", "keynote", "kidnap", "kindness", "kitty",
    "knuckle", "kook". "landing", "landscape", "larva", "lately", "latitude", "lavender", "lawyer", "leader",
    "leakage", "leap", "legally", "leotard", "liberty", "ligament", "light-footed", "likeness", "limiting", "linger",
    "lining", "listen", "liven", "lofty", "logbook", "longhorn", "loudness", "loveliness", "luminous", "lure",
    "lush". "machine", "magazine", "magical", "magnet", "majority", "mammoth", "manager", "marine", "massage",
    "massive", "mechanical", "medicine", "medley", "meow", "merge", "mermaid", "microwave", "migrant", "mineral",
    "mingled", "minimal", "misshapen", "mistletoe", "mistreat", "modest", "modify", "molasses", "muffler", "muscle",
    "mystery", "myth". "napkin", "narrate", "national", "naturalize", "nearby", "necessary", "necklace", "neglect",
    "nephew", "newlywed", "nineteenth", "noel", "noggin", "nomad", "nonfiction", "nonviolent", "normal", "nosebleed",
    "noted", "notion", "nourish", "novel", "noxious", "nudging", "numeric", "nunnery", "nuzzle", "nylon".
    "oarsman", "obsess", "obstinate", "obtain", "oddity", "offense", "oilcloth", "okra", "once", "oodles",
    "oozy", "operate", "opposite", "opt", "orbit", "ordeal", "ore", "organ", "origin", "ouch",
    "ounce", "outlandish", "outside", "overcome", "overripe", "ozone". "painful", "panic", "parasite", "parish",
    "particle", "pastry", "pasture", "patrolman", "peach", "peacock", "pecan", "pedicure", "percent", "perky",
    "perplex", "perspire", "phonics", "phrase", "physical", "pierce", "pledge", "pliable", "pointless", "positive",
    "poultice", "preacher", "precious", "predict", "priceless", "primary", "prosper", "proverb", "purebred". "quail",
    "quaint", "quart", "quash", "quest", "quibbling", "quilt", "quirk", "quite", "quoted". "radar",
    "radio", "raggedy", "raisin", "readable", "rebate", "recess", "recollect", "refashion", "regardful", "register",
    "release", "relic", "remedy", "reporter", "reptile", "respond", "retail", "retreat", "revenge", "rhino",
    "riflery", "romance", "rooster", "rotating", "rough", "rowdy", "ruby", "rudeness", "rust". "sacred",
    "salmon", "salute", "sarcastic", "sawdust", "scientist", "scorpion", "seamstress", "secretary", "seventh", "several",
    "shabbily", "sibling", "sketch", "slippery", "sluggish", "snoopy", "soccer", "soprano", "sourdough", "soybean",
    "spirited", "sponsor", "stadium", "stomach", "struggle", "subtract", "succeed", "suddenly", "superior", "syllable",
    "system". "tabulate", "talent", "tattered", "tattletale", "teethe", "tempting", "tennis", "term", "textbook",
    "thankfully", "theft", "thermostat", "thicken", "thievery", "throat", "thumbnail", "thunderbolt", "tickling", "timid",
    "together", "toughen", "tourism", "treasure", "tremor", "tribal", "trombone", "trouble", "tulip", "tuneful",
    "turmoil", "twitter", "typhoon". "umpire", "unable", "underhand", "underneath", "unfair", "unicorn", "uninstall",
    "unit", "universe", "unlisted", "unpleasant", "unseal", "unsure", "untangle", "upright", "upturn", "urban",
    "usable", "utterly". "vacate", "valor", "valuable", "variety", "vast", "vehicle", "venom", "verdict",
    "vibrant", "victor", "vinegar", "violence", "visiting", "visual", "vocal", "vowel", "voyage", "vulture".
    "wakeful", "waltz", "watermelon", "weather", "welcome", "westerly", "whitener", "wholesome", "wisdom", "worrisome",
    "writing". "xylem". "yank", "yardage", "yearly", "yoga", "youthful". "zap", "zest", "zookeeper"
]

# Create 26 tests (A-Z)
def create_tests(words_list):
    tests = {}
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        filtered_words = [word for word in words_list if word.startswith(letter)]
        tests[letter] = filtered_words
    return tests

tests = create_tests(words)

# Streamlit application
st.title("👍 3rd-4th Grade - Spelling Game")

def pronounce(word):
    # Embed the ResponsiveVoice script into Streamlit using components
    st.components.v1.html("""
    <script src="https://code.responsivevoice.org/responsivevoice.js?key=Ytp4Wvua"></script>
    <script>
        // Use the responsiveVoice JavaScript function to speak the word
        responsiveVoice.speak("{0}", "UK English Male");
    </script>
    """.format(word), height=0)  # Set height=0 to hide the script output

# Select test
letter = st.sidebar.selectbox("Select a letter:", list(tests.keys()))
words_to_test = tests[letter]

# Initialize session state for tracking the current word index
if 'current_word_index' not in st.session_state:
    st.session_state.current_word_index = 0
    st.session_state.score = 0
    st.session_state.last_pronounced = None

# Get the current word based on the index
current_word_index = st.session_state.current_word_index

# Show the current word
if current_word_index < len(words_to_test):
    current_word = words_to_test[current_word_index]

    st.subheader("Spell the word:")
    st.write("(The word will be pronounced now)")

    # Automatically pronounce the next word if it was just submitted
    if st.session_state.last_pronounced != current_word:
        audio_file = pronounce(current_word)
        if audio_file:
            st.audio(audio_file, format='audio/mp3')
        st.session_state.last_pronounced = current_word

    user_input = st.text_input(f"Your answer for '{current_word}':")
    
    if st.button("Submit"):
        if user_input.strip().lower() == current_word:
            st.success("Correct!")
            st.session_state.score += 1
        else:
            st.error(f"Incorrect! The correct spelling is: {current_word}")

        # Move to the next word
        st.session_state.current_word_index += 1

        # Reset the pronunciation tracker for the next word
        st.session_state.last_pronounced = None

        # If at the end, reset or display the final score
        if st.session_state.current_word_index >= len(words_to_test):
            st.write(f"Your total score is: {st.session_state.score} / {len(words_to_test)}")
            if st.button("Restart"):
                st.session_state.current_word_index = 0
                st.session_state.score = 0
else:
    st.write(f"Your total score is: {st.session_state.score} / {len(words_to_test)}")
    if st.button("Restart"):
        st.session_state.current_word_index = 0
        st.session_state.score = 0
        
###########################################################################
