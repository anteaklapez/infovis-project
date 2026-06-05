import streamlit as st
import plotly.express as px

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
    fig = px.pie(names=labels, values=values, title = "Experimental Methods")
    fig.update_layout(height=330, width=290, showlegend = False, margin=dict(l=10, r=10, t=40, b=10))
    st.plotly_chart(fig, use_container_width=False)