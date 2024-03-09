import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
import pickle

from src.pipeline.prediction_pipeline import PredictPipeline,CustomData

st.set_page_config("wide")
selected = option_menu("Main menu", ["home", "Diamond Price Predictor","Info"], icons=["house", "diamond","Info"],
                       orientation="horizontal")

with st.sidebar:
    st.header(":blue[About Me] :man:")
    st.write("I am an AI and Data Science Student. Passionate about Data science and ML")
    github_emoji = "\U0001F680"
    github_link = f"[Github Profile {github_emoji}](https://github.com/BHEESETTIANAND)"
    st.markdown(github_link, unsafe_allow_html=True)
    st.write("To see my work, please visit the link to my portfolio below.")
    portfolio_link = "https://anandbheesetti.wixsite.com/portfolio"
    st.markdown(portfolio_link, unsafe_allow_html=True)
    gmail_emoji = "\U0001F4E7"
    st.markdown(f"email me at {gmail_emoji}")
    st.write("anandbheesetti@gmail.com")

if selected == "home":
    st.title(" Diamond Price Predictor")
    st.write("With the help of this project Predict the Price of your Diamond")
    st.image("th.jpg")
    
    
if selected == "Diamond Price Predictor":
    data = CustomData(
        carat=st.number_input("**Enter the carat value of diamond**"),
        depth=st.number_input("**Enter the Depth value**"),
        table=st.number_input("**Enter the table value**"),
        x=st.number_input("**Enter the X value**"),
        y=st.number_input("**Enter the  Y value**"),
        z=st.number_input("**Enter the Z  value**"),
        cut=st.selectbox("Select the cut type of your diamond", ("Fair", "Good", "Very Good", "Premium", "Ideal")),
        color=st.selectbox("Select the color type of your diamond", ("D", 'E', 'F', 'G', 'H', 'I', 'J')),
        clarity=st.selectbox("Select the Clarity type of your diamond", ("I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"))
    )

    final_data = data.get_data_as_dataframe()

    predict_pipeline = PredictPipeline()

    pred = predict_pipeline.predict(final_data)

    result = round(pred[0], 2)

    if st.button("Predict"):
        st.write(result)
        
if selected=="Info":
    st.image("four-cs-of-diamonds-grahams.jpg")
    

