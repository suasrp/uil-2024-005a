import streamlit as st
import requests
from navigation import make_sidebar, check_user_inactivity  # Import necessary functions

# Check for inactivity and logout if necessary
check_user_inactivity()

# Add sidebar
make_sidebar()

## Example alphabet test data
#ALPHABET_TESTS = {
    #'a': ["abbreviate", "abnormality"],
    #'b': ["badminton", "balky"],
    #'c': ["calculate", "calendar"],
    #'d': ["damask", "dauntless"],
    ## Add more letters and words...
#}

#st.write(
#    """
## 📝 5th-6th Grade - List of Words
    """
#)

#st.title("Select Your Test")
#letter = st.selectbox("Select a letter", list(ALPHABET_TESTS.keys()))
#st.write(f"Selected Test: {letter.upper()}")
#st.write("Words in this test:")
#st.write(ALPHABET_TESTS[letter])

## You could add a function to track progress here
