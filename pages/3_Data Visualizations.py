import streamlit as st
import pandas as pd
import os
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))


# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)



# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

Data_Path = os.path.join(dir_of_interest,"laptop_dataframe.csv")

df = pd.read_csv(Data_Path)

st.write("Countplot of RAM-size and OS:")

st.bar_chart(df["RAM_size"].value_counts())

st.bar_chart(df["OS"].value_counts())

st.write("Let's see how the MRP is varying with respect to features:")

fig = px.bar(df, x='OS', y='MRP')

st.plotly_chart(fig, use_container_width=True)


fig = px.bar(df, x='RAM_size', y='MRP')

st.plotly_chart(fig, use_container_width=True)


fig = px.bar(df, x='bit', y='MRP')

st.plotly_chart(fig, use_container_width=True)


fig = px.bar(df, x='SSD_Storage', y='MRP')

st.plotly_chart(fig, use_container_width=True)




