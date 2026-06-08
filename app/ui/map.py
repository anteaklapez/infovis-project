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

    years = sorted(df['year'].unique().tolist())
    selected_year = st.slider(
        "Year",
        min_value=int(years[0]),
        max_value=int(years[-1]),
        value=int(years[-1]),
        step=1
    )

    df_year = df[df['year'] == selected_year]

    fig = px.choropleth(
        df_year,
        locations='location_name',
        locationmode='country names',
        color='val',
        hover_name='location_name',
        hover_data={'val': ':.2f', 'location_name': False},
        color_continuous_scale='Reds',
        title=f'Global Prevalence Rate per 100,000 — {selected_year}'
    )

    fig.update_layout(
        margin=dict(l=0, r=0, t=40, b=0),
        height=420,
        coloraxis_colorbar=dict(title="Rate per 100k")
    )

    fig.update_traces(
    hovertemplate='<b>%{hovertext}</b><br>Rate: %{customdata[0]:,.2f} per 100k<extra></extra>')


    st.plotly_chart(fig, width='stretch')