import gtts
import streamlit as st

# Set page title and header
st.title("Text to Speech Converter")

# Text input field
text = st.text_input('Enter your text here', '')

# Button to trigger audio playback
if st.button("Convert Text to Audio"):
    sound = gtts.gTTS(text, lang="en")
    sound.save("Welcome1.mp3")
    st.audio("Welcome1.mp3", format="audio/mp3")
