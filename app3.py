# streamlit_app.py

import streamlit as st
from st_files_connection import FilesConnection
from streamlit.components.v1 import html
import time
import plotly.express as px



st.set_page_config(
    page_title="Real-Time VW POC Dashboard",
    page_icon="✅",
    layout="wide",
)
#parent.window.location.reload()
my_html = """
<script>
window.onload = function () {
   setInterval(function () {location.reload();}, 60000);
};
</script>
"""



st.title("Test App No.3 : 1 min" )


# Create connection object and retrieve file contents.
# Specify input format is a csv and to cache the result for 600 seconds.
conn = st.connection(st.secrets.sourcedata.fs, type=FilesConnection)
df = conn.read(st.secrets.sourcedata.data_uri, input_format=st.secrets.sourcedata.format, ttl=st.secrets.sourcedata.ttl)

 # create two columns for charts 
fig_col1, fig_col2 = st.columns(2)
with fig_col1:
    st.markdown("### First Chart")
    fig = px.line(df, x="Owner", y=["Pet","MeasureareaBlueSen"], title='Sensor Blue/Red')
    st.write(fig)
            
with fig_col2:
    st.markdown("### Second Chart")
    fig2 = px.line(df, x="Owner", y=["MeasurearePH_1_S/N:A","ControlareaPH_2_SN"], title='PH 2')
    st.write(fig2)

st.markdown("### Detailed Data View")
st.dataframe(df)

# Print results.
#Timestamp_UTC,ControlareaRedSen,MeasureareaBlueSen,Voltage,MeasurearePH_1_S/N:A,ControlareaPH_2_SN

#for row in df.itertuples():
#    st.write(f"{row.Owner} has a :{row.Pet}: :: {row.Voltage}")








html(my_html)
