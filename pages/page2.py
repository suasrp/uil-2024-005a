import streamlit as st
import requests
from navigation import make_sidebar, check_user_inactivity  # Import necessary functions

# Check for inactivity and logout if necessary
check_user_inactivity()

# Add sidebar
make_sidebar()

# Title for Page 2
st.write("""
# Page 2 - Continue with the Test or Select Other Words
""")

# Display a message for the user
st.write("This is Page 2. You can continue your test or explore other words.")

# Navigation buttons for user
if st.button("Go to Word Definition Page"):
    st.session_state.current_word = ''  # Clear current word for a new selection
    st.write("Navigating to the Word Definition Page...")
    st.experimental_rerun()  # Rerun the app to go back to the previous page

if st.button("Go to the Test Complete Page"):
    st.write("Navigating to the Test Completion Page...")
    # Code for navigating to Test Complete page, for example:
    st.experimental_rerun()  # Adjust to go to your desired page
