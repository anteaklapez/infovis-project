import streamlit as st
import pandas as pd
import plotly.express as px
import os
import country_converter as coco
from styles import palette
   

_CC = coco.CountryConverter()

@st.cache_data
def _load(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def render_map(map_fn: str):
    map_path = os.path.join(BASE_DIR, '..', 'data', 'maps', map_fn)
    map_path = os.path.normpath(map_path)

    if not os.path.exists(map_path):
        st.warning(f"Map data not found: {map_path}")
        return

    df = pd.read_csv(map_path)

    vmin, vmax = df["val"].min(), df["val"].max()

    years = sorted(df['year'].unique().tolist())
    selected_year = st.slider(
        "Year",
        min_value=int(years[0]),
        max_value=int(years[-1]),
        value=int(years[-1]),
        step=1
    )

    df_year = df[df['year'] == selected_year]

    df_year = df_year.groupby("location_name", as_index=False)["val"].mean()

    df_year["iso3"] = _CC.convert(df_year["location_name"].tolist(),
                                      to="ISO3")
    df_year = df_year[df_year["iso3"] != "not found"]


    fig = px.choropleth(
        df_year,
        locations="iso3",
        locationmode="ISO-3",
        color='val',
        hover_name='location_name',
        range_color=[vmin, vmax],
        color_continuous_scale=palette.MAP_SCALE,
        title=f'Global Prevalence Rate per 100,000 — {selected_year}'
    )

    fig.update_layout(
        margin=dict(l=0, r=0, t=40, b=0),
        height=420,
        coloraxis_colorbar=dict(title="Rate per 100k")
    )

    fig.update_traces(
        hovertemplate="<b>%{hovertext}</b><br>Rate: %{z:,.2f} per 100k<extra></extra>"
    )


    st.plotly_chart(fig, width='stretch', use_container_width=True)