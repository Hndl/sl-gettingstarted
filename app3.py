# streamlit_app.py

import streamlit as st
from st_files_connection import FilesConnection

st.title("Test App No.3" )


# Create connection object and retrieve file contents.
# Specify input format is a csv and to cache the result for 600 seconds.
conn = st.connection('s3', type=FilesConnection)
df = conn.read("vw-ram-site-a/master-data/master.csv", input_format="csv", ttl=600)



# Print results.
#Timestamp_UTC,ControlareaRedSen,MeasureareaBlueSen,Voltage,MeasurearePH_1_S/N:A,ControlareaPH_2_SN

for row in df.itertuples():
    st.write(f"{row.Owner} has a :{row.Pet}:")
