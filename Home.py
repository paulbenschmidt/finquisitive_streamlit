import streamlit as st

from helper.page_setup import setup_page


setup_page()

st.write("# Welcome to FinQuisitive! 👋")

# TODO: Create authentication (to capture email)
# TODO: Create donation page

st.markdown("""
    **FinQuisitive** is a financial literacy application designed to teach financial principles interactively.

    While there are many books and courses that teach financial literacy, we felt that there was a lack of
    interactive tools that could help people learn about finance in a more engaging and relatable way:
    FinQuisitive fills that gap. In addition to calculating with your personal finance projections and quantifying
    your decisions, you'll learn a simple, efficient framework that takes the mystery out of finance and investing,
    providing principles for enjoying the most of life and wealth today _and_ in the future.

    To get started, **click the first lesson below** or use the sidebar on the left to navigate to a specific lesson:
""")

with st.container(border=True):
    st.page_link("pages/1_🐣_Lesson_1:_Where_Are_You_Now.py" , label="Lesson 1: Where Are You Now?", icon="➡️")

st.write("""
    To your success,

    The FinQuisitive Team
""")

