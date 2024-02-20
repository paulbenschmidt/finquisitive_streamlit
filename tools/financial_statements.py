import datetime as dt
import math
import numpy as np
import pandas as pd
import streamlit as st

from helper.vars import assets_data_editor, expenses_data_editor, income_data_editor, liabilities_data_editor
from tools.financial_independence_levels import calculate_amortization_amount

YEARS_TO_FORECAST = 30

def tool_financial_statements():
    st.markdown("# Financial Statements")

    with st.expander("Monthly Income"):
        income = income_data_editor()

    with st.expander("Monthly Expenses"):
        expenses = expenses_data_editor(detailed=True)

    with st.expander("Current Assets"):
        assets = assets_data_editor(detailed=True)

    with st.expander("Current Liabilities"):
        liabilities = liabilities_data_editor(detailed=True)

        liabilities["Periods"] = liabilities.apply(
            lambda row: calculate_periods_for_loan(
                principal=row["Amount"],
                apr=row["Interest Rate"],
                monthly_payment=row["Monthly Payment"]
            ),
            axis=1
        )

    if income['Amount'].sum() > 0 and expenses['Amount'].sum() > 0:

        with st.container(border=True):
            st.markdown("#### Balance Sheet")

            col1, col2, col3 = st.columns(3)
            total_assets = int(assets['Amount'].sum())
            normalized_roi = sum(assets['ROI'] * (assets['Amount'] / total_assets))
            col1.metric("Assets", f"${total_assets:,}", f"{normalized_roi:.2%} Average ROI")

            total_liabilities = int(liabilities['Amount'].sum())
            normalized_interest = sum(liabilities['Interest Rate'] * (liabilities['Amount'] / total_liabilities))
            normalized_interest = normalized_interest if not math.isnan(normalized_interest) else 0
            col2.metric("Liabilities", f"${total_liabilities:,}", f"{-normalized_interest:.2%} Average Interest")

            col3.metric("Net Worth", f"${(total_assets - total_liabilities):,}")

        with st.container(border=True):
            st.markdown("#### Profit & Loss Statement")

            col1, col2, col3 = st.columns(3)
            total_income = int(income['Amount'].sum())
            col1.metric("Income", f"${total_income:,}")

            total_expenses = int(expenses['Amount'].sum())
            total_liability_payments = int(liabilities['Monthly Payment'].sum())
            total_expenses_and_payments = int(total_expenses + total_liability_payments)
            col2.metric("Expenses", f"${total_expenses_and_payments:,}")

            net_worth = total_income - total_expenses_and_payments
            col3.metric("Monthly Profit", f"${(net_worth):,}")

        with st.container(border=True):
            st.markdown("#### Financial Forecast")

            annual_profit, monthly_profit = calculate_annual_profit(total_income, total_expenses, liabilities)
            liabilities_by_year, liabilities_by_month = calculate_loan_amounts_over_time(liabilities)
            assets_by_year, assets_by_category_and_year = calculate_asset_amounts_over_time(assets, annual_profit)

            net_worth_by_year = annual_profit\
                .merge(liabilities_by_year, on="Year", how="left")\
                .merge(assets_by_year, on="Year", how="left")
            net_worth_by_year["Liability Balance"].fillna(0, inplace=True)

            net_worth_by_year["Year"] = (net_worth_by_year["Year"] + dt.datetime.now().year).astype(str)
            net_worth_by_year["Net Worth"] = net_worth_by_year["Asset Amount"] - net_worth_by_year["Liability Balance"]

            st.line_chart(
                net_worth_by_year,
                x="Year",
                y=["Asset Amount", "Liability Balance", "Net Worth"],
                # Colors taken from Streamlit theming:
                # https://github.com/streamlit/streamlit/blob/1.19.0/frontend/src/theme/primitives/colors.ts
                color=["#00a4d4", "#ff2b2b", "#09ab3b"],
            )

            milestone_debts = net_worth_by_year[net_worth_by_year["Liability Balance"] == 0].head(1)
            milestone_debts["Milestone"] = "_When will all my debts be paid off?_"
            milestone_expenses = net_worth_by_year[
                net_worth_by_year["Net Worth"] * 0.04 > net_worth_by_year["Expenses & Liability Payments"]
            ].head(1)
            milestone_expenses["Milestone"] = "_According to the 4% rule, when will I be able to withdraw at a rate \
                that covers all my expenses?_"
            milestone_income = net_worth_by_year[
                net_worth_by_year["Net Worth"] * 0.04 > net_worth_by_year["Income"]
            ].head(1)
            milestone_income["Milestone"] = "_According to the 4% rule, when will I be able to withdraw at a rate \
                that equals my income?_"
            milestones = pd.concat([milestone_debts, milestone_expenses, milestone_income], ignore_index=True)
            if len(milestones) > 0:
                milestones["Years to Milestone"] = milestones["Year"].astype(int) - dt.datetime.now().year
                milestones.sort_values(by=['Year'], inplace=True)

                st.write("""
                    If you were to continue living with the current income and expenses without taking on additional
                    liabilities while investing all monthly profit across your current assets, the chart above shows
                    the growth of your assets and the reduction of your liabilities over time.

                    According to your current trajectory, you are on track to reach the following milestones:
                """)
                if len(milestones) >= 1:
                    write_milestone(milestones, 0)
                if len(milestones) >= 2:
                    write_milestone(milestones, 1)
                if len(milestones) >= 3:
                    write_milestone(milestones, 2)

            st.divider()

            st.write("""
                If you're unhappy with your current trajectory, feel free to play around with
                a few variations to see how that would affect your forecast. Some ideas include:
                - Increasing your **monthly profit** by reducing expenses or increasing income
                - Increasing the expected **ROI** of your assets
                - Increasing your **monthly payment** toward any liabilities to pay them off faster
            """)


def calculate_periods_for_loan(principal, apr, monthly_payment):
    # https://www.rocketloans.com/learn/financial-smarts/how-to-calculate-monthly-payment-on-a-loan
    if principal == 0 or apr == 0:
        return 0
    elif monthly_payment == 0:
        st.warning("""
            **Warning!** By paying $0 per month, the loan will continue to grow indefinitely. To avoid this, add
            a monthly payment.
        """)
    else:
        monthly_rate = apr / 12
        dividend = np.log(monthly_payment / (monthly_payment - (monthly_rate * principal)))
        divisor = np.log(1 + monthly_rate)
        periods = dividend / divisor
        try:
            return int(periods + 1)
        except ValueError:
            st.warning(f"""
                **Warning!** By paying \${monthly_payment} per month, the loan will grow faster than it is being paid off. To
                avoid this, consider paying at least
                \${calculate_amortization_amount(principal, apr, YEARS_TO_FORECAST * 12):,.2f} per month in order to
                pay it off in 30 years.
            """)
    return 12 * YEARS_TO_FORECAST


def calculate_annual_profit(total_income, total_expenses, liabilities):
    monthly_profit = []
    for x in range(1, (12 * (YEARS_TO_FORECAST + 1))):
        total_liability_payments_for_month = liabilities[liabilities["Periods"] >= x]["Monthly Payment"].sum()
        monthly_profit.append([x, total_income, total_expenses, total_liability_payments_for_month])

    monthly_profit = pd.DataFrame(
        columns=["Month", "Income", "Expenses", "Liability Payments"],
        data=monthly_profit
    )
    monthly_profit["Expenses & Liability Payments"] = monthly_profit["Expenses"] + monthly_profit["Liability Payments"]
    monthly_profit["Profit"] = monthly_profit["Income"] - monthly_profit["Expenses & Liability Payments"]

    monthly_profit["Year"] = monthly_profit["Month"] // 12

    annual_profit = monthly_profit.groupby("Year").agg({
        "Income": "sum",
        "Expenses": "sum",
        "Liability Payments": "sum",
        "Expenses & Liability Payments": "sum",
        "Profit": "sum"
    }).reset_index()

    return annual_profit, monthly_profit # Returning monthly_profit for debugging purposes


def calculate_loan_amounts_over_time(liabilities):
    """
    Calculate the amount of each loan over time, given the principal, interest rate, and monthly payment.
    """

    liabilities_by_month = []
    for ix, row in liabilities.iterrows():
        amount = row["Amount"]
        liabilities_by_month.append([row["Category"], -1, 0, amount]) # Initial amount
        for period in range(1, row["Periods"] + 1):
            principal_payment = row["Monthly Payment"] - (amount * (row["Interest Rate"] / 12))
            amount -= principal_payment
            liabilities_by_month.append([row["Category"], period, principal_payment, max(amount, 0)])

    liabilities_by_month = pd.DataFrame(
        liabilities_by_month, columns=["Category", "Period", "Principal Payment", "Liability Balance"]
    )

    liabilities_by_month["Year"] = (liabilities_by_month["Period"] // 12) + 1

    liabilities_by_category_and_year = liabilities_by_month.groupby(["Category", "Year"]).agg({
        "Liability Balance": "min"
    }).reset_index()

    liabilities_by_year = liabilities_by_category_and_year.groupby(["Year"]).agg({
        "Liability Balance": "sum"
    }).reset_index()

    return liabilities_by_year, liabilities_by_month # Returning liabilities_by_month for debugging purposes


def calculate_asset_amounts_over_time(assets, annual_profit):
    """
    Calculate the amount of each asset over time, given the ROI for each asset.
    """

    total_asset_amount = assets['Amount'].sum()
    annual_growth = []
    for ix, asset in assets.iterrows():
        amount = asset["Amount"]
        asset_distribution = amount / total_asset_amount
        annual_growth.append([asset["Category"], 0, 0, amount]) # Initial amount
        for year in range(1, YEARS_TO_FORECAST + 1):
            profit_for_year = annual_profit.loc[annual_profit["Year"] == year, "Profit"].values[0]
            profit_for_year_by_asset = profit_for_year * asset_distribution
            amount *= (1 + asset["ROI"])
            amount += profit_for_year_by_asset
            annual_growth.append([asset["Category"], year, profit_for_year_by_asset, amount])


    assets_by_category_and_year = pd.DataFrame(
        columns=["Category", "Year", "Profit for Year", "Asset Amount"], data=annual_growth
    )
    assets_by_year = assets_by_category_and_year.groupby("Year").agg({"Asset Amount": "sum"}).reset_index()
    return assets_by_year, assets_by_category_and_year # Returning assets_by_category_and_year for debugging purposes


def write_milestone(milestones, ix):
    return st.markdown(f"""
            {ix + 1}. {milestones["Milestone"].iloc[ix]} In **{milestones["Years to Milestone"].iloc[ix]} years
            ({milestones["Year"].iloc[ix]})** when net worth is **${int(milestones["Asset Amount"].iloc[ix]):,}**.
        """)


### TODO: Distribute profit across asset according to distribution
