import altair as alt
import pandas as pd
import streamlit as st


def plot_two_net_worth_points(data):
    chart_data = pd.DataFrame(columns=["Age", "Net Worth"], data=data)

    c = (
    alt.Chart(chart_data)
    .mark_circle()
    .encode(
        x=alt.Y("Age", scale=alt.Scale(domain=[19, 51]), axis=alt.Axis(tickMinStep = 1)),
        y=alt.Y("Net Worth", scale=alt.Scale(domain=[min(chart_data["Net Worth"].min(), 0), chart_data["Net Worth"].max()])),
        size=alt.Y("Net Worth", scale=alt.Scale(domain=[-chart_data["Net Worth"].max(), chart_data["Net Worth"].max()]), legend=None),
        )
    )

    st.altair_chart(c, use_container_width=True)
