import streamlit as st
from navigation import make_sidebar, check_user_inactivity  # Import the sidebar function

# Check for inactivity and logout if necessary
check_user_inactivity()

# Add sidebar
make_sidebar()

# Title for the edit misspelled word list page
st.write(
    """
# ✏️ Edit Misspelled Words List
    """
)

# v NO CHANGE

# Display instructions
st.write("You can add or remove words from your misspelled word list below:")

# Initialize session state for misspelled words if not present
if 'incorrect_words' not in st.session_state:
    st.session_state.incorrect_words = []

# Display the current list of misspelled words
if st.session_state.incorrect_words:
    st.write("Current misspelled words:")
    for word in st.session_state.incorrect_words:
        st.write(f"- {word}")
else:
    st.write("No misspelled words yet.")

# Form for adding/removing words
with st.form(key='edit_form'):
    # Text input to add a word
    word_to_add = st.text_input("Add a Word to the List", "")

    # Dropdown to choose an action (Add or Remove)
    action = st.selectbox("Choose Action", ["Add", "Remove"])

    # Display submit button
    submit_button = st.form_submit_button(label="Submit")

    if submit_button:
        # Handle adding a word
        if action == "Add" and word_to_add:
            if word_to_add not in st.session_state.incorrect_words:
                st.session_state.incorrect_words.append(word_to_add)
                st.success(f"Added '{word_to_add}' to your misspelled word list.")
            else:
                st.warning(f"'{word_to_add}' is already in the list.")

        # Handle removing a word
        elif action == "Remove" and word_to_add:
            if word_to_add in st.session_state.incorrect_words:
                st.session_state.incorrect_words.remove(word_to_add)
                st.success(f"Removed '{word_to_add}' from your misspelled word list.")
            else:
                st.warning(f"'{word_to_add}' is not in the list.")

        # Reset form fields after submission
        st.experimental_rerun()

# Provide a button to navigate back to the historical misspelled word list page
if st.button("Back to Historical Misspelled Words"):
    st.session_state.edit_mode = False  # Disable edit mode
    st.experimental_rerun()
