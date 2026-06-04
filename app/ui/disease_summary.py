import streamlit as st

def render_disease_summary(category: str, disease: str, disease_data: dict):
    st.subheader(disease)
    st.caption(
        f"{category} | Wildtype: {disease_data['wildtype_pdb']} - Mutant: {disease_data['mutant_pdb']}"
    )