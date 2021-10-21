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
        st.title("How it Works")

        st.header('1. Compile Vegetable Ratings and Data')

        st.write("I reached out to friends, family, and my data science cohort to participate in a 37 question survey to get their feedback on how they rated 37 vegetables on a scale of 1 - 5, with 1 being disgusting and 5 being delicious - all subjective. I received a total of 134 responses.")
        st.write('')
