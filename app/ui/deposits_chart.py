import streamlit as st
import plotly.express as px
import pandas as pd
from styles.palette import TEAL, BG


def render_deposits_chart(deposits_timeline: list):
    if not deposits_timeline:
        st.warning("No deposit timeline data.")
        return

    df = pd.DataFrame(deposits_timeline, columns=["year", "count"])
    df["year"] = pd.to_datetime(df["year"]).dt.year

    fig = px.bar(
        df, x="year", y="count",
        labels={"year": "Year", "count": "Structures Deposited"},
        color_discrete_sequence=[TEAL],
        
    )
    fig.update_layout(
        margin=dict(l=0, r=10, t=80, b=40), 
        height=400,
        title=dict(
            text="PDB Deposits Over Time",
            subtitle=dict(
                text="Number of disease-related structures deposited to PDB per year.",
                font=dict(size=14, color="#7a7974")
            )
        )
        )
    
    st.plotly_chart(fig, width='stretch')