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

# Fetch pronunciation using LlamaCloud API
def play_pronunciation(word):
    api_url = f"https://api.llamacloud.com/v1/speech/pronounce?word={word}"  # Replace with real free API
    headers = {
            'Authorization': 'Bearer llx-qzM2fHBXD6hl2xyeRS6JzJafF2mKviaxtTJxWdY6nIAouF7a',
        }

    response = requests.get(api_url)
    if response.status_code == 200:
        st.audio(response.content, format='audio/mp3')
    else:
        st.error("Error fetching pronunciation.")

# Function to get definition using Hugging Face API
def get_definition(word):
    api_url = f"https://api-inference.huggingface.co/models/bert-base-uncased"
    headers = {
        'Authorization': 'Bearer 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',
    }
    
    response = requests.get(api_url)
    if response.status_code == 200:
        definition = response.json().get("definition", "No definition found.")
        return definition
    else:
        return "Error fetching definition."

# Function to get example sentence using Hugging Face API
def get_example_sentence(word):
    api_url = f"https://api-inference.huggingface.co/models/bert-base-uncased"
    headers = {
        'Authorization': 'Bearer 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',
    }
    
    response = requests.get(api_url)
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
if st.button("Pronounce word"):
    play_pronunciation(word)

# Get definition
if st.button("Get Definition"):
    definition = get_definition(word)
    st.write(definition)

# Get example sentence
if st.button("Get Example Sentence"):
    example_sentence = get_example_sentence(word)
    st.write(example_sentence)
