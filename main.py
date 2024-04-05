#o código vai aqui
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

df_reviews = pd.read_csv("./dataassets/customer reviews.csv")
df_top100_books = pd.read_csv("./dataassets/Top-100 Trending Books.csv")

df_reviews