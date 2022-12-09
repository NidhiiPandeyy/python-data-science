from PIL import Image
import streamlit as st

st.set_page_config(
    page_title='App One',
    page_icon='🙂',
    layout='wide'
)

st.title("Image Processing App")
st.sidebar.header('select image file')
image_file = st.sidebar.file_uploader('Upload Image', type=['png','jpg','jpeg'])
if image_file is not None:
    image = Image.open(image_file)
    st.image(image, caption=image_file.name)