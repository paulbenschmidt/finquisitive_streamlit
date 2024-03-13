import pandas as pd
import streamlit as st

from helper.page_setup import setup_page
from tools.financial_position_comparison import tool_financial_position_comparison

setup_page()

st.markdown("# Where Are You Now?")

st.write("""
    Before beginning our financial journey, it's helpful to first understand where we are now. This will help us
    understand how our current situation tracks with the averages, because if we want average results (and that's
    ok if we do), we need to make sure that we're _at least_ following average behaviors. However, if we want
    better than average results (and that's probably going to be most of us), we need to find ways
    to beat these averages.
""")

st.divider()

tool_financial_position_comparison()

st.markdown("## U.S. National Statistics")
st.write("""
    ##### Income

    [USA Today](https://www.usatoday.com/money/blueprint/business/hr-payroll/average-salary-us/) highlights that
    the average annual household income in the United States in 2023 was \$59,384, with salaries ranging
    widely across states (from \$48,048 Mississippi to \$86,840 in Massachusetts) and age groups (with earnings
    peaking between the ages of 35 and 44).

    ##### Spending

    According to the [Motley Fool financial service](https://www.fool.com/the-ascent/research/average-monthly-expenses/),
    United States consumers in 2024 are spending \$6,081 on average monthly household spending across the following
    categories:
    - **Housing**: \$2,025, which includes rent or mortgage, utilities, and household operations
    - **Transportation**: \$1,025
    - **Food**: \$779, with \$475 on groceries and \$303 on eating out
    - **Personal** insurance and pensions: \$729
    - **Healthcare**: \$488
    - **Entertainment**: \$288
    - **Apparel** and services: \$162

    ##### Net Worth
    [Kiplinger Personal Finance](https://www.kiplinger.com/personal-finance/how-average-is-your-net-worth) reports
    that the median average net worth of Americans steadily grows, as we would expect, starting around \$10,800
    for 20-24 year olds and peaking at \$433,100 for 70-74 year olds).

    ##### Conclusion
    With a basic familiarity of the national averages, let's dive into what makes your financial situation unique!
    In the next section, we'll approach finance from a different angle by focusing on the end game: what do you want
    out of life?

    Wealth is one of many tools that can help you get there!
""")

with st.container(border=True):
    col1, col2 = st.columns([3,1]) # Cheat to get the page links to be on the right side
    col1.page_link("Home.py" , label="Back to Home", icon="⬅️")
    col2.page_link("pages/2_🎱_Lesson_2:_Your_End_Game.py" , label="Lesson 2: Your End Game", icon="➡️")
