import streamlit as st
from navigation import make_sidebar, check_user_inactivity   # Import the sidebar function

# Check for inactivity and logout if necessary
check_user_inactivity()

# Add sidebar
make_sidebar()

# Title for the historical misspelled word list page
st.write(
    """
# 📝 Historical Misspelled Words
    """
)

# vNO CHANGE BELOW

# Check if the user has any misspelled words stored in the session
if 'incorrect_words' in st.session_state and st.session_state.incorrect_words:
    # Display the list of misspelled words
    st.write("Here are the words you have previously misspelled:")

    # Display the words in a list
    misspelled_words = st.session_state.incorrect_words
    for word in misspelled_words:
        st.write(f"- {word}")
else:
    # If there are no misspelled words, display a message
    st.write("You have no historical misspelled words.")

# Provide options to navigate or edit the misspelled word list
col1, col2 = st.columns(2)
with col1:
    # Option to edit the list of misspelled words
    if st.button("Edit Misspelled Word List"):
        st.session_state.edit_mode = True
        st.experimental_rerun()

with col2:
    # Option to go back to the home page
    if st.button("Back to Home"):
        st.session_state.selected_letter = None
        st.session_state.answers = {}
        st.experimental_rerun()
