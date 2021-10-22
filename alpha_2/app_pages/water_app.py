import streamlit as st
import pandas as pd
import time
import requests

def app():

    header = st.container()
    data = st.container()
    user_input = st.container()
    function = st.container()

    with header:
        st.title('Welcome to the Water Use Estimator App (Alpha)')
        st.write('')
        st.write('This app aims to give you an estimate of how much water you need to use in your vegetable garden in 7-day period after the desired date using historical temperature and rainfall data as well as the size of your garden.')
        st.write('')
        st.write("**NOTE**: This estimator app currently only works for the 88 counties in the state of Ohio.")
        st.write('')

    with data:
        counties = pd.read_csv('./data/counties.csv')

    with user_input:
        county_lst = sorted(['Allen', 'Lake', 'Columbiana', 'Cuyahoga', 'Morgan', 'Harrison', 'Putnam', 'Muskingum', 'Tuscarawas', 'Wyandot', 'Clark', 'Butler', 'Pike', 'Ottawa', 'Hamilton', 'Coshocton',
        'Fulton', 'Van Wert', 'Washington', 'Wood', 'Fairfield', 'Preble', 'Logan', 'Lawrence', 'Pickaway', 'Jackson', 'Athens', 'Stark', 'Auglaize', 'Brown', 'Belmont', 'Medina', 'Paulding', 'Darke', 'Noble',
        'Union', 'Delaware', 'Mahoning', 'Carroll', 'Meigs', 'Henry', 'Champaign', 'Vinton', 'Lorain', 'Franklin', 'Hancock', 'Crawford', 'Highland', 'Huron', 'Adams', 'Guernsey', 'Morrow', 'Erie', 'Clermont',
        'Licking', 'Hardin', 'Williams', 'Summit', 'Geauga', 'Scioto', 'Defiance', 'Seneca', 'Mercer', 'Richland', 'Perry', 'Gallia', 'Madison', 'Trumbull', 'Hocking', 'Miami', 'Ashland', 'Shelby', 'Portage', 'Lucas',
        'Sandusky', 'Montgomery', 'Ross', 'Jefferson', 'Fayette', 'Wayne', 'Clinton', 'Greene', 'Marion', 'Monroe', 'Ashtabula', 'Holmes', 'Warren', 'Knox'])
        days_lst = list(range(1, 32))
        years_lst = list(range(2009, 2022))

        month_str = st.selectbox("1) Please choose a month", options=['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'])

        day_int = st.selectbox("2) Please choose a day", options=days_lst)

        county = st.selectbox("3) Please choose a county", options=county_lst)

        size_of_garden = st.text_input("4) Please enter the square footage of your garden", '')

        estimate = st.button('Estimate')

    with function:
        months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        month_day_dict = {months[i]: days[i] for i in range(len(months))}
        years = list(range(2009, 2022))

        def water_estimate(month_str, day_int, county, size_of_garden):

            if day_int > month_day_dict[month_str]:
                return st.error('Please enter a day that exists in the specified month')

            else:
                pass

            county_coords = counties.loc[counties['NAME'] == county, ['INTPTLAT', 'INTPTLON']]
            lat = round(float(county_coords['INTPTLAT']), 2)
            long = round(float(county_coords['INTPTLON']), 2)

            if day_int+7 > month_day_dict[month_str]:

                next_month = '0' + str(list(month_day_dict.keys()).index(month_str)+2)
                next_month_day = month_day_dict[month_str] - day_int
                next_month_day = 7 - next_month_day
                start_date = month_str + '-' + str(day_int)
                end_date = next_month + '-' +str(next_month_day)

            else:
                start_date = month_str + '-' + str(day_int)
                end_date = month_str + '-' + str(day_int+7)

            urls = []

            for year in years:

                url = 'http://api.worldweatheronline.com/premium/v1/past-weather.ashx?key=ee035e8c8a26404e99b183309212110'
                url = url + '&format=json'
                url = url + '&q=' + str(lat) + ',' + str(long)
                url = url + '&tp=24'
                url = url + '&date=' + str(year) + '-' + start_date
                url = url + '&enddate=' + str(year) + '-' + end_date

                urls.append(url)

            data = []

            for i, url in enumerate(urls):
                time.sleep(1)
                res = requests.get(url)
                data.append(res.json())

            list_of_cols = ['date', 'maxtempF', 'mintempF', 'precipInches']

            list_of_records = []

            for i in range(len(data)):
                for num in range(0, 7):
                    list_of_records.append([data[i]['data']['weather'][num]['date'],
                        int(data[i]['data']['weather'][num]['maxtempF']),
                        int(data[i]['data']['weather'][num]['mintempF']),
                        float(data[i]['data']['weather'][num]['hourly'][0]['precipInches'])])

            df = pd.DataFrame(list_of_records, columns=list_of_cols)

            average_temp = round((df['maxtempF'].mean() + df['mintempF'].mean()) / 2, 2)
            average_precip = round(df['precipInches'].mean(), 2)
            size_of_garden = int(size_of_garden)

            if average_temp > 60:
                diff = 80 - average_temp
                water_amt = round(((diff / 10) * .5) + (1 - average_precip), 2)
                gallons = round((water_amt * 1.56) * size_of_garden, 2)
                st.write(f"**The average temperature for the specified time period is**: {average_temp} F")
                st.write('')
                st.write(f"**The average rainfall for the specified time period is**: {average_precip} inches")
                st.write('')
                st.write(f"**Estimated inches of water:** {water_amt} inches per sq/ft")
                st.write('')
                st.write(f"**Estimated gallons of water:** {gallons} gallons of water for you entire garden")

            else:
                water_amt = 1 - average_precip
                gallons = round((water_amt * 1.56) * size_of_garden, 2)
                st.write(f"**The average temperature for the specified time period is:** {average_temp} F")
                st.write('')
                st.write(f"**The average rainfall for the specified time period is:** {average_precip} inches")
                st.write('')
                st.write(f"**Estimated inches of water:** {water_amt} inches per sq/ft")
                st.write('')
                st.write(f"**Estimated gallons of water:** {gallons} gallons of water for your entire garden")

    if estimate:
        st.spinner('Calculating...')

        water_estimate(month_str, day_int, county, size_of_garden)

        st.success('Done')
