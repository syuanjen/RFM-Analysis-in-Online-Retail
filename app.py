import streamlit as st
import pandas as pd

st.title("Air Quality Dashboard")
st.header("This is header")
st.subheader("This is sub-header")
st.text("the air data is monitored daily")
st.markdown("**Pleas be noted that the data displayed is subject to change.**")
st.markdown("_italic text_")
st.code("for i in range(5): print(i)", language="python")
st.write("Welcome to your first Streamlit App 😎")

q = st.number_input("Enter the minimum product sold quantity you would like to see in the dataset",min_value=1, max_value=100)
df = pd.read_excel("Online Retail.xlsx")
st.write(df[df.Quantity >= q].head())

name = st.text_input("Enter your name")
rating = st.slider("Rate the App!",1,5)
city = st.selectbox("Choose a country",df.columns.tolist())

if st.button("Click me!"):
    st.success(f"{name}! You clicked the button successfully!")