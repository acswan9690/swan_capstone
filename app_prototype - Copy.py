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

with header:
    st.title('Welcome to the Swan Vegetable Garden Assistant App (v Alpha)')
    st.text('With this app I hope to help you discover vegetables that you will be successful\ngrowing based on your location and level of experience, but more importantly\nthat you will enjoy eating!')

with overview:
    st.header("Let's get started!")
    st.text('')

with data:
    recommender_df = pd.read_csv('./data/recommender_df.csv')
    veg_info = pd.read_csv('./data/veg_info.csv')

with user_input:
    sel_col, disp_col = st.columns(2)

    skill_level = sel_col.slider('1) What is your gardening experience level? (1 = beginner, 2 = intermediate 3 = experienced)', min_value=1, max_value=3, value=2, step=1)

    vegetable = sel_col.selectbox('2) What is your favorite vegetable?', options=['Artichokes', 'Arugula',
 'Asparagus', 'Bush beans', 'Pole beans', 'Beets', 'Bok Choy', 'Broccoli', 'Brussel Sprouts', 'Cabbage',
 'Carrots', 'Cauliflower', 'Celery', 'Chives', 'Collards', 'Corn', 'Cucumbers', 'Eggplant', 'Garlic', 'Kale',
 'Leeks', 'Lettuce', 'Mustard Greens', 'Onions', 'Parsnips', 'Peas', 'Peppers', 'Potatoes', 'Pumpkins', 'Radishes',
 'Rhubarb', 'Rutabagas', 'Shallots', 'Spinach', 'Summer Squash', 'Winter Squash', 'Swiss Chard', 'Tomatoes', 'Turnips'])

    image = Image.open('./data/hardiness_zones_map.jpg')
    st.image(image)


    hardiness_zone = sel_col.selectbox('3) What is your hardiness zone? (please reference the below map)', options=['2', '3', '4', '5', '6', '7', '8', '9', '10'])

with function:
    def pull_veggie_v6(vegetable, skill_level, hardiness_zone):
        veg_lst = recommender_df[[vegetable]].sort_values(by=vegetable)[1:11]
        veg_lst = veg_lst.index.tolist()

        created_df = pd.DataFrame(columns=veg_info.columns)

        for num in range(0, veg_info.shape[0]):
            for veg in veg_lst:
                    if veg_info['plant'][num] == veg and veg_info['difficulty'][num] <= skill_level and (hardiness_zone in veg_info['hardiness_zones'][num]):
                        created_df = created_df.append(veg_info.loc[[num]])

        print("Our top picks for you are...")
        print()
        for num in range(0, created_df.shape[0]):
            print(f"#{num+1} - {veg_lst[num]}!")
            print()
            print(f"A few important things to know before you grow {veg_lst[num]}:")
            print()
            print(f"1) Optimal sun exposure: {created_df.iloc[num][1]}")
            print()
            print(f"2) Ideal soil conditions: {created_df.iloc[num][2]}")
            print()
            print(f"3) Moisture level: {created_df.iloc[num][3]}")
            print()
            print(f"4) Expected spread: {created_df.iloc[num][7]}")
            print()
            print(f"5) Expected height: {created_df.iloc[num][8]}")
            print()
            print(f"6) Estimated time to harvest: {created_df.iloc[num][9]}")
            print()
            print("*" * 45)

result = st.button('Show me the veggies!')

if result:
    pull_veggie_v6(vegetable, skill_level, hardiness_zone)






# st.write(pull_veggie_v6)
# if my_page == 'Intro':
#     button = st.button(pull_veggie_v6(skill_level, vegetable, hardiness_zone))
#     if button:
#         st.text("Wait for it...")
# else:
#     st.header('...')
