import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

def app():

    header = st.container()
    data = st.container()
    user_input = st.container()
    function = st.container()


    with header:
        st.title('Welcome to the Swan Vegetable Garden Assistant App (Alpha)')
        st.write('With this app I hope to help you discover vegetables that you will be successful\ngrowing based on your location and level of experience, but more importantly\nthat you will enjoy eating!')

        st.header("**Let's get started!**")
        st.write('')

    with data:
        recommender_df = pd.read_csv('./data/recommender_df.csv')
        veg_info = pd.read_csv('./data/veg_info.csv')
        ratings = pd.read_csv('./data/veggie_ratings.csv')

        ratings['user_id'] = ratings.index
        ratings.drop(columns='Timestamp', inplace=True)

        veg = ratings.columns[0:-1]
        veg_dict = {k: v for v, k in enumerate(veg)}

    with user_input:
        options_lst = ['Artichokes', 'Arugula', 'Asparagus', 'Bush beans (green beans)', 'Beets',
        'Bok Choy', 'Broccoli', 'Brussel Sprouts', 'Cabbage', 'Carrots', 'Cauliflower', 'Celery', 'Chives', 'Collards', 'Corn',
         'Cucumbers', 'Eggplant', 'Garlic', 'Kale', 'Leeks', 'Lettuce', 'Mustard Greens', 'Onions', 'Parsnips', 'Peas', 'Peppers',
          'Potatoes', 'Pumpkins', 'Radishes', 'Rhubarb', 'Rutabagas', 'Shallots', 'Spinach', 'Squash', 'Swiss Chard', 'Tomatoes', 'Turnips']

        skill_level = st.slider("1) How much experience do you have gardening? (1 = none, 2 = a little bit, 3 = you've successfully grown a few things)", min_value=1, max_value=3, value=2, step=1)

        vegetable_1 = st.selectbox("2) What's your favorite vegetable?", options=options_lst)

        vegetable_2 = st.selectbox("3) What's your second favorite vegetable?", options=options_lst)

        vegetable_3 = st.selectbox("4) What's your third favorite vegetable?", options=options_lst)

        hardiness_zone = st.selectbox("5) What's your hardiness zone? (please reference the map below)", options=['2', '3', '4', '5', '6', '7', '8', '9', '10'])

        image = Image.open('./data/hardiness_zones_map.jpg')
        st.image(image)

    with function:
        def pull_veggie_v6(vegetable_1, vegetable_2, vegetable_3, skill_level, hardiness_zone):
            veg_lst_1 = recommender_df[['veggie_name', vegetable_1]].sort_values(by=vegetable_1)[1:11]
            veg_lst_1 = veg_lst_1['veggie_name'].tolist()

            veg_lst_2 = recommender_df[['veggie_name', vegetable_2]].sort_values(by=vegetable_2)[1:11]
            veg_lst_2 = veg_lst_2['veggie_name'].tolist()

            veg_lst_3 = recommender_df[['veggie_name', vegetable_3]].sort_values(by=vegetable_3)[1:11]
            veg_lst_3 = veg_lst_3['veggie_name'].tolist()

            created_df = pd.DataFrame(columns=veg_info.columns)

            for val in veg_lst_2:
                if val not in veg_lst_1:
                    veg_lst_1.append(val)

            for val in veg_lst_3:
                if val not in veg_lst_2:
                    veg_lst_2.append(val)

            veg_lst = veg_lst_2

            for num in range(0, veg_info.shape[0]):
                for veg in veg_lst:
                        if veg_info['plant'][num] == veg and veg_info['difficulty'][num] <= skill_level and (hardiness_zone in veg_info['hardiness_zones'][num]):
                            created_df = created_df.append(veg_info.loc[[num]])

            new_veg_lst = created_df['plant'].tolist()
            final_lst = []

            for val in veg_lst:
                if val in new_veg_lst:
                    final_lst.append(val)

            final_lst = sorted(final_lst)

            st.header(f"**We found {len(final_lst)} vegetables we think are a good fit for you!**")

            for num in range(0, created_df.shape[0]):
                st.header(f"#{num+1} - {final_lst[num]}")
                st.write()
                st.write(f"*A few important things to know before you grow **{final_lst[num].lower()}**:*")
                st.write()
                st.write(f"**Difficulty level:** {int(created_df.iloc[num][6])}")
                st.write()
                st.write(f"**Optimal sun exposure:** {created_df.iloc[num][1]}")
                st.write()
                st.write(f"**Ideal soil conditions:** {created_df.iloc[num][2]}")
                st.write()
                st.write(f"**Moisture level:** {created_df.iloc[num][3]}")
                st.write()
                st.write(f"**Expected spread:** {created_df.iloc[num][8]}")
                st.write()
                st.write(f"**Expected height:** {created_df.iloc[num][7]}")
                st.write()
                st.write(f"**Estimated time to harvest:** {created_df.iloc[num][9]}")
                st.write()
                st.write(f"**Frost tolerance:** {created_df.iloc[num][-5]}")
                st.write()
                st.write(f"**Detailed growing information:** {created_df.iloc[num][-1]}")
                st.write("*" * 45)

            st.header("Tips for getting additional results.")
            st.write("1. Hardiness zones aren't black and white, you're welcome to look outside of your local zone but those plants will likely require more attention and be more susceptible to environmental conditions.")
            st.write("2. Try searching for some of your other favorite vegetables to see what results you get.")
            st.write("3. Take a risk and increase your skill level to see what new plants show up.")
            st.write("4. If you're picky just choose the same vegetable for your all three choices to ensure you only get vegetables similar to your favorite.")

        recommender = st.button('Show me the veggies')

        if recommender:
            pull_veggie_v6(vegetable_1, vegetable_2, vegetable_3, skill_level, hardiness_zone)
            st.success('Done')
