# 1. Import dependencies
import streamlit as st
import pandas as pd
import numpy as np

# 2. Define Page Configurations
st.set_page_config(
    page_title="Breast Cancer Predictor",
    page_icon=":female-doctor:",
    layout="wide",
    initial_sidebar_state="expanded"
  )

# 3. Add the sidebar for the application
st.sidebar.header("Cell Nuclei Measurements")

with st.container():
    st.title('Breast Cancer Predictor')
    st.write('Please connect this app to your cytology lab to help diagnose breast cancer form your tissue sample. This app predicts using a machine learning model whether a breast mass is benign or malignant based on the measurements it receives from your cytosis lab. You can also update the measurements by hand using the sliders in the sidebar.')

col1, col2 = st.columns([4,1])

with col1:
    st.write('Column 1')
    #radar_chart = get_radar_chart(input_data)
    #st.plotly_chart(radar_chart)
with col2:
    st.write('Column 2')
    #add_predictions(input_data)