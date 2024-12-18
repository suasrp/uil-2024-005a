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

# Function to fetch pronunciation using ResponsiveVoice API
def play_pronunciation_responsivevoice(word):
    api_url = f"https://code.responsivevoice.org/getvoice.php?t={word}&lang=en&engine=responsivevoice"
    
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            st.audio(response.content, format='audio/mp3')  # Playing the audio directly
        else:
            st.error(f"Error fetching pronunciation from ResponsiveVoice: {response.status_code}")
            st.write(response.text)
    except Exception as e:
        st.error(f"Error occurred while fetching pronunciation from ResponsiveVoice: {e}")

# Button to trigger pronunciation using ResponsiveVoice
if st.button("Pronounce Word (ResponsiveVoice)"):
    if current_word:
        play_pronunciation_responsivevoice(current_word)
    else:
        st.warning("No word selected for pronunciation. Please go back and select a word.")

# Button to navigate back to the test page
if st.button("Back to Test"):
    st.session_state.edit_mode = False  # Disable edit mode if needed
    st.experimental_rerun()
