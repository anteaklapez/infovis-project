import streamlit as st
import plotly.express as px
from styles import palette

def render_methods_chart(methods_pie):
    st.markdown("""
        <style>
        [data-testid="stPlotlyChart"] {
            padding: 0;
            border-radius: 10px;
            box-shadow: none;
            background: transparent;
        }
        </style>
    """, unsafe_allow_html=True)

    labels = [item[0] for item in methods_pie]
    values = [item[1] for item in methods_pie]
    fig = px.pie(names=labels, values=values, title = "Experimental Methods", color_discrete_sequence=palette.PIE_COLORS)
    fig.update_traces(textinfo="none", hovertemplate="%{label}<br>%{percent}<extra></extra>")
    fig.update_layout(height=330, 
                      showlegend = True, margin=dict(l=10, r=10, t=40, b=10),
                      legend=dict(orientation="h", yanchor="bottom", y=-0.15, xanchor="center", x=0.5))
    st.plotly_chart(fig, use_container_width=True)