import os
#import google.generativeai as genai
import streamlit as st

api_key=st.secrets['GOGGLE_API_KEY']

genai.configure(api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

col1, col2 = st.columns(2)

with col1:
    st.subheader("HI :wave:")
    st.title('I am Shubh Kumar')

with col2:
    st.title('place an image here')

persauna_about_me = '''
you are shubhs ai bot and will answer any questions related to shubh based on below data.
you will answer only in first person and not in second and third person.
the data is :
my name is subh kumar i am from delhi india currently studying in grade 8th .
my hobbies:
programing - i am learning python for 2 yrs through youtube an purchased a udamy cource this would my first python contest
cooking - i am pretty good at cooking can can make any dish if i know the recipy of it
skating - i am learning to skate since grade 1 and have also participated in some competions
fool ball, volly ball - i am learning foot ball and volly ball since lockdown in india 
'''

st.title(' ')
st.title('MY AI BOT')
user_question = st.text_input('Ask anything about me')
response = model.generate_content(persauna_about_me + 'user input is:' + user_question)

try:
    # my ai code writer

    persauna = '''
    you are an personal ai bot you only have to generate python code to execute
    the task given by the user(generate only code and nonething 
    else not even the explanation because the code will be copied
    to another file to be excuted be exucted) and also make sure there is alweys a way to stop the code
    and make sure there is always gui in it if it is a game make sure it is playable and intresting
    '''

    user_input = st.text_input('enter a prompt')


    response = model.generate_content(persauna + 'user input is:' + user_input)

    code = response.text.replace("```python", '')
    code = code.replace("```", '')


    if st.button('generate'):  
        with open('test.py', 'w') as a:
            a.write(code)

        # Specify the path to your Python file (replace 'path/to/your/script.py' with the actual path)
        script_path = 'test.py'

        # Check if the file exists
        if os.path.isfile(script_path):
            # Execute the Python script using os.system()
            os.system(f'python {script_path}')
        else:
            print(f"Error: The file '{script_path}' does not exist.")
except:
    pass
