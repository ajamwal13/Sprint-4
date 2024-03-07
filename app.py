import streamlit as st
import pandas as pd
import plotly.express as px

st.header('This is the data on vehicles in the U.S.')

data = pd.read_csv('vehicles_us.csv')

agree = st.checkbox('Display histogram on odometer readings')

if agree:
    fig3 = px.histogram(data, x='odometer', title='Vehicle Odometer Distribution')
    st.write(fig3)

fig = px.histogram(data, x='price', title='Vehicle Price Distribution')
st.write(fig)

fig2 = px.scatter(data, x='price', y='days_listed', title='Vehicle Odometer Distribution')
st.write(fig2)

