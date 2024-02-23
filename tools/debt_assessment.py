import pandas as pd
import streamlit as st


def tool_debt_assessment():
    st.markdown("# Debt Assessment")

    st.write("""
        As part of this lesson, we're going to take a deep dive into our debts (also called liabilities) and analyze
        each one to determine the best path forward to reaching our financial independence.
        Every debt that is removed is money that stops working against us (by growing over time in the
        negative direction) and becomes additional savings that can be redirected to purchasing assets (which
        grow over time in the positive direction), letting us get to our financial goal even sooner!
    """)

    st.write("""
        In the chart below, provide the following information for each debt:
        - The name
        - The amount owed
        - The annual interest rate
        - The appreciation percentage earned (if it applies), such as home appreciation
        - The income earned (if it applies), such as rental income
    """)

    liabilities = st.data_editor(
        pd.DataFrame(
            data= [["", 0, 0.0, 0.0, 0]],
            columns=["Debt Name", "Amount", "Interest", "Appreciation", "Income",]
        ),
        use_container_width=True,
        column_config={
            "Debt Name": st.column_config.TextColumn(
                label="Debt Name",
                help="The name of debt",
                required=False,
                width="medium",
            ),
            "Amount": st.column_config.NumberColumn(
                format="$%d",
                help="The amount owed for this debt",
                required=True,
                width="small",
            ),
            "Interest": st.column_config.NumberColumn(
                format="%.2f",
                help="The annual interest rate for this debt",
                required=True,
                width="small",
            ),
            "Appreciation": st.column_config.NumberColumn(
                label="Appreciation",
                help="The appreciation rate earned from this debt",
                format="%.2f",
                default=0,
                required=False,
                width="small",
            ),
            "Income": st.column_config.NumberColumn(
                label="Income",
                help="The annual income earned from this debt",
                format="$%d",
                default=0,
                required=False,
                width="small",
            ),
        },
        num_rows="dynamic",
    )

    liabilities["net_annual_cost"] = \
        (liabilities["Amount"] * -liabilities["Interest"]) + \
        (liabilities["Amount"] * liabilities["Appreciation"]) + liabilities["Income"]

    liabilities_text_helper = ""
    for i in range(len(liabilities)):
        debt_name = liabilities['Debt Name'][i] if liabilities['Debt Name'][i] is not None else f"Debt #{i + 1}"
        liabilities_text_helper += f"- {debt_name}"
        is_negative = liabilities["net_annual_cost"][i] < 0
        liabilities_text_helper += ": -" if is_negative else ": +"
        liabilities_text_helper += f"${abs(liabilities['net_annual_cost'][i]):,.2f}\n"

    net_annual_sum = liabilities["net_annual_cost"].sum()
    if net_annual_sum != 0:
        base_text = f"""
            Observing the net annual change (appreciation + income - interest) across all debts, the total net annual
            change is: **{"-" if net_annual_sum < 0 else "+"}${abs(net_annual_sum):,.2f}**.
        """
        if net_annual_sum >= 0:
            text = f"""
                Congratulations! {base_text} This means that the debts are currently working for you, earning you money
                over time. Keep it up!
            """
            st.success(text)
        else:
            text = f"""
                {base_text} This means that the debts are currently working against you, costing you money over time.
                In order to overcome the negative momentum of these debts, you can either work to pay them off
                or find investments that earn more than the debts are costing you.
            """
            st.warning(text)

    st.write("""
        In the financial world, debt can be measured against income or assets and helps determine our financial
        health, or the amount of leverage we have. In order to reduce risk, ideally, we want this ratio to be as low
        as possible. Debt is a tool that should be used with caution in order to
        avoid situations where the amount owed (debt) is greater than the amount owned (assets). In the 2008
        financial crisis, after the housing market crashed, many people found themselves in this exact situation:
        the debts on the homes ended up being greater than the value of the homes themselves, meaning that the
        thousands of people were over-leveraged and had to sell their homes at a loss or declare bankruptcy.
    """)
