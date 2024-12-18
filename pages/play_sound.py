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

# Function to fetch pronunciation using ResponsiveVoice (JavaScript approach)
def play_pronunciation_responsivevoice(word):
    # Embed the ResponsiveVoice script into Streamlit using components
    st.components.v1.html("""
    <script src="https://code.responsivevoice.org/responsivevoice.js?key=Ytp4Wvua"></script>
    <script>
        // Use the responsiveVoice JavaScript function to speak the word
        responsiveVoice.speak("{0}", "UK English Male");
    </script>
    """.format(word), height=0)  # Set height=0 to hide the script output

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
