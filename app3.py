# streamlit_app.py

import streamlit as st
from st_files_connection import FilesConnection

st.title("Test App No.3" )


# Create connection object and retrieve file contents.
# Specify input format is a csv and to cache the result for 600 seconds.
conn = st.connection('s3', type=FilesConnection)
df = conn.read("vw-ram-site-a/master-data/master.csv", input_format="csv", ttl=600)



# Print results.
#for row in df.itertuples():
#    st.write(f"{row.Controlarea-RedSen} has a :{row.Measurearea-BlueSen}:")
