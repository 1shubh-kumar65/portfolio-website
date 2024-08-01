import streamlit as st
import speech_recognition as sr
from googletrans import Translator
from pydub import AudioSegment
import tempfile
import os
import ai.ai as ai  # Assuming ai is a custom module with a generative_ai function

# Function to handle voice input and translation
def start():
    def translate_voice_to_english(source='mic', file=None, language='en-US'):
        recognizer = sr.Recognizer()
        if source == 'mic':
            with sr.Microphone() as mic:
                st.info("Listening...")
                audio = recognizer.listen(mic)
        elif source == 'file' and file is not None:
            with sr.AudioFile(file) as audio_file:
                audio = recognizer.record(audio_file)
        else:
            return "Invalid source or file."

        try:
            recognized_text = recognizer.recognize_google(audio, language=language)
        except sr.UnknownValueError:
            return "Sorry, I could not understand the audio."
        except sr.RequestError as e:
            return f"Could not request results; {e}"

        translator = Translator()
        translated_text = translator.translate(recognized_text, dest='en').text
        return translated_text

    # Function to translate text to a selected language
    def translate_to_selected_language(text, dest_language):
        translator = Translator()
        translated_text = translator.translate(text, dest=dest_language).text
        return translated_text

    st.title('Voice Input Translator')

    # Dropdown menu for language selection
    language_options = {
        'English': 'en',
        'Spanish': 'es',
        'French': 'fr',
        'German': 'de',
        'Chinese': 'zh-CN',
        'Japanese': 'ja',
        'Korean': 'ko',
        'Hindi': 'hi',
        'Arabic': 'ar',
        'Russian': 'ru'
    }

    selected_language = st.selectbox('Select the language of the voice input', list(language_options.keys()))
    language_code = language_options[selected_language]

    # File uploader for audio file
    uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])

    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(uploaded_file.read())
            temp_filename = temp_file.name

        if uploaded_file.type == 'audio/mp3':
            sound = AudioSegment.from_mp3(temp_filename)
            temp_filename_wav = temp_filename.replace('.mp3', '.wav')
            sound.export(temp_filename_wav, format="wav")
            temp_filename = temp_filename_wav

        translated_text = translate_voice_to_english(source='file', file=temp_filename, language=language_code)
        st.write(f"Translated text: {translated_text}")

        os.remove(temp_filename)
        if uploaded_file.type == 'audio/mp3':
            os.remove(temp_filename_wav)

    if st.button('Listen'):
        translated_text = translate_voice_to_english(source='mic', language=language_code)
        st.write(f"Recognized text: {translated_text}")
        
        # Generate AI response
        answer = ai.generative_ai(translated_text)
        st.write(f"AI Response: {answer}")
        
        # Translate AI response to selected language
        translated_answer = translate_to_selected_language(answer, language_code)
        st.write(f"Translated AI Response: {translated_answer}")
