import pandas as pd
import streamlit as st


def tool_financial_position_comparison():
    st.markdown("# Financial Position Comparison")

    age = st.number_input(
        "Enter your age:",
        value=0,
        format="%i", # format as integer
        help="Enter your age. This will be used to compare against the average financial position for your age group."
    )
    income = st.number_input(
        "Total annual income:",
        value=60000,
        format="%i", # format as integer
        help="Enter your total annual income across all active and passive sources (salary, contract work, rental income, etc.)"
    )
    expenses = st.number_input(
        "Total monthly expenses:",
        value=5000,
        format="%i", # format as integer
        help="Enter your total monthly expenses across all categories (housing, transportation, food, taxes, etc.)"
    )
    assets = st.number_input(
        "Total assets:",
        value=0,
        format="%i", # format as integer
        help="Enter your total assets (cash, investments, stocks, real estate, etc.)"
    )
    liabilities = st.number_input(
        "Total liabilities/debts:",
        value=0,
        format="%i", # format as integer
        help="Enter your total liabilities (mortgage, car loans, student loans, credit card debt, etc.)"
    )

    current_metrics = pd.read_csv("./data/financial_position_comparison_data_2024.csv")
    minimum_age = current_metrics["Age"].min()
    maximum_age = current_metrics["Age"].max()

    if age <= 0:
        age = 0
    elif age < minimum_age and age > 0:
        age = current_metrics["Age"].min()
    elif age > maximum_age:
        age = current_metrics["Age"].max()

    if age == 0:
        st.markdown("Enter age and additional details to see your financial position comparison.")

    else:
        net_worth_median = int(current_metrics.loc[current_metrics["Age"] == age]["Net Worth: Values to Use"].values[0])
        income_median = int(current_metrics.loc[current_metrics["Age"] == age]["Income: Values to Use"].values[0])
        expenses_median = int(current_metrics.loc[current_metrics["Age"] == age]["Expenses: Values to Use"].values[0])

        individual_net_worth = assets - liabilities
        individual_income = income
        individual_assets = assets
        individual_expenses = expenses * 12
        individual_liabilities = liabilities

        with st.container(border=True):
            st.subheader(f"Median Financial Comparison for Age {age}")
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
