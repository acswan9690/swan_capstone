import streamlit as st
from multiapp import MultiApp
from app_pages import main_app, how_it_works, water_app

app = MultiApp()

app.add_app("Vegetable Predictor", main_app.app)
app.add_app("Watering Estimate", water_app.app)
# app.add_app("How it Works", how_it_works.app)

app.run()

st.sidebar.title("About")
st.sidebar.info("This app was created by Adam Swan - October 2021")
st.sidebar.title("Sources")
st.sidebar.info("1. https://gardening.cals.cornell.edu/ \n 2. https://www.almanac.com/")
