import streamlit as st
from pages.protein_explorer import render_protein_explorer

st.set_page_config(
    page_title="Protein & Disease Dashboard",
    page_icon="🧬",
    layout="wide",
)

render_protein_explorer()