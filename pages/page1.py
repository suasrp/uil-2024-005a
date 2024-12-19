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

# Fetch pronunciation using ElevenLabs API
def play_pronunciation_elevenlabs(word):
    api_url = "https://api.elevenlabs.io/v1/text-to-speech"  # Replace with actual ElevenLabs API endpoint if needed
    headers = {
        'Authorization': 'Bearer sk_0da51f2e22e6df77ffd9477976e0d683b88ebcd3571dd99a',  # ElevenLabs API key
        'Content-Type': 'application/json'
    }

    data = {
        "text": word,  # The word to be pronounced
        "voice": "en_us_male",  # Select the voice if needed
        "output_format": "mp3"
    }

    try:
        response = requests.post(api_url, json=data, headers=headers)
        if response.status_code == 200:
            st.audio(response.content, format='audio/mp3')
        else:
            st.error(f"Error fetching pronunciation: {response.status_code}")
            st.write(response.text)
    except Exception as e:
        st.error(f"Error occurred while fetching pronunciation: {e}")

# Fetch pronunciation using ResponsiveVoice (JavaScript approach)
def play_pronunciation_responsivevoice(word):
    # Embed the ResponsiveVoice script into Streamlit using components
    st.components.v1.html("""
    <script src="https://code.responsivevoice.org/responsivevoice.js?key=Ytp4Wvua"></script>
    <script>
        // Use the responsiveVoice JavaScript function to speak the word
        responsiveVoice.speak("{0}", "UK English Male");
    </script>
    """.format(word), height=0)  # Set height=0 to hide the script output

# Function to get definition using Wordnik API
def get_definition(word):
    api_url = f"https://api.wordnik.com/v4/word.json/{word}/definitions"
    headers = {
        'Authorization': 'Bearer cfkfozedk4amxz92tyh1boi833dv7t881s8df9aqvy5e5261h',  # Wordnik API key
    }

    try:
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            definitions = response.json()
            if definitions:
                return definitions[0].get("text", "No definition found.")
            else:
                return "No definition found."
        else:
            return f"Error fetching definition: {response.status_code}"
    except Exception as e:
        return f"Error occurred while fetching definition: {e}"

# Function to get example sentence using Wordnik API
def get_example_sentence(word):
    api_url = f"https://api.wordnik.com/v4/word.json/{word}/examples"
    headers = {
        'Authorization': 'Bearer cfkfozedk4amxz92tyh1boi833dv7t881s8df9aqvy5e5261h',  # Wordnik API key
    }

    try:
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            examples = response.json().get('examples', [])
            if examples:
                return examples[0].get("text", "No example sentence found.")
            else:
                return "No example sentence found."
        else:
            return f"Error fetching example sentence: {response.status_code}"
    except Exception as e:
        return f"Error occurred while fetching example sentence: {e}"

# Streamlit interface for the test
st.write(
    """
# 📝 5th-6th Grade - List of Words
    """
)

st.title("Alphabet Spelling Test")

letter = st.selectbox("Choose a letter", list(ALPHABET_TESTS.keys()))
word_list = ALPHABET_TESTS[letter]

word = st.selectbox("Choose a word", word_list)

# Pronounce word using ElevenLabs
if st.button("Pronounce word (ElevenLabs)"):
    play_pronunciation_elevenlabs(word)

# Pronounce word using ResponsiveVoice
if st.button("Pronounce word (ResponsiveVoice)"):
    play_pronunciation_responsivevoice(word)

# Get definition
if st.button("Get Definition"):
    definition = get_definition(word)
    st.write(definition)

# Get example sentence
if st.button("Get Example Sentence"):
    example_sentence = get_example_sentence(word)
    st.write(example_sentence)
