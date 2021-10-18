import streamlit as st
import pandas as pd
from PIL import Image
import os.path
import pickle as pkle

header = st.container()
overview = st.container()
data = st.container()
function = st.container()
user_input = st.container()

st.spinner(text='Loading page...')

st.sidebar.title("About")
st.sidebar.info("This app was created by Adam Swan - October 2021")
st.sidebar.title("Sources")
st.sidebar.info("1. https://gardening.cals.cornell.edu/ \n 2. https://www.almanac.com/")

with header:
    st.title('Welcome to the Swan Vegetable Garden Assistant App (Alpha)')
    st.write('With this app I hope to help you discover vegetables that you will be successful\ngrowing based on your location and level of experience, but more importantly\nthat you will enjoy eating!')

with overview:
    st.header("Let's get started!")
    st.text('')

with data:
    recommender_df = pd.read_csv('./data/recommender_df.csv')
    veg_info = pd.read_csv('./data/veg_info.csv')
    ratings = pd.read_csv('./data/veggie_ratings.csv')

    ratings['user_id'] = ratings.index
    ratings.drop(columns='Timestamp', inplace=True)

    veg = ratings.columns[0:-1]
    veg_dict = {k: v for v, k in enumerate(veg)}

with user_input:
    sel_col, disp_col = st.columns(2)

    skill_level = sel_col.slider("1) What's your gardening experience level? (1 = beginner, 2 = intermediate, 3 = expert)", min_value=1, max_value=3, value=2, step=1)

    vegetable = sel_col.selectbox("2) What's your favorite vegetable?", options=['Artichokes', 'Arugula',
 'Asparagus', 'Bush beans (green beans)', 'Pole beans (green beans)', 'Beets', 'Bok Choy', 'Broccoli', 'Brussel Sprouts', 'Cabbage',
 'Carrots', 'Cauliflower', 'Celery', 'Chives', 'Collards', 'Corn', 'Cucumbers', 'Eggplant', 'Garlic', 'Kale',
 'Leeks', 'Lettuce', 'Mustard Greens', 'Onions', 'Parsnips', 'Peas', 'Peppers', 'Potatoes', 'Pumpkins', 'Radishes',
 'Rhubarb', 'Rutabagas', 'Shallots', 'Spinach', 'Summer Squash', 'Winter Squash', 'Swiss Chard', 'Tomatoes', 'Turnips'])

    image = Image.open('./data/hardiness_zones_map.jpg')
    st.image(image)


    hardiness_zone = sel_col.selectbox('3) What is your hardiness zone? (please reference the below map)', options=['2', '3', '4', '5', '6', '7', '8', '9', '10'])

with function:
    def pull_veggie_v6(vegetable, skill_level, hardiness_zone):
        veg_lst = recommender_df[['veggie_name', vegetable]].sort_values(by=vegetable)[1:11]
        veg_lst = veg_lst['veggie_name'].tolist()

        created_df = pd.DataFrame(columns=veg_info.columns)

        for num in range(0, veg_info.shape[0]):
            for veg in veg_lst:
                    if veg_info['plant'][num] == veg and veg_info['difficulty'][num] <= skill_level and (hardiness_zone in veg_info['hardiness_zones'][num]):
                        created_df = created_df.append(veg_info.loc[[num]])

        st.title("Our top picks for you are...")

        for num in range(0, created_df.shape[0]):
            st.write()
            st.header(f"#{num+1} - {veg_lst[num]}!")
            st.write()
            st.write(f"*A few important things to know before you grow {veg_lst[num]}:*")
            st.write()
            st.write(f"**Optimal sun exposure:** {created_df.iloc[num][1]}")
            st.write()
            st.write(f"**Ideal soil conditions:** {created_df.iloc[num][2]}")
            st.write()
            st.write(f"**Moisture level:** {created_df.iloc[num][3]}")
            st.write()
            st.write(f"**Expected spread:** {created_df.iloc[num][7]}")
            st.write()
            st.write(f"**Expected height:** {created_df.iloc[num][8]}")
            st.write()
            st.write(f"**Estimated time to harvest:** {created_df.iloc[num][9]}")
            st.write()
            st.write(f"**Frost tolerance:** {created_df.iloc[num][-5]}")
            st.write()
            st.write(f"**Origin:** {created_df.iloc[num][-4]}")
            st.write()
            st.write(f"**Detailed instructions:** {created_df.iloc[num][-1]}")
            st.write("*" * 45)

        st.header("Tips for getting additional results.")
        st.write("1. Hardiness zones aren't black and white, you're welcome to look outside of your local zone but those plants will likely require more attention and be more susceptible to environmental conditions.")
        st.write("2. Try searching for some of your other favorite vegetables to see what results you get.")
        st.write("3. Take a risk and increase your skill level to see what new plants show up.")

recommender = st.button('Show me the veggies!')

if recommender:
    pull_veggie_v6(vegetable, skill_level, hardiness_zone)

st.spinner(text='Retrieving plants...')
