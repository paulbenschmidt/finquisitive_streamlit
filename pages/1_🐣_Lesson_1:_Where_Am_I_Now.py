import pandas as pd
import streamlit as st

from helper.page_setup import setup_page
from tools.financial_position_comparison import tool_financial_position_comparison


setup_page()

st.markdown("# Where Am I Now?")

st.markdown("## Financial Advisors Solve All Your Problems, Right?")
st.write(
    """When I met with my first financial advisor, I came in thinking that I would be wealthy just because I was doing what other people my age weren't doing: talking to financial advisors in college. The conversation went well, but I didn't end up learning much: we talked about saving and index funds. She signed me up for a few brokerage accounts, complimented me on my progress, and encouraged me to keep doing what I was doing.

Years later, I realized that what I really wanted out of that meeting was to know, deep down, in my bones, that I was going to be ok, that the things I was doing were going to be enough to feel safe.

Above all else, my hope is that through this seminar we can start planting that seed of contentment and peace, growing into this idea that our principles and strategies, if followed consistently over time, will get us to where we want to go.

So, to begin, we're going to start with a fun numbers game. Before we get into the nitty-gritties of financial principles and fundamental strategies, it's helpful to know where we are now. It's helpful to see how our current situation tracks with the averages, because if we want average results (and that's ok if we do), we need to make sure that we're _at least_ following average behaviors. However, if we want better than average results (and I'm sure that's going to be most, if not all, of us), we need to find ways to beat the average milestones and metrics.

Without further ado, let's dig into some basic metrics on US expenses, income, assets/liabilities, and savings rates. As we do this, I want you to think about your current financial situation and the ways that you have similarities or differences."""
)

st.divider()

st.markdown("## U.S. National Statistics")
st.write(
    """According to the [Motley Fool financial service](https://www.fool.com/the-ascent/research/average-monthly-expenses/), United States consumers in 2024 are spending \$6,081 on average monthly household spending, which is up \$1.8k since a decade ago and up $503 since 2021. This is largely due to inflation and not because of any actual spending changes.
- According to the [U.S. BUREAU OF LABOR STATISTICS](https://www.bls.gov/news.release/cesan.nr0.htm#:~:text=The%20average%20annual%20expenditures%20for,and%20healthcare%20(8.0%20percent).), "housing accounted for the largest share (33.3 percent), followed by transportation (16.8 percent), food (12.8 percent), personal insurance and pensions (12.0 percent), and healthcare (8.0 percent)."
- Housing is the largest average cost at $2,025 per month, making up 33% of typical spending.
- Americans spend $779 on food per month, with almost two-thirds being spent on groceries ($475) and the rest on eating out ($303).
- Transportation costs more than many realize ($1,025 per month), largely due to the intermittent nature of those expenses.

United States residents average annual household income after taxes is $83,195 and $94,003 before taxes, per the BLS. In a moment, we're going to drill down a little further by age, since this varies considerably across age groups.

Based on those figures, Americans spend 88% of their after-tax income and have a savings rate of 12%. That's somewhat off the recommended savings rate of 20% and a 3% decline from 2021."""
)

st.divider()

tool_financial_position_comparison()
