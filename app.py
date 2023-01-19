import streamlit as st
from PIL import Image, ImageFilter

st.set_page_config(page_title="Oil Painting App", page_icon=":paintbrush:", layout="wide")

file_types = ["jpg", "jpeg", "png"]
uploaded_file = st.file_uploader("Upload an image file (jpg, jpeg, png)", type=file_types)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, use_column_width=True)
    image = image.filter(ImageFilter.CONTOUR)
    st.image(image, use_column_width=True)
    st.success("The image has been converted to an oil painting!")