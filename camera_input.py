import streamlit as st
from PIL import Image
import ai

def camera_input():
    st.title("enter your image either by camera or upload a file")

    st.header("Capture Image from Camera")
    camera_image = st.camera_input("Take a picture")

    if camera_image:
        st.image(camera_image, caption="Captured Image", use_column_width=True)
        # To process the image
        img = Image.open(camera_image)
        st.write("Image captured from camera")

    st.header("Upload Image from System")
    uploaded_image = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

    if uploaded_image:
        img = Image.open(uploaded_image)
        st.image(img, caption="Uploaded Image", use_column_width=True)
        st.write("Image uploaded from system")

    # Example processing with the captured or uploaded image
    if camera_image or uploaded_image:
        # Convert camera image to PIL Image
        if camera_image:
            img = Image.open(camera_image)
        else:
            img = Image.open(uploaded_image)

        text_input = st.text_input('enter your input (what to do with the image)')

        if st.button('generate'):
            a = ai.image_ai(text_input, img)
            st.write(a)

        



    

