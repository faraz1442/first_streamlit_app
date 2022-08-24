import streamlit
import pandas as pd

streamlit.title("My parents New Healthy Diner")

streamlit.header("Breakfast Menu")
streamlit.title("🥣Omega 3 & Blueberry Oatmeal")
streamlit.title("🥗Kale, Spinach & Rocket Smootie")
streamlit.title("🐔Hard boiled free ranged egg")
streamlit.title("🥑🍞Avocado Toast")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list=pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
