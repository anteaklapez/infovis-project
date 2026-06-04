import os
import json
import streamlit as st

data_path = os.path.join(os.path.dirname(__file__), 'diseases_config.json')

@st.cache_data
def load_config() -> dict:
    with open(data_path) as f:
        return json.load(f)