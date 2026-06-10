import streamlit as st
import plotly.express as px
import pandas as pd
from styles.palette import TEAL_LIGHT, BG


def render_resolution_hist(resolution_hist: list):
    if not resolution_hist:
        st.warning("No resolution data.")
        return

    df = pd.DataFrame(resolution_hist, columns=["resolution", "count"])

    fig = px.bar(
        df, x="resolution", y="count",
        labels={"resolution": "Resolution (Å)", "count": "Count"},
        color_discrete_sequence=[TEAL_LIGHT],        
    )
    fig.update_layout(
        margin=dict(l=0, r=10, t=80, b=40), 
        height=400,
        title=dict(
            text="Resolution Distribution — All Structures",
            subtitle=dict(
                text="Distribution of structural resolution across all disease proteins.",
                font=dict(size=14, color="#7a7974")
            )
        ))
    st.plotly_chart(fig, width='stretch')