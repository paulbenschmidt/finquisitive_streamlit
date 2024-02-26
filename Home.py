import streamlit as st

from helper.page_setup import setup_page


setup_page()

st.write("# Welcome to FinQuisitive! 👋")

# TODO: Create all variables in cache
# TODO: Create authentication (to capture email)
# TODO: Create donation page

st.markdown("""
    **FinQuisitive** is a financial literacy application designed to teach financial principles interactively.

    While there are many books and courses that teach financial literacy, we felt that there was a lack of
    interactive tools that could help people learn about finance in a more engaging and relatable way. We hope that
    FinQuisitive can fill that gap. And we hope that having a framework to think about your future will help
    inspire creative ways of living today that will lead to a life of abundance for yourself and those around you!

    With love and gratitude,

    The FinQuisitive Team
""")
