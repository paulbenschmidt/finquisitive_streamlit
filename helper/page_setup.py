from PIL import Image

import streamlit as st


def setup_page():
    st.set_page_config(
        page_title="FinQuisitive",
        page_icon=Image.open("./static/logo_black.png"),
        layout="wide"
    )
