import pandas as pd
import streamlit as st


def tool_income_assessment():
    st.markdown("# Income Assessment")

    st.write("""
        In the last section, we did a deep-dive into our expenses in order to proactively _choose_ how we
        spend our money, instead of letting the moment in time choose for us. Using the monthly expenses,
        let's try and find a way to save _at least_ 10% of our income. Why 10%? It's a good starting point
        that allows us to save for the future while still having a large enough portion of our income to
        enjoy the present.

    """)

    # TODO: Grab this number from the expenses section via cache
    monthly_expenses = st.number_input("Monthly Expenses", value=0, step=10)

    if monthly_expenses > 0:
        target_monthly_income = int(monthly_expenses / 0.90)
        target_annual_income = int(target_monthly_income * 12)
        target_savings_amount = int(target_monthly_income - monthly_expenses)
        st.write(f"""
            To save 10% of your income, you would need to earn at least **\${target_annual_income:,}**/year
            or **\${target_monthly_income:,}**/month after taxes.
            This would allow you to save **\${target_savings_amount * 12:,}**/year, or
            **\${target_savings_amount:,}**/month.
        """)

        actual_annual_income = st.number_input("Annual Income After Taxes", value=0, step=10)

        if actual_annual_income > 0:
            actual_monthly_income = int(actual_annual_income / 12)
            actual_savings_rate = (actual_monthly_income - monthly_expenses) / actual_monthly_income
            actual_savings_amount = int(actual_monthly_income - monthly_expenses)
            st.write(f"""
                With your current after-tax income, you are saving **{actual_savings_rate:.2%}** of your income,
                which is the equivalent of **\${(actual_savings_amount * 12):,}**/year or
                **\${actual_savings_amount:,}**/month.
            """)

            if actual_savings_rate < 0.10:
                st.warning("""
                    You are currently saving less than 10% of your income. To reach this goal, you could:
                    - Find ways to increase your income (e.g. side-hustles, promotions, etc.)
                    - Find ways to decrease your expenses
                    - Both
                """)
            else:
                st.success("""
                    Congratulations! You are currently saving more than 10% of your income. If you're still
                    interested in increasing your savings rate, you could:
                    - Find ways to increase your income (e.g. side-hustles, promotions, etc.)
                    - Find ways to decrease your expenses
                    - Both
                """)
            st.write("""
                In conclusion, savings rates percentages are a great way to provide general recommendations for
                savings targets. Additionally, they can be a helpful way to measure the degree of consumption
                for your particular lifestyle relative to your income. However, the real goal in your financial
                journey is determining your specific financial goals and then working backwards to find the monthly
                dollar savings amount required to get there in your target time frame.
            """)

