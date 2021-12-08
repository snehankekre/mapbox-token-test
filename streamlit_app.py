import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

import os
import subprocess
import sys

@st.experimental_memo
def load_data():
  df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
  return df

if "STREAMLIT_MAPBOX_TOKEN" not in os.environ:
  os.environ["STREAMLIT_MAPBOX_TOKEN"] = st.secrets["token"]

subprocess.run([f"{sys.executable}", "-m", "streamlit", "config", "show"])

df = load_data()

st.pydeck_chart(pdk.Deck(
     map_style='mapbox://styles/mapbox/light-v9',
     initial_view_state=pdk.ViewState(
         latitude=37.76,
         longitude=-122.4,
         zoom=11,
         pitch=50,
     ),
     layers=[
         pdk.Layer(
            'HexagonLayer',
            data=df,
            get_position='[lon, lat]',
            radius=200,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
         ),
         pdk.Layer(
             'ScatterplotLayer',
             data=df,
             get_position='[lon, lat]',
             get_color='[200, 30, 0, 160]',
             get_radius=200,
         ),
     ],
 ))
