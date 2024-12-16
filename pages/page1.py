import streamlit as st
import requests
from navigation import make_sidebar, check_user_inactivity  # Import necessary functions

# Check for inactivity and logout if necessary
check_user_inactivity()

# Add sidebar
make_sidebar()

# Title for the Page 1
st.write("""
# Page 1 - Word Definition, Example, and Pronunciation
""")

# Word input from the user
word = st.text_input("Enter a word:")

if word:
    st.session_state.current_word = word  # Store word for further pages

    # Fetch definition using Hugging Face API
    def get_definition(word):
        api_url = f"https://api-inference.huggingface.co/models/bert-base-uncased"
        headers = {
            'Authorization': 'Bearer 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',
        }
        payload = {
            "inputs": f"Define the word {word}",
        }

        try:
            response = requests.post(api_url, headers=headers, json=payload)
            if response.status_code == 200:
                definition = response.json()[0].get('generated_text', 'No definition found.')
                st.write(f"**Definition of {word}:** {definition}")
            else:
                st.error(f"Failed to fetch definition: {response.status_code}")
        except Exception as e:
            st.error(f"Error occurred while fetching definition: {e}")

    # Fetch example sentence using Hugging Face API
    def get_example_sentence(word):
        api_url = f"https://api-inference.huggingface.co/models/bert-base-uncased"
        headers = {
            'Authorization': 'Bearer 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',
        }
        payload = {
            "inputs": f"Use {word} in a sentence.",
        }

        try:
            response = requests.post(api_url, headers=headers, json=payload)
            if response.status_code == 200:
                example_sentence = response.json()[0].get('generated_text', 'No example sentence found.')
                st.write(f"**Example sentence for {word}:** {example_sentence}")
            else:
                st.error(f"Failed to fetch example sentence: {response.status_code}")
        except Exception as e:
            st.error(f"Error occurred while fetching example sentence: {e}")

    # Fetch pronunciation using LlamaCloud API
    def play_pronunciation(word):
        api_url = f"https://api.llamacloud.com/v1/speech/pronounce?word={word}"
        headers = {
            'Authorization': 'Bearer llx-qzM2fHBXD6hl2xyeRS6JzJafF2mKviaxtTJxWdY6nIAouF7a',
        }

        try:
            response = requests.get(api_url, headers=headers)
            if response.status_code == 200:
                audio_url = response.json().get('audio_url', None)
                if audio_url:
                    st.audio(audio_url, format='audio/mp3')
                else:
                    st.error("Pronunciation audio not available.")
            else:
                st.error("Failed to fetch pronunciation.")
        except Exception as e:
            st.error(f"Error occurred while fetching pronunciation: {e}")

    # Display Definition and Example Sentence
    get_definition(word)
    get_example_sentence(word)

    # Button to trigger pronunciation
    if st.button("Pronounce Word"):
        play_pronunciation(word)
else:
    st.write("Please enter a word to get the definition, example sentence, and pronunciation.")
