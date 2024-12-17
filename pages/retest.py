import streamlit as st
from navigation import make_sidebar, check_user_inactivity  # Import the sidebar function

# Check for inactivity and logout if necessary
check_user_inactivity()

# Add sidebar
make_sidebar()

# Title for the retake page
st.write(
    """
# 🔄 Retake Test for Missed Words
    """
)

# Check if the user has missed words in session state
if 'selected_words_for_retest' in st.session_state and st.session_state.selected_words_for_retest:
    missed_words = st.session_state.selected_words_for_retest
    if missed_words:
        # Show the current word to spell
        current_word = missed_words[0]  # Get the first missed word for retesting

        # Show instructions
        st.write(f"**Spell the word: {current_word}**")

        # Form to input answer
        user_input = st.text_input("Your Answer", "", key="user_input")

        # Handle form submission
        if user_input:
            # Check if the answer is correct
            correct_word = current_word.lower()
            if user_input.lower() == correct_word:
                # Correct answer: remove word from missed words list
                missed_words.pop(0)  # Remove the word from the retake list

                # Save the updated list of missed words
                st.session_state.selected_words_for_retest = missed_words

                # Show success message
                st.success(f"✅ Correct! The word is '{current_word}'.")

            else:
                # Incorrect answer: show a reminder
                st.warning(f"❌ Incorrect! Try again with the word '{current_word}'.")

            # Check if all words are retaken
            if not missed_words:
                st.write("🎉 You have successfully retaken all missed words!")
                # Reset answers for the user or navigate to another page
                if st.button("Go Back to Test Completion"):
                    st.session_state.answers = {}
                    st.session_state.selected_letter = None
                    st.experimental_rerun()
                elif st.button("Go Back to Home"):
                    st.session_state.selected_letter = None
                    st.session_state.answers = {}
                    st.experimental_rerun()

    else:
        st.write("No missed words left to retake.")
        # Provide an option to go back to the home page
        if st.button("Go Back to Home"):
            st.session_state.selected_letter = None
            st.session_state.answers = {}
            st.experimental_rerun()

else:
    st.write("It seems like there are no missed words in your session.")
    
    # v CHANGE BELOW - delete
    # Provide an option to go back to the home page
    if st.button("Go Back to Home"):
        st.session_state.selected_letter = None
        st.session_state.answers = {}
        st.experimental_rerun()
