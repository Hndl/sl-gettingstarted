# streamlit_app.py

import streamlit as st
from st_files_connection import FilesConnection
from streamlit.components.v1 import html
import time

st.set_page_config()

my_html = """
<script>
window.onload = function () {
   setInterval(function () {location.reload();}, 300000);
};
</script>
"""

html(my_html)

st.title("Test App No.3 using secrets more" )


# Create connection object and retrieve file contents.
# Specify input format is a csv and to cache the result for 600 seconds.
conn = st.connection(st.secrets.sourcedata.fs, type=FilesConnection)
df = conn.read(st.secrets.sourcedata.data_uri, input_format=st.secrets.sourcedata.format, ttl=st.secrets.sourcedata.ttl)



# Print results.
#Timestamp_UTC,ControlareaRedSen,MeasureareaBlueSen,Voltage,MeasurearePH_1_S/N:A,ControlareaPH_2_SN

for row in df.itertuples():
    st.write(f"{row.Owner} has a :{row.Pet}:")
