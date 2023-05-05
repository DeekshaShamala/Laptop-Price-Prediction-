import streamlit as st
import os
import pandas as pd



# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))


# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)



# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

Data_Path = os.path.join(dir_of_interest,"laptop_details.csv")

df = pd.read_csv(Data_Path)

st.subheader("Laptop Data")

st.markdown("The below data has been extracted from flipkart.")

st.dataframe(df)

Data_Path = os.path.join(dir_of_interest,"laptop_dataframe.csv")

df = pd.read_csv(Data_Path)

st.markdown("After performing feature extraction, this is the final dataframe that has been used for training and testing the model.")

st.dataframe(df)







