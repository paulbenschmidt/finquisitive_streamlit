import altair as alt
import pandas as pd
import streamlit as st

from utilities.stateful_widgets import stateful_number_input


def tool_financial_growth_calculations():
    st.markdown("# Growth Calculation")

    with st.expander("Inputs", expanded=True) as inputs:
        stateful_number_input(
            key="age",
            label="Enter your age:",
            format="%i", # format as integer
            step=1,
            help="""Enter your age. This will be used to calculate the time it takes to reach your target
                retirement net worth.""",
            min_value=0,
            max_value=100,
        )
        stateful_number_input(
            key="current_net_worth",
            label="Enter your current net worth:",
            format="%i", # format as integer
            step=500,
            help="""Enter your current net worth. This will be used as the starting point for your retirement
                net worth calculation.""",
        )
        stateful_number_input(
            key="retirement_net_worth",
            label="Enter your target retirement net worth:",
            format="%i", # format as integer
            step=500,
            help="""Enter your target retirement net worth. This will be used as the ending point for your retirement
                net worth calculation.""",
        )
        stateful_number_input(
            key="monthly_investment",
            label="Enter your monthly investment contribution amount:",
            format="%i", # format as integer
            step=50,
            help="""Enter your monthly investment contribution amount (income - expenses). This will be used to
                 calculate your rate of growth towards your retirement net worth.""",
            min_value=0,
        )
        stateful_number_input(
            key="roi",
            label="Enter your estimated ROI:",
            format="%.3f", # format as float
            step=0.005,
            help="""Enter your estimated ROI on your net worth. This will be used to calculate your rate of growth.""",
            min_value=0.000,
        )

    current_net_worth_no_roi = st.session_state["current_net_worth"]
    current_net_worth_with_roi = st.session_state["current_net_worth"]
    data = [[st.session_state["age"], current_net_worth_no_roi, current_net_worth_with_roi]]
    age_counter = st.session_state["age"]
    while age_counter < 100:
        age_counter += 1
        current_net_worth_no_roi += st.session_state["monthly_investment"] * 12
        current_net_worth_with_roi += st.session_state["monthly_investment"] * 12
        current_net_worth_with_roi *= (1 + st.session_state["roi"])
        data.append([age_counter, current_net_worth_no_roi, current_net_worth_with_roi])
        if current_net_worth_with_roi >= st.session_state["retirement_net_worth"]:
            break
    chart_data = pd.DataFrame(columns=["Age", "Net Worth (No ROI)", "Net Worth (With ROI)"], data=data)

    st.line_chart(data=chart_data, x="Age", y=("Net Worth (No ROI)", "Net Worth (With ROI)"))

    st.write(f"""
        By contributing **${st.session_state["monthly_investment"]}/month** and getting an average
        **{int(st.session_state["roi"]*100):,}%** annual return on the amount invested, you will reach your retirement
        net worth at age **{chart_data['Age'].max()}**, in
        {int(chart_data['Age'].max() - st.session_state["age"])} years.

        If you're interested in shortening the time it takes to get to your retirement target, you can either
        increase your monthly investment amount or increase your estimated ROI. For shorter time horizons, it is
        more effective to increase your monthly investment amount; while for longer time horizons, it can be more
        effective to increase your estimated ROI because of the compounding effect. However, it is important to note
        that increasing your ROI is often more challenging and riskier than increasing your monthly investment amount.
        We will explore these concepts in more detail in later lessons.
    """)
