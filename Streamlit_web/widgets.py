import streamlit as st 
import pandas as pd

st.title("Streamlit Text Input")

name = st.text_input("Enter Your Name: ")
age = st.slider("Enter Your age: ",0,100,18)

options = ["Python", "JavaScript", "Golang", "Rust"]
choice = st.selectbox("Choose your favourite language: ", options)
st.write(f"You have selected {choice}.")

st.write(f"Your age is {age}.")
if name:
    st.write(f"Hello, {name}")
    
# TO Upload File

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

