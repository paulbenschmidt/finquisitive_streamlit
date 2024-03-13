import pandas as pd
import streamlit as st


def tool_asset_assessment():
    st.markdown("# Asset Assessment")

    st.write("""
    """)

    st.write("""
    """)

    with st.expander("Inputs", expanded=True) as inputs:
        current_age = st.number_input(
            "Enter your age:",
            value=18,
        )
        net_worth = st.number_input(
            "Enter your current net worth:",
            value=0,
        )
        retirement_annual_income = st.number_input(
            "Enter your target retirement annual income:",
            value=100000,
        )
        monthly_investment = st.number_input(
            "Enter your monthly investment contribution amount (income - expenses):",
            value=200,
        )

    age = current_age
    data = [[age, net_worth, net_worth, net_worth, net_worth, net_worth, net_worth, net_worth]]
    net_worth_0 = net_worth
    net_worth_5 = net_worth
    net_worth_10 = net_worth
    net_worth_15 = net_worth
    net_worth_20 = net_worth
    net_worth_25 = net_worth
    net_worth_30 = net_worth
    for i in range(0, 30):
        age = age + 1
        net_worth_0 = (net_worth_0 + (monthly_investment * 12)) * 1.00
        net_worth_5 = (net_worth_5 + (monthly_investment * 12)) * 1.05
        net_worth_10 = (net_worth_10 + (monthly_investment * 12)) * 1.10
        net_worth_15 = (net_worth_15 + (monthly_investment * 12)) * 1.15
        net_worth_20 = (net_worth_20 + (monthly_investment * 12)) * 1.20
        net_worth_25 = (net_worth_25 + (monthly_investment * 12)) * 1.25
        net_worth_30 = (net_worth_30 + (monthly_investment * 12)) * 1.30
        data.append([age, net_worth_0, net_worth_5, net_worth_10, net_worth_15, net_worth_20, net_worth_25, net_worth_30])

    chart_data = pd.DataFrame(
        columns=["Age", "0% ROI", "05% ROI", "10% ROI", "15% ROI", "20% ROI", "25% ROI", "30% ROI"],
        data=data
    )

    st.line_chart(data=chart_data, x="Age", y=("0% ROI", "05% ROI", "10% ROI", "15% ROI", "20% ROI", "25% ROI", "30% ROI"))

    st.write(f"""By contributing {monthly_investment}/month, you would have the following net worth:""")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(f"""
        In 5 years:
        - ${chart_data.iloc[5]['0% ROI']:,.2f} at 0% ROI
        - ${chart_data.iloc[5]['05% ROI']:,.2f} at 5% ROI
        - ${chart_data.iloc[5]['10% ROI']:,.2f} at 10% ROI
        - ${chart_data.iloc[5]['15% ROI']:,.2f} at 15% ROI
        - ${chart_data.iloc[5]['20% ROI']:,.2f} at 20% ROI
        - ${chart_data.iloc[5]['25% ROI']:,.2f} at 25% ROI
        - ${chart_data.iloc[5]['30% ROI']:,.2f} at 30% ROI
        """)
    with col2:
        st.write(f"""
        In 15 years:
        - ${chart_data.iloc[15]['0% ROI']:,.2f} at 0% ROI
        - ${chart_data.iloc[15]['05% ROI']:,.2f} at 5% ROI
        - ${chart_data.iloc[15]['10% ROI']:,.2f} at 10% ROI
        - ${chart_data.iloc[15]['15% ROI']:,.2f} at 15% ROI
        - ${chart_data.iloc[15]['20% ROI']:,.2f} at 20% ROI
        - ${chart_data.iloc[15]['25% ROI']:,.2f} at 25% ROI
        - ${chart_data.iloc[15]['30% ROI']:,.2f} at 30% ROI
        """)
    with col3:
        st.write(f"""
        In 25 years:
        - ${chart_data.iloc[25]['0% ROI']:,.2f} at 0% ROI
        - ${chart_data.iloc[25]['05% ROI']:,.2f} at 5% ROI
        - ${chart_data.iloc[25]['10% ROI']:,.2f} at 10% ROI
        - ${chart_data.iloc[25]['15% ROI']:,.2f} at 15% ROI
        - ${chart_data.iloc[25]['20% ROI']:,.2f} at 20% ROI
        - ${chart_data.iloc[25]['25% ROI']:,.2f} at 25% ROI
        - ${chart_data.iloc[25]['30% ROI']:,.2f} at 30% ROI
        """)

    retirement_ages = {}
    for i in range(len(chart_data), 1, -1):
        for roi in reversed(["0% ROI", "05% ROI", "10% ROI", "15% ROI", "20% ROI", "25% ROI", "30% ROI"]):
            if chart_data.iloc[i-1][roi] - chart_data.iloc[i-2][roi] >= retirement_annual_income:
                retirement_ages[roi] = [chart_data.iloc[i-1]['Age'], chart_data.iloc[i-1][roi]]

    text = f"""
        Achieving a higher ROI on your investments not only enables your investments to grow faster, but
        it also gives you the freedom to retire with a _lower_ net worth, since the investments are
        generating more income and replenishing more quickly.

        For example, by contributing \${monthly_investment}/month, in order to reach your target retirement annual
        income of ${retirement_annual_income:,}:
    """
    for ix, (roi, age_and_nw) in enumerate(retirement_ages.items()):
        text += f"""
        - At a {roi} and , you can retire in {int(age_and_nw[0] - current_age)} years at **age {int(age_and_nw[0])}**
        with a net worth of ${age_and_nw[1]:,.2f}"""
    st.write(text)
