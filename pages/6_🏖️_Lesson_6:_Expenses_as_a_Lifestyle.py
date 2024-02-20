import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

from helper.page_setup import setup_page
from tools.spending_assessment import tool_spending_assessment


setup_page()

st.write("""
    # Expenses as a Lifestyle

    "_If you operate so that you can manage your downside, the upside will take care of itself._" — David Osborn in
    _Wealth Can't Wait_, pg 167)

    ## Learning to Spend Well

    In the four quadrants, expenses are where we have the most immediate control; it is the lowest hanging fruit to
    make immediate action in achieving your goals and the best place to begin. Your expenses, combined with your
    income, define your savings rate, and your savings rate determines how quickly you'll reach your goal.

    In _The Psychology of Money_, Morgan Housel writes: "one of the most powerful ways to increase your savings isn't
    to raise your income. It's to raise your humility." We may have the most control over our expenses, but coming
    face-to-face with our spending habits and patterns is not easy. This is especially true when we live in a
    culture of consumerism, drowning in advertisements that constantly broadcasts that "we don't have enough" or
    that "this new product will change your life".

    But every dollar that we spend on an expense is a dollar that isn't invested, and any dollar that isn't invested
    won't grow over time. In _The Richest Man in Babylon_, a fictional book full of financial parables, the author
    talks about thinking about money as employees who work for you if you let them, investing in ourselves by
    strategically putting our money in places it will grow for us.

    > _Then he looked at me shrewdly from under his shaggy brows and said in a low, forceful tone, "I found the road
    > to wealth when I decided that a part of all I earned was mine to keep. And so will you."... "But all I earn
    > is mine to keep, is it not?" I demanded. "Far from it," he replied. "Do you not pay the garment-maker? Do
    > you not pay the sandal-maker? Do you not pay for the things you eat? Can you live in Babylon without
    > spending?...You pay to everyone but yourself."_ From _The Richest Man in Babylon_

    So how do we bridge the gap between living an enjoyable life today while also saving enough on the side to have
    an even better future tomorrow? I find it helpful to think about expenses as a way to create our personal
    "good enough" life, that is proactively defined by _our_ standards, not by the standards of _advertisers_ and
    _marketers_ who are after more of our paycheck.

    Practically, this looks like going through your expenses and asking yourself questions like:
    - Would I be happy without this?
    - Would I be happier if I had more of this? How much happier?
    - Am I happy with the amount of spending on this item or category?

    It will take some work, but after a while, you can begin to see every purchase through this lens of "satisfizing",
    getting the most joy out of your dollars spent while still being on track to reach future goals. At the beginning
    of his career, Sir John Marks Templeton, a legendary investor, banker, fund manager, and philanthropist,
    made it a game to see how well he and his wife could live while only using *50% of their income*.
    You can be sure that they were scrutinizing every purchase to see if it was actually needed or if it would
    truly bring them joy!

    If the approach of analyzing every purchase seems too tedious, you could also work backwards by using your
    financial goal as your guide. By first determining your financial goal (amount and target date), and then
    determining how much you would need to save in order to reach that amount, you can
    calculate the amount that you would need to save each month in order to reach your target on time. This can
    be especially helpful if you're frugal and have a hard time spending money, because you begin by defining your
    goal (without regard to spending) and then work backwards to determine how much you can spend. This approach
    provides you with mathematical permission to spend the rest with the peace of mind that you're still on track
    to reach your goal.

    Wealth building is a process; it is an endurance race, not a sprint. Because of this, be wary of the
    temptation to force yourself to live more frugally than you're currently able to. By putting too restrictive
    of a budget, you may end up resorting to spending splurges. Your goal here is to find a sustainable growth
    rate for a life that you can enjoy today, and in the future!
""")

tool_spending_assessment()
