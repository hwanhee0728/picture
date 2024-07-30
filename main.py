import streamlit as st
from PIL import Image

image_paths = [
    'IMG_01.jpg',
    'IMG_02.jpg',
    'IMG_03.jpg',
    'IMG_04.jpg',
    'IMG_05.jpg',
    'IMG_06.jpg',
    'IMG_07.jpg'
]

st.write("잠실 트리지움 314-201 마루바닥 파손 현황")

desired_height = 300

for img_path in image_paths:
    img = Image.open(img_path)
    width, height = img.size
    new_width = int((desired_height / height) * width)
    resized_img = img.resize((new_width, desired_height))
    st.image(resized_img, use_column_width=False)