import streamlit as st


def render_filters(config: dict) -> tuple[str, str, dict]:
    col1, col2 = st.columns(2)

    categories = list(config.keys())

    with col1:
        selected_category = st.selectbox("Category", categories)

    with col2:
        selected_disease = st.selectbox(
            "Disease",
            list(config[selected_category].keys())
        )

    return selected_category, selected_disease, config[selected_category][selected_disease]