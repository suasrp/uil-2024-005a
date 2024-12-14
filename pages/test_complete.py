import streamlit as st
from navigation import make_sidebar  # Import the sidebar function

# Add sidebar
make_sidebar()

# Display test completion header
st.write(
    """
# 🎉 Test Complete
    """
)

# Check if answers are stored in session state
if 'answers' in st.session_state:
    # Get selected letter and the test words from session state
    selected_letter = st.session_state.get("selected_letter", None)
    words = ALPHABET_TESTS.get(selected_letter, [])
    
    correct_answers = 0
    incorrect_answers = []

    # Check each answer
    for word in words:
        correct_word = word.lower()  # Assuming the correct word is the lowercase version
        user_answer = st.session_state.answers.get(word, "").lower()

        if user_answer == correct_word:
            correct_answers += 1
        else:
            incorrect_answers.append(word)

    # Display the result message
    total_words = len(words)
    if correct_answers == total_words:
        st.success(f"🎉 Congratulations! You got all the words correct! ({correct_answers}/{total_words})")
    else:
        st.warning(f"Test complete! You got {correct_answers}/{total_words} words correct.")
        st.write("Here are the words you missed:")

        # Display the list of incorrect answers
        for incorrect_word in incorrect_answers:
            st.write(f"- {incorrect_word}")

    # Option to retake the test for missed words
    if incorrect_answers:
        if st.button("Retake Missed Words"):
            st.session_state.answers = {}
            st.session_state.selected_words_for_retest = incorrect_answers
            st.experimental_rerun()

    # Option to retake the entire test
    if st.button("Retake Entire Test"):
        st.session_state.answers = {}
        st.session_state.selected_letter = None  # Clear selected letter
        st.experimental_rerun()

    # Button to go back to the home page
    if st.button("Go to Home"):
        st.session_state.selected_letter = None
        st.session_state.answers = {}  # Clear answers on home return
        st.experimental_rerun()

else:
    st.write("It seems like there was an issue with your test progress. Please try again.")
