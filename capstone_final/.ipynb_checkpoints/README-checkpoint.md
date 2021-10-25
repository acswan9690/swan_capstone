# Vegetable Recommender & Water Usage Planner
---

### Problem Statement:
---
Can I build an app that will make accurate recommendations based on users' ratings as well as give users a rough estimate on their water usage using historical weather data and garden size as parameters?

### Executive Summary:
---
I remember when I was younger living in Ohio and my parents started their small salsa garden.  They loved planting their tomatoes and peppers and enjoyed taking care of them.  I didn't like salsa back then, a truly heinous offense, but now that I'm older I can appreciate the joy it brough them through the experience of growing their own vegetables and the satisfaction of enjoying the delicious food that came from them.  I don't yet own a plot of land big enough to have my own vegetable garden but I hope that someday I can.  Those thoughts are how the app was conceived.

I had no clue where to start and I'm sure many amateur gardeners feel the same way.  Just like anything in life there are difficulty levels to consider and one of the biggest discouraging factors to novices in any activity is starting with something that's too difficult.  I used Cornell University's gardening database to determine difficulty levels and provided parameters in the app to help people select vegetables that will be achievable to their skill level.  Additionally, it's important to consider location.  Hardiness zones are the USDA's way of identifying temperature conditions where certain plants can be grown most successfully.  It's possible to grow plants that aren't ideal for your hardiness zone but they will require more care and resources.  

Finally the data sciencey part.  The recommender app.  I received 134 survey responses rating the most commonly grown vegetables and input them into a dataframe and measured the cosine distances between them all to generate a recommender dataframe that can be used to pull the best recommendations using user input.

Another important resource to consider when gardening, especially for vegetables, is water.  One of the most time consuming processes of garden care is watering.  If you have a rain water reserve or water is in short supply it's helpful to have an idea of how much water will be used.  The rule of thumb is an inch of water for your vegetable garden every week, however, they also recommend an extra 0.5 inch of water for every 10 degrees over 60&deg;F.  The conversion rate is about 1.56 gallons per 1 inch of water in a square foot.  There are quite a few steps to calculating the ideal water amount so I took all steps out.  All a user has to do is input a date, their county, and the size of their garden and the app calculates an estimated amount of water to be used for the next 7-day period.

---

### 1. Sample Details:

- 39 vegetables
- 134 anonymous ratings on a scale of 1 - 5

### 2. Sources:

- https://gardening.cals.cornell.edu/
    - Vegetables details
- https://www.almanac.com/
    - Detailed growing instructions
- https://public.opendatasoft.com/
    - Ohio county information
- Jeff Warchall
    - Adapted his webscraping code from a previous project we collaborated on
    
### 3. Conclusion:

The app really helped me develop my coding skills.  It wasn't a formal modeling problem like we really dug into with previous projects but the recommender app was fun to create and the challenges I faced trying to write functions that did everything I wanted for the recommender and the water estimator definitely pushed my abilities.

The recommender does a good job choosing vegetables that fit someone's taste as well as pick choices appropriate to their location and skill level.  The watering app is also fantastic for planning and creates recommendations based on the last 12 years of weather in the user specified 7-day period.

### 4. Next-step:

The best part about the app is that I can continue to refine and add features.  I can add new states to the water estimator as well as get new ratings to flesh out the recommender.  Overall I think it's in a great place for alpha level deployment and further refinement. 
