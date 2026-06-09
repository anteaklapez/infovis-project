import streamlit as st
from ui.disease_summary import render_disease_summary
from ui.protein_viewer import render_protein_viewer
from ui.map import render_map
from ui.filters import render_filters
from data.data_loader import load_config
from ui.pie_chart import render_methods_chart
from ui.resolution_chart import render_resolution_bar
from api.search_api import disease_query
from api.data_api import data_query

@st.cache_data
def load_disease_query(wildtype_id, mutant_id):
    return disease_query(wildtype_id, mutant_id)

@st.cache_data
def load_protein_data():
    return data_query()

def render_protein_explorer():
    config = load_config()

    selected_category, selected_disease, disease_data = render_filters(config)
    disease_data_query = load_disease_query(disease_data["wildtype_pdb"], disease_data["mutant_pdb"])
    protein_data = load_protein_data()

    #render_disease_summary(selected_disease, disease_data, protein_data)
    wt_title, mt_title = render_disease_summary(selected_disease, disease_data, protein_data)

    main_left, main_right = st.columns([1, 1.3])

    with main_left:
        with st.container(border=True):
            render_protein_viewer("Wildtype", disease_data["wildtype_pdb"], "wildtype", wt_title)
        with st.container(border=True):
            render_protein_viewer("Mutant", disease_data["mutant_pdb"], "mutant", mt_title)

    with main_right:
        with st.container(border=True):
            render_map(disease_data["map_fn"])


    with st.container(border=True):
        pie_col, res_col = st.columns(2)
        with pie_col:
            render_methods_chart(disease_data_query["methods_pie"])
        with res_col:
            render_resolution_bar(protein_data, disease_data["wildtype_pdb"], disease_data["mutant_pdb"])

        
