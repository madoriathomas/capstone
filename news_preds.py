from copyreg import pickle
import streamlit as st
import pandas as pd

st.title("News Headline Predictions")

st.subheader("Please enter your text here: ")

headline_input= st.text_input(
    label='Headline Prediction',
    max_chars= 120
)

loaded_model = pickle.load(open('../models/mnb_model.pkl', 'rb'))


if st.button('Generate Predictions'):
    test_data = pd.DataFrame(columns = ['topic', 'title'])

    test_data = test_data.append({'title': headline_input}, 
                            ignore_index=True)

    prediction = loaded_model.predict(test_data)

    st.write(f"({prediction})")