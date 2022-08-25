import streamlit
import pandas as pd
import requests


streamlit.title("My parents New Healthy Diner")

streamlit.header("Breakfast Menu")
streamlit.title("🥣Omega 3 & Blueberry Oatmeal")
streamlit.title("🥗Kale, Spinach & Rocket Smootie")
streamlit.title("🐔Hard boiled free ranged egg")
streamlit.title("🥑🍞Avocado Toast")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list=pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# Display the table on the page.
streamlit.dataframe(my_fruit_list)

streamlit.header("Fruityvice Fruit Advice!")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
