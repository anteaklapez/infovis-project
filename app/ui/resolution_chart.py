import streamlit as st
import plotly.express as px
import pandas as pd

def render_resolution_bar(protein_data, wildtype_id, mutant_id):
    entries = protein_data.get("data", {}).get("entries", [])

    rows = []
    for entry in entries:
        entry_id = entry.get("rcsb_id")
        if entry_id not in [wildtype_id, mutant_id]:
            continue

        resolution = (entry.get("rcsb_entry_info", {}).get("resolution_combined"))

        if isinstance(resolution, list):
            resolution = resolution[0]

        variant = "Wildtype" if entry_id == wildtype_id else "Mutant"

        rows.append({"entry_id": entry_id, "variant":  variant, "resolution": resolution})

    df = pd.DataFrame(rows)
    df = df[df["resolution"].notna()]

    if df.empty:
        st.info("No resolution data available — structures were determined by NMR, which does not produce a resolution value.")
        return

    fig = px.bar(df, x="entry_id", y="resolution", color="variant", title="Resolution Structure",
        labels={"entry_id": "Protein Structure", "resolution": "Resolution (Å)"},
        color_discrete_map={"Wildtype": "blue", "Mutant": "red"},
    )

    fig.update_traces(textposition="outside")
    fig.update_layout(
        yaxis=dict(title="Resolution (Å)", rangemode="tozero"),
        showlegend=True,
        bargap=0.4,
        height = 400
    )

    st.plotly_chart(fig, width='stretch', key="resolution_chart")