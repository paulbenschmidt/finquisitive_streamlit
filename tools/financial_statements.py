import datetime as dt
import math

import numpy as np
import pandas as pd
import streamlit as st

from tools.financial_independence_levels import calculate_amortization_amount
from utilities.stateful_widgets import stateful_multiselect, stateful_number_input


YEARS_TO_FORECAST = 30

def tool_financial_statements():
    st.markdown("# Financial Statements")

    with st.expander("**Income**"):
        stateful_number_input(
            key="income_active",
            label="Total annual active income:",
            format="%i", # format as integer
            step=1000,
            help="Enter your total annual active income across all sources (salary, contract work, etc.)",
            min_value=0,
        )
        stateful_number_input(
            key="income_passive",
            label="Total annual passive income:",
            format="%i", # format as integer
            step=1000,
            help="Enter your total annual passive income across all sources (dividends, rental income, etc.)",
            min_value=0,
        )
        income = create_income_df()
        st.write(f"Total annual income: **${(income['Amount'].sum() * 12):,}**")
        st.write(f"Total monthly income: **${income['Amount'].sum():,}**")

    with st.expander("**Expenses**"):
        expenses_options = ["Education", "Entertainment", "Family", "Fitness", "Food", "Gifts", "Housing",
                            "Other", "Personal Care", "Pets", "Shopping", "Taxes", "Travel"]
        expenses_selections = stateful_multiselect(
            key="expenses_selections",
            label="Select any expense categories that you want to include:",
            options=expenses_options,
            initial_value=["Housing"],
        )
        for option in expenses_options:
            if option in expenses_selections:
                st.write(f"**{option}**")
                stateful_number_input(
                    key=f"expenses_amount_for_{option.lower()}",
                    label=f"Expenses Amount for {option}",
                    format="%i", # format as integer
                    step=50,
                    help=f"Enter the total monthly expenses amount for the {option} category",
                    label_visibility="collapsed",
                    min_value=0,
                )
        expenses = create_expenses_df(expenses_selections)
        st.write(f"Total monthly expenses: **${expenses['Amount'].sum():,}**")

    with st.expander("**Assets**"):
        asset_options = ["Checking", "Savings", "Stocks", "Bonds", "Real Estate", "Retirement Accounts", "Other"]
        asset_selections = stateful_multiselect(
            key="asset_selections",
            label="Select any asset categories that you want to total:",
            options=asset_options,
            initial_value=["Checking"],
        )
        for option in asset_options:
            if option in asset_selections:
                st.write(f"**{option}**")
                col1, col2 = st.columns(2)
                with col1:
                    stateful_number_input(
                        key=f"asset_amount_for_{option.lower()}",
                        label="Amount:",
                        help=f"Enter the total asset amount for the {option} category",
                        format="%i", # format as integer
                        step=100,
                        min_value=0,
                    )
                with col2:
                    stateful_number_input(
                        key=f"asset_roi_for_{option.lower()}",
                        label="ROI (expressed as decimal):",
                        help=f"Enter the expected annual return-on-investment (ROI) of the {option} category",
                        format="%.3f", # format as float
                        step=0.005,
                        min_value=0.000,
                    )
                st.divider()
        assets = create_assets_df(asset_selections)
        st.write(f"Total asset amount: **${assets['Amount'].sum():,}**")

    with st.expander("**Liabilities**"):
        liabilities_options = ["Mortgage Debt", "Car Loans", "Credit Card", "School Loans", "Medical Debt", "Other"]
        liabilities_selections = stateful_multiselect(
            key="liabilities_selections",
            label="Select any liability categories that you want to total:",
            options=liabilities_options,
            initial_value=["Mortgage Debt"],
        )
        for option in liabilities_options:
            if option in liabilities_selections:
                st.write(f"**{option}**")
                col1, col2, col3 = st.columns(3)
                with col1:
                    stateful_number_input(
                        key=f"liability_amount_for_{option.lower()}",
                        label="Amount:",
                        help=f"Enter the total liability amount for the {option} category",
                        step=100,
                        format="%i", # format as integer
                        min_value=0,
                    )
                with col2:
                    stateful_number_input(
                        key=f"liability_interest_for_{option.lower()}",
                        label="Annual Interest Rate (expressed as decimal):",
                        help=f"Enter the annual interest rate for the {option} category",
                        step=0.005,
                        format="%.3f", # format as float
                        min_value=0.000,
                    )
                with col3:
                    stateful_number_input(
                        key=f"liability_monthly_payment_for_{option.lower()}",
                        label="Monthly Payment:",
                        help=f"Enter the monthly payment for the {option} category",
                        step=50,
                        format="%i", # format as integer
                        min_value=0,
                    )
                calculate_periods_for_loan(option=option)
                st.divider()
        liabilities = create_liabilities_df(liabilities_selections)
        st.write(f"Total liability amount: **${liabilities['Amount'].sum():,}**")

    if not(income["Amount"].sum() > 0 and expenses["Amount"].sum() > 0 and assets["Amount"].sum() > 0):
        with st.container(border=True):
            st.markdown("""
                To calculate the financial statements, fill out the **income**, **expenses**, **assets**,
                and **liabilities** sections.
            """)
    else:
        with st.container(border=True):
            st.markdown("#### Balance Sheet")

            col1, col2, col3 = st.columns(3)
            total_assets = int(assets['Amount'].sum())
            if total_assets > 0:
                normalized_roi = sum(assets['ROI'] * (assets['Amount'] / total_assets))
            if len(assets) == 0:
                normalized_roi = 0
            else:
                normalized_roi = sum(assets['ROI'] * (1 / len(assets)))
            col1.metric("Assets", f"${total_assets:,}", f"{normalized_roi:.2%} Average ROI")

            total_liabilities = int(liabilities['Amount'].sum())
            normalized_interest = sum(liabilities['Interest Rate'] * (liabilities['Amount'] / total_liabilities))
            normalized_interest = normalized_interest if not math.isnan(normalized_interest) else 0
            col2.metric("Liabilities", f"${total_liabilities:,}", f"{-normalized_interest:.2%} Average Interest")

            col3.metric("Net Worth", f"${(total_assets - total_liabilities):,}")

        with st.container(border=True):
            st.markdown("#### Monthly Profit & Loss Statement")

            col1, col2, col3 = st.columns(3)
            total_income = int(income['Amount'].sum())
            col1.metric("Income", f"${total_income:,}")

            total_expenses = int(expenses['Amount'].sum())
            total_liability_payments = int(liabilities['Monthly Payment'].sum())
            total_expenses_and_payments = int(total_expenses + total_liability_payments)
            col2.metric("Expenses", f"${total_expenses_and_payments:,}")

            net_worth = total_income - total_expenses_and_payments
            col3.metric("Profit", f"${(net_worth):,}")

        with st.container(border=True):
            st.markdown("#### Financial Forecast")

            stateful_number_input(
                key="years_to_forecast",
                label="Years to Forecast:",
                format="%i", # format as integer
                step=1,
                help="Enter the number of years to forecast",
                min_value=0,
                max_value=YEARS_TO_FORECAST,
                initial_value=YEARS_TO_FORECAST,
            )

            annual_profit, monthly_profit = calculate_annual_profit(total_income, total_expenses, liabilities)
            liabilities_by_year, liabilities_by_month = calculate_loan_amounts_over_time(liabilities)
            assets_by_year, assets_by_category_and_year = calculate_asset_amounts_over_time(assets, annual_profit)

            net_worth_by_year = annual_profit\
                .merge(liabilities_by_year, on="Year", how="left")\
                .merge(assets_by_year, on="Year", how="left")
            net_worth_by_year["Liability Balance"] = net_worth_by_year["Liability Balance"].fillna(0)

            net_worth_by_year["Year"] = (net_worth_by_year["Year"] + dt.datetime.now().year).astype(str)
            net_worth_by_year["Net Worth"] = net_worth_by_year["Asset Amount"] - net_worth_by_year["Liability Balance"]

            net_worth_to_forecast = net_worth_by_year.head(int(st.session_state["years_to_forecast"]))

            st.line_chart(
                net_worth_to_forecast,
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


def calculate_periods_for_loan(option):
    # https://www.rocketloans.com/learn/financial-smarts/how-to-calculate-monthly-payment-on-a-loan
    principal = st.session_state[f"liability_amount_for_{option.lower()}"]
    apr = st.session_state[f"liability_interest_for_{option.lower()}"]
    monthly_payment = st.session_state[f"liability_monthly_payment_for_{option.lower()}"]
    if principal == 0:
        periods_to_use = 0
    elif apr == 0 or monthly_payment == 0:
        st.warning("""
            **Warning!** By paying $0 per month, the loan will continue to grow indefinitely. To avoid this, add
            a monthly payment.
        """)
        periods_to_use = 12 * YEARS_TO_FORECAST
    else:
        monthly_rate = apr / 12
        dividend = np.log(monthly_payment / (monthly_payment - (monthly_rate * principal)))
        divisor = np.log(1 + monthly_rate)
        periods = dividend / divisor
        try:
            if int(periods + 1) > 12 * YEARS_TO_FORECAST:
                st.warning(f"""
                    **Warning!** By paying \${monthly_payment} per month, the loan will take more than 30 years to
                    pay off. To pay it off in less than 30 years, consider paying at least
                    \${calculate_amortization_amount(principal, apr, YEARS_TO_FORECAST * 12):,.2f} per month.
                """)
            periods_to_use = int(periods + 1)
        except ValueError:
            st.warning(f"""
                **Warning!** By paying \${monthly_payment} per month, the loan will grow faster than it is being
                paid off. To avoid this, consider paying at least
                \${calculate_amortization_amount(principal, apr, YEARS_TO_FORECAST * 12):,.2f} per month in order to
                pay it off in 30 years.
            """)
            periods_to_use = 12 * YEARS_TO_FORECAST
    st.session_state[f"liability_periods_for_{option.lower()}"] = periods_to_use


def create_income_df():
    income = []
    for option in ["active", "passive"]:
        income.append([
            option.capitalize(),
            int(st.session_state[f"income_{option}"] / 12),
        ])
    income = pd.DataFrame(
        columns=["Category", "Amount"],
        data=income
    )
    return income


def create_expenses_df(expenses_selections):
    expenses = []
    for option in expenses_selections:
        if "cache_helper" not in option:
            expenses.append([option, st.session_state[f"expenses_amount_for_{option.lower()}"]])
    expenses = pd.DataFrame(
        columns=["Category", "Amount"],
        data=expenses
    )
    return expenses


def create_assets_df(asset_selections):
    assets = []
    for option in asset_selections:
        if "cache_helper" not in option:
            assets.append([
                option,
                st.session_state[f"asset_amount_for_{option.lower()}"],
                st.session_state[f"asset_roi_for_{option.lower()}"],
            ])
    assets = pd.DataFrame(
        columns=["Category", "Amount", "ROI"],
        data=assets
    )
    return assets


def create_liabilities_df(liabilities_selections):
    liabilities = []
    for option in liabilities_selections:
        if "cache_helper" not in option:
            liabilities.append([
                option,
                st.session_state[f"liability_amount_for_{option.lower()}"],
                st.session_state[f"liability_interest_for_{option.lower()}"],
                st.session_state[f"liability_monthly_payment_for_{option.lower()}"],
                st.session_state[f"liability_periods_for_{option.lower()}"],
            ])
    liabilities = pd.DataFrame(
        columns=["Category", "Amount", "Interest Rate", "Monthly Payment", "Periods"],
        data=liabilities
    )
    return liabilities


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
        amount = asset["Amount"] if asset["Amount"] > 0 else 0
        roi = asset["ROI"] if asset["ROI"] > 0 else 0
        if total_asset_amount > 0:
            asset_distribution = (amount / total_asset_amount)
        else:
            asset_distribution = 1 / len(assets)
        annual_growth.append([asset["Category"], 0, 0, amount]) # Initial amount
        for year in range(1, YEARS_TO_FORECAST + 1):
            profit_for_year = annual_profit.loc[annual_profit["Year"] == year, "Profit"].values[0]
            profit_for_year_by_asset = profit_for_year * asset_distribution
            amount *= (1 + roi)
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
