# streamlit_app.py

import streamlit as st
from st_files_connection import FilesConnection

st.title("Test App No.3" )

data_load_state.text('Loading data ' + st.secrets.sourcedata.data_uri)

# Create connection object and retrieve file contents.
# Specify input format is a csv and to cache the result for 600 seconds.
conn = st.connection(st.secrets.sourcedata.fs, type=FilesConnection)
df = conn.read(st.secrets.sourcedata.data_uri, input_format=st.secrets.sourcedata.format, ttl=st.secrets.sourcedata.ttl)

data_load_state.text('Loading data...done!')

st.write(data)

# Print results.
#for row in df.itertuples():
#    st.write(f"{row.Controlarea-RedSen} has a :{row.Measurearea-BlueSen}:")
