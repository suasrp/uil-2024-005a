import streamlit as st

make_sidebar()

st.title("Welcome to Diamond Corp")

st.write("Please log in to continue (username `test`, password `test`).")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Log in", type="primary"):
    if username == "test" and password == "test":
        st.session_state.logged_in = True
        st.success("Logged in successfully!")
        sleep(0.5)
        st.switch_page("pages/page1.py")
    else:
        st.error("Incorrect username or password")
