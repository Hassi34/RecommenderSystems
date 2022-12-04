import gzip
import os
import pickle
from os import path
from pathlib import Path
from pickle import bytes_types
import pandas as pd 
import numpy as np

import streamlit as st


def unzip_artifacts(dir: path = Path(os.path.join('books','artifacts')).resolve().absolute() , ext: tuple = (".gz")) -> None:
    for file in os.listdir(dir):
        if file.endswith(ext):
            file = Path(os.path.join(dir, file)).resolve().absolute()
            with gzip.open(file, 'rb') as f:
                loaded_artifact = pickle.load(f)
            with open(os.path.join(str(file.parent), str(file.stem)), 'wb') as f:
                pickle.dump(loaded_artifact, f)
            os.remove(file)


def load_artifacts(dir : path = Path(os.path.join('books','artifacts')).resolve().absolute()) -> tuple:
    if Path(os.path.join(dir, "model.pkl.gz")).resolve().absolute().exists():
        unzip_artifacts()
    try:
        with open(Path(os.path.join(dir, "model.pkl")).resolve().absolute(), 'rb') as f:
            model = pickle.load(f)
        with open(Path(os.path.join(dir, "books_name.pkl")).resolve().absolute(), 'rb') as f:
            books_name = pickle.load(f)
        with open(Path(os.path.join(dir, "final_ratings.pkl")).resolve().absolute(), 'rb') as f:
            final_rating = pickle.load(f)
        with open(Path(os.path.join(dir, "books_pivot.pkl")).resolve().absolute(), 'rb') as f:
            books_pivot = pickle.load(f)
    except FileNotFoundError:
        unzip_artifacts()
        load_artifacts()
    return (model, books_name, final_rating, books_pivot)