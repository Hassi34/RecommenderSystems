import os 
import numpy as np 
import pandas as pd 
import streamlit as st 
import pickle
from pathlib import Path
from os import path
import gzip
from books.loader import load_artifacts
from books.helper import Helper

def render_books():
    st.header("Book Recommender System Using Machine Learning")
    helper = Helper()
    col1, col2 = st.columns(2)
    with col1:
        selected_book = st.selectbox("Type of Select a Book", helper.books_name)

    if st.button("Show Recommendations"):
        predictions = helper.fetch_predictions(selected_book)
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(predictions[0]['title'])
            st.image(predictions[0]['image_url'])
        with col2:
            st.text(predictions[1]['title'])
            st.image(predictions[1]['image_url'])
        with col3:
            st.text(predictions[2]['title'])
            st.image(predictions[2]['image_url'])
        with col4:
            st.text(predictions[3]['title'])
            st.image(predictions[3]['image_url'])

        with col5:
            st.text(predictions[4]['title'])
            st.image(predictions[4]['image_url'])

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.text(predictions[5]['title'])
            st.image(predictions[5]['image_url'])
        with col2:
            st.text(predictions[6]['title'])
            st.image(predictions[6]['image_url'])
        with col3:
            st.text(predictions[7]['title'])
            st.image(predictions[7]['image_url'])
        with col4:
            st.text(predictions[8]['title'])
            st.image(predictions[9]['image_url'])
        with col5:
            st.text(predictions[10]['title'])
            st.image(predictions[10]['image_url'])
