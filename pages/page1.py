import streamlit as st
import pyttsx3
import openai
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

openai.api_key = "your_openai_api_key"

# Function for pronunciation using TTS
def pronounce_word(word):
    engine = pyttsx3.init()
    engine.say(word)
    engine.runAndWait()

# Function to get definition using OpenAI
def get_definition(word):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Define the word: {word}",
            max_tokens=50
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return "Error fetching definition."

# Function to get example sentence using OpenAI
def get_example_sentence(word):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Use the word '{word}' in a sentence.",
            max_tokens=50
        )
        return response.choices[0].text.strip()
    except Exception as e:
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
