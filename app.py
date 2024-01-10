import streamlit as st
import numpy as np
import pandas as pd


st.title("Test App - " + st.secrets.env_test)

data_load_state = st.text('Loading data...')

data = pd.read_csv(st.secrets.test.data_file)

data_load_state.text('Loading data...done!')

st.subheader('Raw data')
st.write(data)
