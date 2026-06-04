import streamlit as st
import os
import py3Dmol

def render_protein_viewer(label: str, pdb_id: str, variant: str):
    st.markdown(f"**{label}** — `{pdb_id}`")

    pdb_path = f"data/proteins/{pdb_id}.pdb"

    if not os.path.exists(pdb_path):
        st.warning(f"PDB file not found: {pdb_path}")
        return

    with open(pdb_path) as f:
        pdb_data = f.read()

    view = py3Dmol.view(width=360, height=320)
    view.addModel(pdb_data, "pdb")
    view.setStyle({
        "cartoon": {
            "colorscheme": {
                "prop": "ss",
                "map": {"h": "red", "s": "yellow", "": "green"}
            }
        }
    })
    view.zoomTo()

    viewer_width = 320
    viewer_height = 300

    html = f"""
    <div style="display:flex; justify-content:center; align-items:center; width:100%;">
        <div style="width:{viewer_width}px; height:{viewer_height}px;">
            {view._make_html()}
        </div>
    </div>
    """

    st.iframe(html, height=340)