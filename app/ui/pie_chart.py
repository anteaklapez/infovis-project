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
    st.markdown("**Experimental Methods**")
    st.markdown(
        '<p style="font-size:14px; color:#7a7974; margin-top:-12px;">Experimental methods used to determine the 3D structures of the wildtype and mutant proteins.</p>',
        unsafe_allow_html=True
    )

    labels = [item[0] for item in methods_pie]
    values = [item[1] for item in methods_pie]
    fig = px.pie(names=labels, values=values, color_discrete_sequence=palette.PIE_COLORS)
    fig.update_traces(textinfo="none", hovertemplate="%{label}<br>%{percent}<extra></extra>")
    fig.update_layout(
        height=330, 
        showlegend = True, margin=dict(l=10, r=10, t=20, b=10),
        legend=dict(orientation="h", yanchor="bottom", y=-0.15, xanchor="center", x=0.5)
    )
    st.plotly_chart(fig, width='stretch')