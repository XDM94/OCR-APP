import streamlit as st
from PIL import Image
import easyocr
import requests
from io import BytesIO

st.title("Text Extraction from Images using EasyOCR")

st.write("Upload an image or provide a URL to extract text from it.")

# Выбор метода загрузки изображения
option = st.radio("Choose image source:", ("Upload Image", "Provide Image URL"))

if option == "Upload Image":
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        if st.button('Extract Text'):
            with st.spinner('Extracting text...'):
                reader = easyocr.Reader(['ru'])
                result = reader.readtext(image)

                if result:
                    extracted_text = "\n".join([text[1] for text in result])
                    st.text_area("Extracted Text", extracted_text, height=200)
                else:
                    st.write("No text found on the image.")

elif option == "Provide Image URL":
    image_url = st.text_input("Enter image URL:")

    if st.button('Load Image'):
        if image_url:
            try:
                response = requests.get(image_url)
                image = Image.open(BytesIO(response.content))
                st.image(image, caption='Image from URL', use_column_width=True)

                with st.spinner('Extracting text...'):
                    reader = easyocr.Reader(['ru'])
                    result = reader.readtext(image)

                    if result:
                        extracted_text = "\n".join([text[1] for text in result])
                        st.text_area("Extracted Text", extracted_text, height=200)
                    else:
                        st.write("No text found on the image.")

            except Exception as e:
                st.error(f"Error loading image from URL: {e}")
        else:
            st.warning("Please provide a valid image URL.")
