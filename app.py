import streamlit as st
from PIL import Image
import easyocr

st.title("Text Extraction from Images using EasyOCR")

st.write("Upload an image and extract the text from it.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    if st.button('Extract Text'):
        with st.spinner('Extracting text...'):
            # Инициализация EasyOCR
            reader = easyocr.Reader(['ru'])  # Используем язык 'en' (английский)

            # Преобразование изображения в текст
            result = reader.readtext(image)

            if result:
                # Обработка результата
                extracted_text = "\n".join([text[1] for text in result])
                st.text_area("Extracted Text", extracted_text, height=200)
            else:
                st.write("No text found on the image.")

st.write("Note: The accuracy of the text extraction may vary based on the quality of the image.")
