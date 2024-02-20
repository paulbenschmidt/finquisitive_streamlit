import pandas as pd
import streamlit as st


FOUR_PERCENT_RULE = 0.04

def tool_financial_independence_levels():
    st.markdown("# Financial Independence Levels Calculator")

    with st.expander("Basic Needs (Monthly)"):
        basic_needs = st.data_editor(
            pd.DataFrame(
                columns=["Name", "Amount"],
                data=[["Housing & Utilities", 0], ["Food", 0], ["Transportation", 0], ["Healthcare", 0], ["Insurance", 0], ["Other", 0]]
            ),
            column_config={
                "Name": st.column_config.Column(
                    label="Name",
                    width="large",
                    disabled=True,
                ),
                "Amount": st.column_config.NumberColumn(
                    format="$%d",
                    default=0,
                    required=True,
                    width="medium",
                )
            },
            num_rows="static",
            hide_index=True,
        )

    with st.expander("Additional Wants (Monthly)"):
        additional_wants = st.data_editor(
            pd.DataFrame(
                columns=["Name", "Amount"],
                data=[["Clothing", 0], ["Restaurants", 0], ["Entertainment", 0], ["Travel", 0], ["Gifts", 0]]
            ),
            column_config={
                "Name": st.column_config.TextColumn(
                    label="Name",
                    width="large",
                ),
                "Amount": st.column_config.NumberColumn(
                    format="$%d",
                    default=0,
                    required=True,
                    width="medium",
                )
            },
            num_rows="dynamic",
        )

    with st.expander(f"Entry Luxuries"):
        st.write("""
            These are luxuries that you would personally want to have in your life, but are a little bit more
            extravagant in nature. These could be things like a boat, a condo, or an annual trip to your favorite
            destination. Additionally, this could be a monthly donation to a cause that you're passionate about.

            In order to calculate the affordability of these luxuries, we'll use the **monthly payment** of the item.
            For example, if you wanted to buy a boat that costs \$50,000, with nothing down for the down payment,
            you would finance the \$50,000 over 5 years at a 5% interest rate and would result in a monthly payment
            of \$943.56.

            For help calculating the monthly payments for your specific luxuries, see the expander _Helper:
            Luxury Loan Payment Calculator_ below.
        """)
        entry_luxuries = st.data_editor(
            pd.DataFrame(
                columns=["Name", "Amount"],
                data=[["Luxury Item #1 (name me)", 0], ["Luxury Item #2 (name me)", 0], ["Monthly Donation", 0]]
            ),
            key="entry_luxuries",
            column_config={
                "Name": st.column_config.TextColumn(
                    label="Name",
                    width="large",
                ),
                "Amount": st.column_config.NumberColumn(
                    format="$%d",
                    default=0,
                    required=True,
                    width="medium",
                )
            },
            num_rows="dynamic",
        )

    with st.expander("High-End Luxuries"):
        st.write("""
            Dream Big! These are luxuries that might seem a little excessive, like a private island or a private jet.
            As we'll soon see, when viewed in bite-size monthly payments, these luxuries may be more attainable than
            we think.

            For help calculating the monthly payments for your specific luxuries, see the expander _Helper:
            Luxury Loan Payment Calculator_ below.
        """)
        high_end_luxuries = st.data_editor(
            pd.DataFrame(
                columns=["Name", "Amount"],
                data=[["", 0]]
            ),
            key="high_end_luxuries",
            column_config={
                "Name": st.column_config.TextColumn(
                    label="Name",
                    width="large",
                ),
                "Amount": st.column_config.NumberColumn(
                    format="$%d",
                    default=0,
                    required=True,
                    width="medium",
                )
            },
            num_rows="dynamic",
        )

    with st.expander("Helper: Luxury Loan Payment Calculator"):
        st.write("""

        """)
        calculator_loan_amount = st.number_input(label="Loan Amount", value=50000, step=1)
        calculator_interest_rate = st.number_input(label="Interest APR (Annual Percentage Rate)", value=0.05, step=0.001)
        calculator_term_in_years = st.number_input(label="Term (Years)", value=5, step=1)
        calculator_term_in_months = calculator_term_in_years * 12
        amortized_loan_payment = calculate_amortization_amount(
            principal = calculator_loan_amount,
            apr = calculator_interest_rate,
            periods = calculator_term_in_months
        )
        st.write(f"The monthly payment for this item would be : **${round(amortized_loan_payment, 2):,}**")

    with st.container(border=True):
            st.markdown("## Levels of Financial Independence")
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                security_sum = basic_needs["Amount"].sum()
                display_financial_level_metric(
                    label = "Financial Security",
                    metric_sum = security_sum
                )
                st.write("All basic needs are covered!")
            with col2:
                vitality_sum = security_sum + (additional_wants["Amount"].sum() / 2)
                display_financial_level_metric(
                    label = "Financial Vitality",
                    metric_sum = vitality_sum
                )
                st.write("All basic needs and half of daily desires are covered!")
            with col3:
                independence_sum = security_sum + additional_wants["Amount"].sum()
                display_financial_level_metric(
                    label = "Financial Independence",
                    metric_sum = independence_sum
                )
                st.write("All basic needs and daily desires are covered!")
            ### TODO: Fix the calculation for the two luxuries!
            with col4:
                freedom_sum = independence_sum + entry_luxuries["Amount"].sum()
                display_financial_level_metric(
                    label = "Financial Freedom",
                    metric_sum = freedom_sum
                )
                st.write("All basic needs and daily desires are covered, plus a few luxuries!")
            with col5:
                absolute_freedom_sum = freedom_sum + high_end_luxuries["Amount"].sum()
                display_financial_level_metric(
                    label = "Absolute Financial Freedom",
                    metric_sum = absolute_freedom_sum
                )
                st.write("All basic needs and daily desires are covered, plus more high-end luxuries!")

            st.write("""
                By first calculating our monthly expenses for each level, we determine the amount of _passive
                income_ required to satisfy that level of financial independence. Inverting the 4% Rule (i.e. dividing
                our monthly expenses by 4%) gives us the amount of money that we would need to have invested in order
                to comfortably "retire" at that specific level.
            """)

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

def display_financial_level_metric(label, metric_sum):
    st.metric(
        label=label,
        value=f"${int(metric_sum * 12 / FOUR_PERCENT_RULE):,}",
        delta=f"${int(metric_sum):,} / mo.",
    )

def calculate_amortization_amount(principal, apr, periods):
    # https://www.rocketloans.com/learn/financial-smarts/how-to-calculate-monthly-payment-on-a-loan
    monthly_rate = apr / 12
    dividend = monthly_rate * ((1 + monthly_rate) ** periods) # (r (1+r)n)
    divisor = ((1 + monthly_rate) ** periods) - 1 # ((1+r)n−1)
    return principal * (dividend / divisor)
