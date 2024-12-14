import streamlit as st
from navigation import make_sidebar  # Import sidebar function

# Add sidebar
make_sidebar()

# Example alphabet test data (replace this with the actual test data)
ALPHABET_TESTS = {
    'a': ["abbreviate", "abnormality"],
    'b': ["badminton", "balky"],
    'c': ["calculate", "calendar"],
    'd': ["damask", "dauntless"],
    'e': ["earliest", "earphone"],
    'f': ["fabulous", "facedown"],
    'g': ["gangplank", "gasoline"],
    'h': ["habitable", "haggard"],
    'i': ["impressive", "illusion"],
    'j': ["jaguar", "jamboree"],
    'k': ["kelp", "kernel", "kidney", "kindhearted", "kinship", "Kleenex"],
    'l': ["laboratory", "lacerate"],
    'm': ["magnetic", "magnolia"],
    'n': ["nape", "narcotic"],
    'o': ["obese", "obeying"],
    'p': ["packaging", "palpitate"],
    'q': ["quaintness", "qualm"],
    'r': ["racketeer", "radiantly"],
    's': ["sabotage", "salsa"],
    't': ["taffeta", "talkative"],
    'u': ["ultima", "unaffected"],
    'v': ["vaccinate", "validity"],
    'w': ["waistband", "wallaby"],
    'x': ["xylophone"],
    'y': ["yacht", "yearling"],
    'z': ["zealous", "zestfully"]
}

# Streamlit UI
st.write(
    """
# 📝 5th-6th Grade - List of Words
    """
)

# Sidebar for selecting the test
st.title("Select Your Test")
letter = st.selectbox("Select a Letter", list(ALPHABET_TESTS.keys()))  # User selects letter
st.write(f"Selected Test: {letter.upper()}")

# Display the words for the selected letter
words = ALPHABET_TESTS[letter]
st.write(f"Words in this test: {', '.join(words)}")

# Show test details
st.write(f"Test for the letter **{letter.upper()}** includes these words.")

# Option to start test for the selected letter
if st.button("Start Test"):
    # Redirect the user to the test page with the selected letter
    st.session_state.selected_letter = letter  # Store the selected letter for use in the test
    st.write(f"Now starting the test for the letter **{letter.upper()}**.")
    st.write("Proceed to the next step for the test!")
    # Redirect to the test page (For example, `page1.py`)
    st.experimental_rerun()  # This could also be replaced with an actual redirect if needed

# Option to view the word definitions and pronunciation (optional)
st.write("Want to hear the words and get definitions? Use the buttons below!")

# Example buttons to get definitions, pronunciation, or examples for a selected word
selected_word = st.selectbox("Choose a word to get more information", words)

# Display buttons for additional features (Pronounce, Get Definition, Get Example Sentence)
if st.button(f"Pronounce '{selected_word}'"):
    # Replace this with the pronunciation functionality
    # For now, we’ll simulate this step. You can replace this with the Llama3 or Phi3 APIs.
    st.write(f"Pronouncing {selected_word}...")
    # Pronounce function can be integrated here
    # For example: pronounce_word(selected_word)

if st.button(f"Get Definition of '{selected_word}'"):
    # Replace this with the definition-fetching functionality
    # Call the API or fetch the definition of the word
    definition = "This is a mock definition of the word."  # Replace with API call
    st.write(f"Definition of {selected_word}: {definition}")
    
if st.button(f"Get Example Sentence for '{selected_word}'"):
    # Replace this with the example sentence functionality
    # Fetch an example sentence for the word
    example_sentence = "This is a mock example sentence."  # Replace with API call
    st.write(f"Example sentence for {selected_word}: {example_sentence}")
