from PIL import Image

import streamlit as st


def setup_page():
    st.set_page_config(
        page_title="FinQuisitive",
        page_icon=Image.open("./static/logo_black.png"),
        layout="wide"
    )

    hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    [data-testid="stToolbarActions"] {visibility: hidden;}
    #viewerBadge_link__qRIco {visibility: hidden;}
    </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
