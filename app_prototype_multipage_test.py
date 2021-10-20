import streamlit as st
import pandas as pd
from PIL import Image
import os
# from multipage import MultiPage
from app_pages import main_app, how_it_works

header = st.container()
overview = st.container()
data = st.container()
user_input = st.container()
function = st.container()
sidebar = st.sidebar.container()

class MultiPage:
    """Framework for combining multiple streamlit applications."""

    def __init__(self) -> None:
        """Constructor class to generate a list which will store all our applications as an instance variable."""
        self.pages = []

    def add_page(self, title, func) -> None:
        """Class Method to Add pages to the project
        Args:
            title ([str]): The title of page which we are adding to the list of apps

            func: Python function to render this page in Streamlit
        """

        self.pages.append({

                "title": title,
                "function": func
            })

    def run(self):
        # Drodown to select the page to run
        page = st.sidebar.selectbox(
            'App Navigation',
            self.pages,
            format_func=lambda page: page['title']
        )

        # run the app function
        page['function']()

app = MultiPage()

st.sidebar.title("About")
st.sidebar.info("This app was created by Adam Swan - October 2021")
st.sidebar.title("Sources")
st.sidebar.info("1. https://gardening.cals.cornell.edu/ \n 2. https://www.almanac.com/")

app.add_page("App Home", main_app)
app.add_page("How it works", how_it_works)

# with sidebar:
#
#     page = st.radio("Choose your page", ["App Home", "How it works"])

app.run()

# if page == "App Home":
#
#     main_app



# elif page == 'How it works':
#
#     def how_it_works():
#         st.write('test')
#
# app.run()
