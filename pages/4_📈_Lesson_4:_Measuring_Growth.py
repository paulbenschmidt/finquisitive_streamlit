import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

from helper.page_setup import setup_page
from helper.visuals import plot_two_net_worth_points
from tools.financial_growth_calculations import tool_financial_growth_calculations


setup_page()

st.markdown("# Measuring Growth")

st.write("""
    In the past few lectures, we've explored our current position as well as a few of our desired future goals.
    What we haven't spent a lot of time talking about is the gap between these two points; this is the focus of this
    lesson and will be the focus for the remainder of the course, because this is, for most of us, where we'll be
    living for the next 5 to 35 years.

    If you are 20 years old and your goal is to reach Financial Independence by age 50, we would get something like
    this when plotting on an XY axis:
""")

plot_two_net_worth_points(data = [[20, 5000], [50, 1000000]])

st.write("""
    In mathematics, the slope or gradient of a line is a number that describes both the direction and the steepness
    of the line. By plotting a few variations of the graph we can see how the slope changes across each one:
""")

st.write(f"""
    - if you're 20 with a lower net worth of \$5,000 and want to retire in 30 years, the slope is very gradual
""")
plot_two_net_worth_points(data = [[20, 5000], [50, 1000000]])

st.write("""
    - if you're 40 with a high net worth of \$668,333 and want to retire in 10 years, the slope is equally gradual
""")
plot_two_net_worth_points(data = [[40, 668333], [50, 1000000]])

st.write("""
    - if you're 20 with a net worth of \$5,000 and want to retire in 10 years, the slope is aggressive
""")
plot_two_net_worth_points(data = [[20, 5000], [30, 1000000]])

st.write("""
    - if you're 40 with a low net worth of $5,000 and want to retire in 10 years, the slope is equally aggressive
""")
plot_two_net_worth_points(data = [[40, 5000], [50, 1000000]])

st.write("## Sustainability")
st.write("""
    The space between the two dots is _where our lives are lived_. Since this is a large portion of our lives, it is
    essential to make sure that our current lifestyle supports our financial timeline. Therefore, for those interested
    in decreasing the duration of time between the two points (i.e. retiring earlier than the average person), it is
    essential to identify the slope that is sustainable for our case.

    This last situation - of being older with a lower net worth - is what we want to avoid: a short timeline with
    little margin for error (because we aren't getting any younger). The more aggressive the slope is,
    the more difficult it is to achieve. In terms of increasing net worth,
    there are only two major levers to play with: saving more or getting a higher return on investment. And we have a
    little more control over the former than the latter.

    To expand on the two major levers, let's revisit our initial net worth sheet:
""")


tool_financial_growth_calculations()
