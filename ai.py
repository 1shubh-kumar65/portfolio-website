import google.generativeai as genai

def image_ai(text, img):
    genai.configure(api_key='AIzaSyBGSvpA5Ex9TOBBZSe2tiNzHYe-fAJ37O8')
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([ 'user input is:', text, img])
    return response.text

def generative_ai(text):
    genai.configure(api_key='AIzaSyBGSvpA5Ex9TOBBZSe2tiNzHYe-fAJ37O8')
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([text])
    return response.text
