import streamlit as st
import pandas as pd
import plotly.express as px

st.header('This is the data on vehicles in the U.S.')

data = pd.read_csv('vehicles_us.csv')

fig1_check = st.checkbox('Display histogram on vehicle prices')
fig2_check = st.checkbox('Display scatter plot of days listed versus vehicle price')
fig3_check = st.checkbox('Display histogram on odometer readings')

if fig1_check:
    fig = px.histogram(data, x='price', title='Vehicle Price Distribution')
    st.plotly_chart(fig)

if fig2_check:
    fig2 = px.scatter(data, x='price', y='days_listed', title='Vehicle Odometer Distribution')
    st.plotly_chart(fig2)

if fig3_check:
    fig3 = px.histogram(data, x='odometer', title='Vehicle Odometer Distribution')
    st.plotly_chart(fig3)