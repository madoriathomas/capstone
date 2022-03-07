import streamlit as st
import pandas as pd
import plotly as px

st.write("# What's New?")

corpus = pd.read_csv("data\\labeled_newscatcher_dataset.csv",  sep=";")

topics = st.sidebar.radio(label='Choose Your Topic:',
    options=['TECHNOLOGY', 'BUSINESS', 'HEALTH', 'ENTERTAINMENT', 'NATION', 'SPORTS', 'WORLD', 'SCIENCE'])

st.write(f"# {topics}")

subset_df= corpus.loc[corpus['topic'] == topics]

types = corpus['title'].value_counts().reset_index()
types = types.rename(columns={'index':'Type', 'title': 'Count'})

fig = px.pie(types, values='Count', names='Type',
              color_discrete_sequence=px.colors.qualitative.Pastel)
st.write(fig)

