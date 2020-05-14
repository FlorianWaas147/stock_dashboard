import streamlit as st
import yfinance as yf
import numpy as np
import pandas as pd



list_of_investments = pd.read_csv('list_of_investments.csv')

# Define sidebar ######################################################

st.sidebar.markdown('# Finance Dashboard')
selection = st.sidebar.selectbox(label='Select investment', options=list_of_investments)
delete = st.sidebar.button(label='Remove selection from list', key= 'remove')


# Main page #####################################################

st.write(selection)
st.write(list_of_investments)
st.write(delete)

if delete:
    list_of_investments = list_of_investments.loc[list_of_investments.values != selection]
    delete = False

st.write(selection)
st.write(list_of_investments)
st.write(delete)