import streamlit as st
import requests
from navigation import make_sidebar  # Import the sidebar function

# Add sidebar
make_sidebar()

# Title for the Play Sound page
st.write(
    """
# 🔊 Pronunciation of the Word
    """
)

# Initialize session state for the current word if not already set
if 'current_word' not in st.session_state:
    st.session_state.current_word = ''

# Display the current word for pronunciation
current_word = st.session_state.current_word

if current_word:
    st.write(f"The word to pronounce is: **{current_word}**")
else:
    st.write("No word selected for pronunciation.")

# Function to fetch pronunciation via ElevenLabs API
def play_pronunciation(word):
    api_url = "https://api.elevenlabs.io/v1/text-to-speech"  # Replace with actual ElevenLabs API endpoint if needed

    headers = {
        'Authorization': 'Bearer sk_llx-12345678901234567890123456789012345678901234',  # ElevenLabs API key
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

# Button to trigger pronunciation
if st.button("Pronounce Word"):
    if current_word:
        play_pronunciation(current_word)
    else:
        st.warning("No word selected for pronunciation. Please go back and select a word.")

# Button to navigate back to the test page
if st.button("Back to Test"):
    st.session_state.edit_mode = False  # Disable edit mode if needed
    st.experimental_rerun()
