import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

def app():

    header = st.container()
    overview = st.container()
    data = st.container()
    user_input = st.container()
    function = st.container()
    sidebar = st.sidebar.container()

    with header:
        st.title("How I Made the App")

        st.header('1. Compile Vegetable Ratings')

        st.write("I reached out to friends, family, and my data science cohort to participate in a 37 \n question survey to get their feedback on how to rated vegetables.")

        st.header("")
        image1 = Image.open('./data/how1')
        st.image(image1)
