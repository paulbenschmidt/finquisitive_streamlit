import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

from helper.page_setup import setup_page
from tools.financial_statements import tool_financial_statements


setup_page()

st.markdown("# You Are a Business")
st.write("""
    In the international best-seller _The War of Art_, author Steven Pressfield helps readers win the inner creative
    battle. When talking about the leap of faith that people make from living the comfortable W-2 employer-employee
    life to the new and uncertain self-employed life, he recommends thinking about ourselves as if we were a business.

    > _Even for a business of one, have a beginning-of-week status meeting that serves to highlight the most important
    > business tasks for the week, type them up on business stationary and distribute them to the different "team
    > members" of the business. If we think of ourselves as a corporation, it gives us a healthy distance from the
    > business._

    So also with personal finance: if we think of ourselves as a business, it gives us a healthy distance from our
    finances. When we map things out on spreadsheets and run our personal financial projections, we quickly get a
    glimpse of whether or not our we're on the track we want to be.

    According to a bank, the viability of a business is determined by three key financial statements:
    1. a balance sheet
    2. a profit and loss statement
    3. historical cash flow

    These three statements give the bank a high-level overview on the financial health of your business, so why not
    use these same statements to determine the financial health of your household? The famous real estate
    investor and author of _The Millionaire Real Estate Investor_ Gary Keller agrees that it would be very beneficial
    for every home (loc 2036).

    In the last lesson, we spent time identifying the rate of financial growth that would be required to reach point B
    (financial goal) from point A (current day). Now we'll look at the same idea with a little more detail, using our
    financial statements instead.
""")

tool_financial_statements()

st.write("""
    Over the next few lessons, we'll dive into each of the four quadrants: expenses, income, liabilities, and
    assets. We'll start with expenses, the area where we have the most control and can have the most immediate
    impact on our financial health.
""")
