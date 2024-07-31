#Basic Operations of Streamlit Framework

import streamlit as st
import pandas as pd
import numpy as np

#Title Of Application

st.title("Hello Streamlit")

#Display a simle text in streamlit

st.write("This is a simple text")

#Create basic dataframe

df = pd.DataFrame({
    'First Column': [1,2,3,4],
    'Second Column': [10,20,30,40]
})

#Display the DataFrame

st.write("Here is the DataFrame")
st.write(df)

#Create a Line Chart

chart_data = pd.DataFrame(
    np.random.randn(20,3),columns = ['a','b','c']
)
st.line_chart(chart_data)
