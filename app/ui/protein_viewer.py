import streamlit as st
import os
import py3Dmol

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def render_protein_viewer(label: str, pdb_id: str, variant: str, description: str = ""):
    accent = "#28251d"   
    st.markdown(
        f"<div style='display:flex; align-items:center; gap:8px; margin-bottom:4px;'>"
        f"<span style='width:10px; height:10px; border-radius:50%; background:{accent}; display:inline-block;'></span>"
        f"<span style='font-weight:600;'>{label}</span>"
        f"<code style='color:{accent}; background:transparent;'>{pdb_id}</code>"
        f"</div>",
        unsafe_allow_html=True,
    )

    pdb_path = os.path.join(BASE_DIR, '..', 'data', 'proteins', f'{pdb_id}.pdb')
    pdb_path = os.path.normpath(pdb_path)

    if not os.path.exists(pdb_path):
        st.warning(f"PDB file not found: {pdb_path}")
        return

    with open(pdb_path) as f:
        pdb_data = f.read()

    view = py3Dmol.view(width=390, height=160)
    view.addModel(pdb_data, "pdb")
    view.setStyle({
        "cartoon": {
            "colorscheme": {
                "prop": "ss",
                "map": {"h": "#01696f", "s": "#ca5b33", "": "#a8cdd0"}
            }
        }
    })
    view.zoomTo()

    viewer_width = 320
    viewer_height = 230

    html = f"""
    <div style="display:flex; justify-content:center; align-items:center; width:100%;">
        <div style="width:{viewer_width}px; height:{viewer_height}px;">
            {view._make_html()}
        </div>
    </div>
    """

    st.iframe(html, height=160)

    if description:
        st.caption(description)