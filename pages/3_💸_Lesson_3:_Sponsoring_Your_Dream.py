import pandas as pd
import streamlit as st

from helper.page_setup import setup_page
from tools.financial_independence_levels import tool_financial_independence_levels


setup_page()

st.markdown("# Sponsoring Your Dream")

st.markdown("## The 4% Rule")
st.write("""
    Bill Bengen, a financial adviser in Southern California, created a helpful guideline commonly referenced by
    young and old retirees; this rule of thumb is called the 4% Rule.

    This is a "practical rule of thumb that may be used by retirees to decide how much they should withdraw from
    their retirement funds each year" to "serve as a steady income stream while maintaining an adequate overall
    account balance for future years" (_[What Is the 4% Rule for Withdrawals in Retirement and How Much Can You Spend?](https://www.investopedia.com/terms/f/four-percent-rule.asp)_).
    Using stock and bond returns over a 50-year period from 1926 to 1976, with a heavy focus on the severe market
    downturns of the Great Depression and early 1970s, Bengen determined that using this principle, retirement
    funds always lasted at least 30 years, still accounting for inflation, if we assumed that the retiree was living
    off of 4% of those retirement funds. By limiting withdrawals to the conservative 4%, funds were primarily taken
    from the interest and dividends of those savings, meaning that the savings had a stronger chance of lasting even
    longer.

    Putting this 4% Rule to use, let's determine the size of retirement fund that it would take to support a few
    variations of our current lifestyle. To do this, we'll take our monthly expenses amount from the last section,
    multiply it by 12 to annualize it, then divide it by 4% to get to our Financial Freedom number.
""")

st.markdown("## The Levels of Independence")
st.write("""
    According to Tony Robbins in _[MONEY Master the Game](https://www.amazon.com/MONEY-Master-Game-Financial-Freedom/dp/1476757860)_,
    more than _half_ of Americans haven't even tried to calculate the level of wealth they would need in order to
    retire. Why do you think it is? Is it that the thought of the number being too big is scary enough for us to
    instead ignore and pretend it doesn't exist? As Robbins says, "You can't manage your health if you can't measure
    it. And the same goes for your finances."

    With our 4% Rule and a long enough time horizon, I hope this exercise will be of an encouragement to you and
    help you begin to put your investing plans into action.

    In _[MONEY Master the Game](https://www.amazon.com/MONEY-Master-Game-Financial-Freedom/dp/1476757860)_, there
    are 5 levels of financial freedom:
    1. **Financial Security.** All basic needs are covered: rent, food, utilities, transportation, and healthcare.
    2. **Financial Vitality.** All basic needs are covered, with half of daily desires covered as well.
    3. **Financial Independence.** All your basic needs and daily desires are covered. You may now stop working.
    4. **Financial Freedom.** Everything from above, plus a luxury or three and regular donations!
         (boat/condo/annual trips/etc.)
    5. **Absolute Financial Freedom.** Everything from above, plus more high-end luxuries! (private island/jet/etc.)

    The empowering concept here is the progression of levels, the realization of our goals over time. Being financially
    free isn't just about hitting a "magic number"; there are layers depending on what we're after.
    We can win at different stages.

    As we'll see in the exercise below, our targets may be a lot closer than we think. And once we
    reach that, we can let our momentum carry us to the next level until we've reached a level of our personal
    contentment.


""")

tool_financial_independence_levels()

st.write("""
    Armed with this knowledge, you now have an approximation of the amount required to retired, tailored specifically
    to your lifestyle. Before moving on to the next section, choose one or two of the levels above and keep this
    in the back of your mind as we move forward. We'll be coming back to this in the future!
""")
