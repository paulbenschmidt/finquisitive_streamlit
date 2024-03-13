import pandas as pd
import streamlit as st

from utilities.stateful_widgets import stateful_number_input


def tool_financial_position_comparison():
    st.markdown("## Financial Position Comparison")

    st.write("""
        Using the inputs below, let's calculate your current financial position and compare it to the
        median values for your age group.
    """)

    stateful_number_input(
        key="age",
        label="Enter your age:",
        format="%i", # format as integer
        step=1,
        help="Enter your age. This will be used to compare against the average financial position for your age group.",
        min_value=0,
        max_value=100,
    )
    stateful_number_input(
        key="income",
        label="Total annual income:",
        format="%i", # format as integer
        step=500,
        help="Enter your total annual income across all active and passive sources (salary, contract work, rental income, etc.)",
        min_value=0,
    )
    stateful_number_input(
        key="expenses",
        label="Total monthly expenses:",
        format="%i", # format as integer
        step=50,
        help="Enter your total monthly expenses across all categories (housing, transportation, food, etc.)",
        min_value=0,
    )
    stateful_number_input(
        key="assets",
        label="Total assets:",
        format="%i", # format as integer
        step=500,
        help="Enter your total assets (cash, investments, stocks, real estate, etc.)",
        min_value=0,
    )
    stateful_number_input(
        key="liabilities",
        label="Total liabilities/debts:",
        format="%i", # format as integer
        step=500,
        help="Enter your total liabilities (mortgage, car loans, student loans, credit card debt, etc.)",
        min_value=0,
    )

    current_metrics = pd.read_csv("./data/financial_position_comparison_data_2024.csv")
    minimum_age = current_metrics["Age"].min()
    maximum_age = current_metrics["Age"].max()

    if st.session_state["age"] <= 0:
        age = 0
    elif st.session_state["age"] < minimum_age:
        age = minimum_age
    elif st.session_state["age"] > maximum_age:
        age = maximum_age
    else:
        age = st.session_state["age"]

    if age == 0:
        st.warning("Enter age and additional details to see your financial position comparison.")

    else:
        net_worth_median = int(current_metrics.loc[current_metrics["Age"] == age]["Net Worth: Values to Use"].values[0])
        income_median = int(current_metrics.loc[current_metrics["Age"] == age]["Income: Values to Use"].values[0])
        expenses_median = int(current_metrics.loc[current_metrics["Age"] == age]["Expenses: Values to Use"].values[0])

        individual_assets = st.session_state["assets"]
        individual_liabilities = st.session_state["liabilities"]
        individual_net_worth = individual_assets - individual_liabilities
        individual_income = st.session_state["income"]
        individual_expenses = st.session_state["expenses"] * 12

        with st.container(border=True):
            st.subheader(f"Your Financial Standing Against Median Values for Your Age Group")
            st.metric(
                "Net Worth", f"${individual_net_worth:,}",
                f"{(individual_net_worth - net_worth_median) / net_worth_median:.2%} from ${net_worth_median:,}"
            )
            col1, col2 = st.columns(2)
            col1.metric(
                "Annual Income", f"${individual_income:,}",
                f"{(individual_income - income_median) / income_median:.2%} from ${income_median:,}"
            )
            col2.metric("Assets", f"${individual_assets:,}")
            col1, col2 = st.columns(2)
            col1.metric(
                "Annual Expenses", f"${individual_expenses:,}",
                f"{(individual_expenses - expenses_median) / expenses_median:.2%} from ${expenses_median:,}",
                delta_color="inverse"
            )
            col2.metric("Liabilities", f"${individual_liabilities:,}")
            css='''
            [data-testid="stHeading"] {
                width: fit-content;
                margin: auto;
            }
            [data-testid="stHeading"] > div {
                width: fit-content;
                margin: auto;
            }
            [data-testid="stHeading"] h3 {
                width: fit-content;
                margin: auto;
            }
            [data-testid="stMetric"] {
                width: fit-content;
                margin: auto;
            }
            [data-testid="stMetric"] > div {
                width: fit-content;
                margin: auto;
            }
            [data-testid="stMetric"] label {
                width: fit-content;
                margin: auto;
            }
            '''
        st.markdown(f'<style>{css}</style>',unsafe_allow_html=True)
