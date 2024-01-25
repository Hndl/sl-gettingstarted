# streamlit_app.py

import streamlit as st
from st_files_connection import FilesConnection
from streamlit.components.v1 import html
import time
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

def plot_wind(dfX: pd.DataFrame) -> None:
    figX = px.line(dfX, y="V_WIND")
    for wind_row in dfX.iterrows():
        figX.add_trace(
            go.Scatter(
                x=[wind_row[0]],
                y=[wind_row[1]['V_WIND']],
                showlegend=False,
                marker=dict(
                    color='red',
                    size=15,
                    symbol='arrow',
                    angle=[wind_row[1]['DIR_WIND']],
                )))
    st.write(figX)
 
def plot_temp(dfX: pd.DataFrame) -> None:
    figX = px.line(dfX, y=["Dew-Point-Temperature","Ambient-Temperature"],Markers=True)
    
    st.write(figX)   

def plot_windX(dfX: pd.DataFrame) -> None:
    figX = px.line(dfX, y="V_WIND")
    figX.update_traces(dict(
        mode='lines+markers',
        marker=dict(
            color='red',
            size=20,
            symbol='triangle-down-open',
            angle=dfX['DIR_WIND']
        )
    ))
    st.write(figX)

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
    fig2 = px.line(df, x="Timestamp_UTC", y=["Measure area - PH_1_S/N: 2213805","Control area - PH_2_S/N: 2213826_CONTROL"], title='PH Level',markers=True)
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

st.markdown("### Test Windspeed and Direction")

np.random.seed(seed=13)

idx = pd.date_range("2023-07-11 10:05", "2023-07-13 23:00", freq='60min')
wind_speeds = np.random.random_sample(size=len(idx)) * 15
wind_directions = np.random.randint(0, high=3600, size=len(idx)) / 10.0


dew_points = np.random.randint(-8, high=5, size=len(idx2))
amb_points = np.random.randint(-10, high=44, size=len(idx2))

dfW = pd.DataFrame({'datetime': idx, 'V_WIND': wind_speeds, 'DIR_WIND': wind_directions,'Ambient-Temperature': amb_points, 'Dew-Point-Temperature': dew_points})
dfW['datetime'] = pd.to_datetime(dfW.datetime)
dfW = dfW.set_index('datetime')
st.dataframe(dfW)










plot_wind(dfW)
plot_temp(dfW)
#plot_windX(dfW)



html(my_html)
