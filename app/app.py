import streamlit as st
from pages.protein_explorer import render_protein_explorer
from api.search_api import dashboard_query
from styles.load_styles import load_css


st.set_page_config(
    page_title="Protein & Disease Dashboard",
    page_icon="🧬",
    layout="wide",
)

load_css()
render_protein_explorer() 