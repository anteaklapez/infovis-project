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

    return wt_title, mt_title # captions for protein viewer


  