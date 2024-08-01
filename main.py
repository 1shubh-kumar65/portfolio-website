import streamlit as st
import webbrowser

import inputs.voice_input as voice_input
import inputs.camera_input as camera_input
import inputs.text_input as text_input 
from main_data import popular_websites

# Create a simple navigation bar
st.sidebar.title("Navigation")
option = st.sidebar.radio("Go to", ["voice input", "camera input", "text input"])

# voice input
if option == "voice input":
    voice_input.start()

# camera input
elif option == "camera input":
    camera_input.camera_input()

# text input
elif option == "text input":
    command = text_input.text_input()
    if st.button('generate'):
        
        
