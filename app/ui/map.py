import streamlit as st
import pandas as pd
import plotly.express as px
import os

def render_map(map_fn: str):
    map_path = f'data/maps/{map_fn}'

    if not os.path.exists(map_path):
        st.warning(f"Map data not found: {map_path}")
        return
    
    df = pd.read_csv(map_path)

    loc_cols = {'location', 'country', 'location_name', 'iso_code', 'iso3'}
    loc_col = next((c for c in df.columns if c.lower() in loc_cols), df.columns[0])
    val_col = next((c for c in df.columns if c.lower() not in loc_cols), df.columns[-1])

    fig = px.choropleth(
        df,
        locations=loc_col,
        locationmode="ISO-3",
        color=val_col,
        title='Global Disease Burden'
    )

    fig.update_layout(margin=dict(l=0, r=0, t=40, b=0), height=420)
    st.plotly_chart(fig, width='stretch')