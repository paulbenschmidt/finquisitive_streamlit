import altair as alt
import pandas as pd
import streamlit as st


def tool_financial_growth_calculations():
    st.markdown("# Growth Calculation")

    with st.expander("Inputs", expanded=True) as inputs:
        age = st.number_input(
            "Enter your age:",
            value=18,
        )
        current_net_worth = st.number_input(
            "Enter your current net worth:",
            value=0,
        )
        retirement_net_worth = st.number_input(
            "Enter your target retirement net worth:",
            value=1000000,
        )
        monthly_investment = st.number_input(
            "Enter your monthly investment contribution amount (income - expenses):",
            value=200,
        )
        roi = st.number_input("Enter your estimated ROI:", value=0.07, placeholder="Estimated ROI")

    current_net_worth_no_roi = current_net_worth
    current_net_worth_with_roi = current_net_worth
    data = [[age, current_net_worth_no_roi, current_net_worth_with_roi]]
    age_counter = age
    while age_counter < 100:
        age_counter += 1
        current_net_worth_no_roi += monthly_investment * 12
        current_net_worth_with_roi += monthly_investment * 12
        current_net_worth_with_roi *= (1 + roi)
        data.append([age_counter, current_net_worth_no_roi, current_net_worth_with_roi])
        if current_net_worth_with_roi >= retirement_net_worth:
            break
    chart_data = pd.DataFrame(columns=["Age", "Net Worth (No ROI)", "Net Worth (With ROI)"], data=data)

    st.line_chart(data=chart_data, x="Age", y=("Net Worth (No ROI)", "Net Worth (With ROI)"))

    st.write(f"""
        By contributing **${monthly_investment}/month** and getting an average **{int(roi*100):,}%** annual return on
        the amount invested, you will reach your retirement net worth at age **{chart_data['Age'].max()}**, in
        {int(chart_data['Age'].max() - age)} years.

        If you're interested in shortening the time it takes to get to your retirement target, you can either
        increase your monthly investment amount or increase your estimated ROI. For shorter time horizons, it is
        more effective to increase your monthly investment amount; while for longer time horizons, it can be more
        effective to increase your estimated ROI because of the compounding effect. However, it is important to note
        that increasing your ROI is often more challenging and riskier than increasing your monthly investment amount.
        We will explore these concepts in more detail in later lessons.
    """)
