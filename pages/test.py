import streamlit as st
from navigation import make_sidebar, check_user_inactivity  # Import the sidebar function

# Check for inactivity and logout if necessary
check_user_inactivity()

# Add sidebar
make_sidebar()

# Initialize session state for tracking answers (if not already initialized)
if 'answers' not in st.session_state:
    st.session_state.answers = {}

# Fetch the selected letter from session state (passed from select_test.py)
selected_letter = st.session_state.get("selected_letter", None)

# Display header
st.write(
    """
# 📝 Test for 5th-6th Grade - Selected Letter Words
    """
)

# Ensure a letter is selected before proceeding
if selected_letter:
    st.write(f"Testing words for the letter **{selected_letter.upper()}**")

    # Get the list of words for the selected letter (this should match your test data structure)
    words = ALPHABET_TESTS.get(selected_letter, [])

    # Iterate over the words and create the test UI
    for word in words:
        # Display word
        st.subheader(f"Word: {word}")

        # Input for user answer
        user_answer = st.text_input(f"Your answer for '{word}'", key=f"{word}_answer")

        # Store the user's answer in the session state
        if user_answer:
            st.session_state.answers[word] = user_answer

        # Pronounce the word (integrate API here)
        if st.button(f"Pronounce '{word}'", key=f"{word}_pronounce"):
            st.write(f"Pronouncing: {word}...")
            # Example API integration for pronunciation (replace with actual call to Llama3/Phi3)
            # You can call your API here and play the audio
            # pronounce_word(word)

        # Get definition of the word (integrate API here)
        if st.button(f"Get Definition of '{word}'", key=f"{word}_definition"):
            st.write(f"Getting definition for: {word}...")
            # Example API integration for definition (replace with actual call to Llama3/Phi3)
            # Replace with actual API call to fetch definition
            definition = "This is a mock definition of the word."  # Replace with API call
            st.write(f"Definition: {definition}")

        # Get an example sentence for the word (integrate API here)
        if st.button(f"Get Example Sentence for '{word}'", key=f"{word}_example"):
            st.write(f"Getting example sentence for: {word}...")
            # Example API integration for example sentences (replace with actual call to Llama3/Phi3)
            # Replace with actual API call to fetch example sentence
            example_sentence = "This is a mock example sentence."  # Replace with API call
            st.write(f"Example sentence: {example_sentence}")

    # Show user's answers after they finish the test
    if st.button("Submit Test"):
        st.write("Your Answers:")
        for word, answer in st.session_state.answers.items():
            st.write(f"{word}: {answer}")

    # Option to retake the test
    if st.button("Retake Test"):
        # Clear answers and reset the session state for the test
        st.session_state.answers = {}
        st.experimental_rerun()

else:
    st.write("Please select a letter from the previous page to begin the test.")
