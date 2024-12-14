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

# Button to play pronunciation via a free API like Llama3, Phi3, or other GPT-based API
# Example: Using an external service for free pronunciation, replace with real API if available

def play_pronunciation(word):
    # Example URL for free pronunciation API (replace with actual working API)
    # Llama3, Phi3, or Free GPT API may provide pronunciation features
    api_url = f"https://api.some-free-pronunciation-service.com/pronounce?word={word}"

    # Send request to pronunciation API
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            audio_url = response.json().get('audio_url', None)
            if audio_url:
                # Use the audio URL to play the pronunciation
                st.audio(audio_url, format='audio/mp3')
            else:
                st.error("Pronunciation audio not available.")
        else:
            st.error("Failed to fetch pronunciation.")
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
