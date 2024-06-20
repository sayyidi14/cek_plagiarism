import numpy as np
import pandas as pd

import nltk

import streamlit as st


# Inisialisasi stemmer dan stopwords
stemmer = PorterStemmer()
stop_words = set(stopwords.words('indonesian'))

df= pd.read_csv("coba.csv")
df
