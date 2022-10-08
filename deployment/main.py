import streamlit as st
from streamlit_option_menu import option_menu 
import json
import eda
import prediction

# Membuat sidebar untuk navigasi
with st.sidebar:
    selected = option_menu('Menu',
                           ['Exploratory Data Analysis (EDA)',
                            'Churn Prediction'],
                            icons = ['bar-chart-fill', 'people'],
                            default_index = 0)

# Mengatur halaman
if (selected == 'Exploratory Data Analysis (EDA)'):
    eda.run()
else:
    prediction.run()