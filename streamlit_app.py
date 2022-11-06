import streamlit
streamlit.title('My Parents Healthy Diner.')

streamlit.header('Breakfast Menu')

streamlit.text('🥣 Omega 3 and Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach and Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list.set_index('Fruit',inplace=True)

# Let's put a pick list here so they can pick the fruit they want to include 
selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_to_show=my_fruit_list.loc[selected]
# Display the table on the page.



streamlit.dataframe(fruit_to_show)

import requests
fruityvice_response=requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response.json())
streamlit.header('FruityVice Fruit Advice!!!')

fruit_choice = streamlit.text_input('What fruit would you like information about?'
streamlit.write('The user entered', fruit_choice)
                                     
# take the json version of the response and normalize it
fruityvice_normalized=pd.json_normalize(fruityvice_response.json())
#output it the screen as a table
streamlit.dataframe(fruityvice_normalized)
