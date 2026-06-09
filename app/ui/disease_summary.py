import streamlit as st

def render_disease_summary(disease: str, disease_data: dict, protein_data:dict):
    # NOTE: conversion of list to dict for easier lookup!!
    protein_lookup = {
        entry["rcsb_id"]: entry 
        for entry in protein_data["data"]["entries"]
    }
    
    st.subheader(disease)

    wildtype_id = disease_data['wildtype_pdb']
    mutant_id = disease_data['mutant_pdb']

    wt_title = protein_lookup.get(wildtype_id, {}).get('struct', {}).get('title', 'No description available.')
    mt_title = protein_lookup.get(mutant_id, {}).get('struct', {}).get('title', 'No description available.')

    col1, col2 = st.columns(2)
    with col1:
        st.info(f"**Wildtype** `{wildtype_id}`\n\n{wt_title}")
    with col2:
        st.warning(f"**Mutant** `{mutant_id}`\n\n{mt_title}")