import streamlit as st
import requests
from navigation import make_sidebar  # Import sidebar function

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

# Function for pronunciation using Llama3 or Phi3
def pronounce_word(word):
    url = f"https://api.llama3.com/tts?text={word}&voice=en_us_male"  # Replace with real free API
    response = requests.get(url)
    if response.status_code == 200:
        st.audio(response.content, format='audio/mp3')
    else:
        st.error("Error fetching pronunciation.")

# Function to get definition using Llama3 or Phi3
def get_definition(word):
    url = f"https://api.phi3.com/definition?word={word}"  # Replace with real free API
    response = requests.get(url)
    if response.status_code == 200:
        definition = response.json().get("definition", "No definition found.")
        return definition
    else:
        return "Error fetching definition."

# Function to get example sentence using Llama3 or Phi3
def get_example_sentence(word):
    url = f"https://api.phi3.com/example?word={word}"  # Replace with real free API
    response = requests.get(url)
    if response.status_code == 200:
        example = response.json().get("example", "No example sentence found.")
        return example
    else:
        return "Error fetching example sentence."

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

# Pronounce word
if st.button("Pronounce"):
    pronounce_word(word)

# Get definition
if st.button("Get Definition"):
    definition = get_definition(word)
    st.write(definition)

# Get example sentence
if st.button("Get Example Sentence"):
    example_sentence = get_example_sentence(word)
    st.write(example_sentence)
