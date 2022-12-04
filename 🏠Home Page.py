import streamlit as st 
from streamlit_lottie import st_lottie
import requests
import os
import json

st.set_page_config(
    page_title="Recommender Systems",
    layout="wide",
    initial_sidebar_state="expanded",)

with open (os.path.join(os.getcwd(),'static', 'reviews.json'), "r") as f:
    reviews = json.load(f)

with open (os.path.join(os.getcwd(),'static', 'stars_client.json'), "r") as f:
    client = json.load(f)

col1, col2 = st.columns(2)

with col1:
    st_lottie(reviews, key="reviews")
with col2:
    st_lottie(client, key="client")