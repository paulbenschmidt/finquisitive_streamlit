import pandas as pd
import streamlit as st


def assets_data_editor(detailed=False):
    if detailed:
        st.write("""
            For each asset, provide an estimate on the annual return-on-investment (ROI) of that asset in terms of its
            appreciation; if the asset provides income (like a rental property), include that under the income section.
            This doesn't need to be exact, but it's helpful to have a rough idea of the ROI of each asset. For example:
            - a checking account might have an ROI of 0.00 (0%)
            - a savings account might have an ROI of 0.01 (1%)
            - a rental property might have an ROI of 0.04 (4%)
            - a stock/index fund might have an ROI of 0.07 (7%)
        """)

    data = [["Checking", 0]]
    columns = ["Category", "Amount"]
    column_config = {
        "Category": st.column_config.SelectboxColumn(
            label="Category (Dropdown)",
            help="The category of asset",
            options=[
                "Checking",
                "Savings",
                "Stocks",
                "Bonds",
                "Real Estate",
                "Retirement Accounts",
                "Other",
            ],
            required=True,
            width="large",
        ),
        "Amount": st.column_config.NumberColumn(
            help="The amount/worth of each asset",
            format="$%d",
            default=0,
            required=True,
            width="medium",
        )
    }
    if detailed:
        columns.append("ROI")
        data[0].append(0.00)
        column_config["ROI"] = st.column_config.NumberColumn(
            help="The expected annual return-on-investment (ROI) of the asset",
            format="%.2f",
            default=0,
            required=True,
            width="medium",
        )

    return st.data_editor(
        pd.DataFrame(columns=columns, data=data),
        column_config=column_config,
        num_rows="dynamic",
    )

def expenses_data_editor(detailed=False):
    st.write("""
        For all expenses, enter the **monthly** average amount of the expense.
    """)
    if detailed:
        st.write("""
            *Note*: if the expense is related to a liability (like a mortgage or car payment), include that under the
            liabilities section.
        """)
    return st.data_editor(
        pd.DataFrame(data= [["Other", 0]], columns=["Category", "Amount"]),
        column_config={
            "Category": st.column_config.SelectboxColumn(
                label="Category (Dropdown)",
                help="The category of expense",
                options=[
                    "Taxes",
                    "Housing",
                    "Transportation",
                    "Food",
                    "Restaurants",
                    "Entertainment",
                    "Other"
                ],
                required=True,
                width="large",
            ),
            "Amount": st.column_config.NumberColumn(
                help="The amount of each expense",
                format="$%d",
                default=0,
                required=True,
                width="medium",
            )
        },
        num_rows="dynamic",
    )

def income_data_editor():
    st.write("""
        For all sources of income, enter the **monthly** amount of income.
    """)
    return st.data_editor(
        pd.DataFrame(columns=["Category", "Amount"], data=[["Employment", 0]]),
        column_config={
            "Category": st.column_config.SelectboxColumn(
                label="Category (Dropdown)",
                help="The category of debt",
                options=[
                    "Employment",
                    "Passive Income",
                    "Other",
                ],
                required=True,
                width="large",
            ),
            "Amount": st.column_config.NumberColumn(
                help="The monthly amount earned from each income source",
                format="$%d",
                default=0,
                required=True,
                width="medium",
            )
        },
        num_rows="dynamic",
    )

def liabilities_data_editor(detailed=False):
    if detailed:
        st.write("""
            For each liability, provide an approximation of the interest rate on that liability. This doesn't need to
            be exact, but it's helpful to have a rough idea of the interest rate on each liability. For example:
            - a mortgage might have an interest rate of 0.04 (4%)
            - a car loan might have an interest rate of 0.05 (5%)
            - a student loan might have an interest rate of 0.06 (6%)
            - a credit card might have an interest rate of 0.20 (20%)
        """)

    data = ["Mortgage Debt", 0]
    columns = ["Category", "Amount"]
    column_config = {
        "Category": st.column_config.SelectboxColumn(
            label="Category (Dropdown)",
            help="The category of debt",
            options=[
                "Mortgage Debt",
                "Car Loans",
                "Credit Card",
                "School Loans",
                "Medical Debt",
                "Other",
            ],
            required=True,
            width="medium" if detailed else "large",
        ),
        "Amount": st.column_config.NumberColumn(
            help="The amount of each debt",
            format="$%d",
            default=0,
            required=True,
            width="medium",
        )
    }
    if detailed:
        data.extend([0.04, 0])
        columns.extend(["Interest Rate", "Monthly Payment"])
        column_config["Interest Rate"] = st.column_config.NumberColumn(
            help="The annual interest rate of each debt",
            format="%.2f",
            default=0,
            required=True,
            width="medium",
        )
        column_config["Monthly Payment"] = st.column_config.NumberColumn(
            help="The monthly payment of each debt",
            format="$%d",
            default=0,
            required=True,
            width="medium",
        )

    return st.data_editor(
        pd.DataFrame(data=[data], columns=columns),
        column_config=column_config,
        num_rows="dynamic",
    )
