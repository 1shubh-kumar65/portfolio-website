import streamlit as st
import os
import google.generativeai as genai

# Initialize and configure the generative AI model
try:
    api_key = st.secrets['GOOGLE_API_KEY']
    genai.configure(api_key)
except KeyError:
    st.error("Google API key not found. Please configure the API key in Streamlit secrets.")
    st.stop()

# Initialize generative model
try:
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Error initializing generative model: {e}")
    st.stop()

# Streamlit UI setup
col1, col2 = st.columns(2)

with col1:
    st.subheader("HI :wave:")
    st.title('I am Shubh Kumar')

with col2:
    st.title('Place an image here')

# Persona description
persauna_about_me = '''
you are shubhs ai bot and will answer any questions related to shubh based on below data.
you will answer only in first person and not in second and third person.
the data is:
my name is shubh kumar, I am from Delhi, India currently studying in grade 8th.
my hobbies:
programming - I am learning python for 2 years through YouTube and purchased a Udemy course. This would be my first python contest.
cooking - I am pretty good at cooking and can make any dish if I know the recipe.
skating - I am learning to skate since grade 1 and have also participated in some competitions.
football, volleyball - I am learning football and volleyball since the lockdown in India.
'''

st.title(' ')
st.title('MY AI BOT')
user_question = st.text_input('Ask anything about me')
if user_question:
    try:
        response = model.generate_content(persauna_about_me + ' user input is: ' + user_question)
        st.write(response.text)
    except Exception as e:
        st.error(f"Error generating response: {e}")

# AI code writer section
try:
    persauna = '''
    you are a personal AI bot. You only have to generate python code to execute
    the task given by the user (generate only code and nothing else, not even the explanation
    because the code will be copied to another file to be executed). Ensure there is always a way to stop the code,
    and make sure there is always a GUI in it if it is a game. Ensure it is playable and interesting.
    '''

    user_input = st.text_input('Enter a prompt for generating Python code')

    if user_input:
        try:
            response = model.generate_content(persauna + ' user input is: ' + user_input)
            code = response.text.replace("```python", '').replace("```", '')
            st.code(code, language='python')

            if st.button('Generate and Execute'):
                with open('test.py', 'w') as script_file:
                    script_file.write(code)

                script_path = 'test.py'
                if os.path.isfile(script_path):
                    os.system(f'python {script_path}')
                else:
                    st.error(f"Error: The file '{script_path}' does not exist.")
        except Exception as e:
            st.error(f"Error generating code: {e}")
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")
