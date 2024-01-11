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
# takes too much space on page
#st.title("POC Dashboard" ) 

# Create connection object and retrieve file contents.
# Specify input format is a csv and to cache the result for 600 seconds.
conn = st.connection(st.secrets.sourcedata.fs, type=FilesConnection)
df = conn.read(st.secrets.sourcedata.data_uri, input_format=st.secrets.sourcedata.format, ttl=st.secrets.sourcedata.ttl)

 # create two columns for charts 
fig_col1, fig_col2, fig_col3 = st.columns(3)
with fig_col1:
    #st.markdown("### Redox") too much spage
    fig = px.line(df, x="Timestamp_UTC", y=["Control area - Redox 1_Red Sensor","Measure area - Redox 2_Blue Sensor"], title='Redox Blue/Red',markers=True)
    fig.update_traces(textposition="bottom right")
    st.write(fig)
            
with fig_col2:
    #st.markdown("### PH") too much space
    fig2 = px.line(df, x="Timestamp_UTC", y=["Measure area - PH_1_S/N: 2213805","Control area - PH_2_S/N: 2213826_CONTROL"],line_dash="Voltage", title='PH Level',markers=True)
    fig2.update_traces(textposition="bottom right")
    st.write(fig2)

with fig_col3:
    #st.markdown("### Voltage") too much spage
    fig3 = px.line(df, x="Timestamp_UTC", y="Voltage", title='Voltage', markers=True, text="Voltage")
    fig3.update_traces(textposition="bottom right")
    st.write(fig3)

st.markdown("### Detailed Data View")
st.dataframe(df)

# Print results.
#Timestamp_UTC,ControlareaRedSen,MeasureareaBlueSen,Voltage,MeasurearePH_1_S/N:A,ControlareaPH_2_SN

#for row in df.itertuples():
#    st.write(f"{row.Owner} has a :{row.Pet}: :: {row.Voltage}")








html(my_html)
