import pandas as pd
import streamlit as st

from helper.vars import assets_data_editor, expenses_data_editor, income_data_editor, liabilities_data_editor


def tool_financial_position_comparison():
    st.markdown("# Financial Position Comparison")

    age = st.number_input("Enter your age:", value=0, placeholder="Age")

    with st.expander("Monthly Income"):
        income = income_data_editor()

    with st.expander("Monthly Expenses"):
        expenses = expenses_data_editor()

    with st.expander("Current Assets"):
        assets = assets_data_editor()

    with st.expander("Current Liabilities"):
        liabilities = liabilities_data_editor()

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
        st.markdown(f"Comparing results to Age {age}")
        net_worth_median = int(current_metrics.loc[current_metrics["Age"] == age]["Net Worth: Values to Use"].values[0])
        income_median = int(current_metrics.loc[current_metrics["Age"] == age]["Income: Values to Use"].values[0])
        expenses_median = int(current_metrics.loc[current_metrics["Age"] == age]["Expenses: Values to Use"].values[0])

        individual_net_worth = assets['Amount'].sum() - liabilities['Amount'].sum()
        individual_income = income['Amount'].sum() * 12
        individual_assets = assets['Amount'].sum()
        individual_expenses = expenses['Amount'].sum() * 12
        individual_liabilities = liabilities['Amount'].sum()

        with st.container(border=True):
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
