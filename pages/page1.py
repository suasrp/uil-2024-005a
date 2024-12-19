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


## Streamlit interface for the test
st.write(
    """
## 📝 5th-6th Grade - List of Words
    """
)

st.title("Alphabet Spelling Test")

#################################################################################

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
