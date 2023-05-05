import streamlit as st
import joblib
import os 
import pandas as pd

st.title("Laptop Price Prediction")


#model = joblib.load(r"C:\Users\deeksha\laptop price analysis\laptop_price_prediction.pkl")

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))


# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)



# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")



MODEL_PATH = os.path.join(dir_of_interest,"laptop_price_prediction.pkl")

model = joblib.load(MODEL_PATH)

Processor = st.selectbox("Select the type of Processor:", ('Intel Core i3 Processor', 'AMD Ryzen 5 Hexa Core Processor',
       'Intel Core i5 Processor', 'AMD Ryzen 7 Quad Core Processor',
       'AMD Ryzen 5 Quad Core Processor',
       'AMD Ryzen 9 Octa Core Processor',
       'AMD Ryzen 7 Octa Core Processor', 'Apple M1 Processor',
       'Intel Celeron Dual Core Processor',
       'AMD Ryzen 3 Dual Core Processor',
       'AMD Athlon Dual Core Processor', 'Intel Evo Core i5 Processor',
       'AMD Ryzen 3 Quad Core Processor', 'Apple M2 Processor',
       'Intel Celeron Quad Core Processor', 'Intel Core i7 Processor',
       'Apple M1 Pro Processor', 'Qualcomm Snapdragon 7c Gen 2 Processor',
       'Intel Pentium Silver Processor', 'Apple M1 Max Processor',
       'Intel Core i9 Processor', 'AMD Ryzen 5 Dual Core Processor',
       'Intel Pentium Quad Core Processor', 'AMD Dual Core Processor',
       'AMD Ryzen 3 Hexa Core Processor'))

RAM_size = st.selectbox("Select the type of RAM_size:", ('8', '16', '4', '32', '28'))

bit = st.selectbox("Select the type of bit:", ('64', '32'))

SSD_Storage = st.selectbox("Select the type of SSD_Storage:", ('256 GB ', '512 GB ', '1 TB ', '128 GB ', '2 TB '))

OS = st.selectbox("Select the type of OS:", ('Windows 11', 'Windows 10', 'Chrome'))

RAM_Type = st.selectbox("Select the type of RAM_Type:", ('DDR4', 'DDR5', 'DDR3'))

Display = st.selectbox("Select the type of Display:", (5.56, 39.62, 36.07, 35.81, 38.1 , 38. ))




new_pt = [[Processor, RAM_size, bit, SSD_Storage, OS, RAM_Type, Display]]

new_pt = pd.DataFrame(new_pt, columns = ["Processor", "RAM_size", "bit", "SSD_Storage", "OS", "RAM_Type", "Display"])

pr = model.predict(new_pt)

btn_click = st.button("Predict")

if btn_click == True:
    st.write("This is the predicted price of the laptop based on the features selected:")
    st.write("₹",pr[0])
    


