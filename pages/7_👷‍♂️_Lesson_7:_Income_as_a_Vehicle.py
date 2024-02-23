import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

from helper.page_setup import setup_page
from tools.income_assessment import tool_income_assessment

setup_page()

st.write("""
    # Income as a Vehicle

    *"Our success is not the result of making money. Making money is the result of success and success is in direct
    proportion to our service. Most people have this law backwards. They believe that you're successful if you
    earn a lot of money. The truth is that you can only earn money after you're successful. It's like the story
    of the man who sat in front of the stove and said to it, 'Give me heat and then I'll add the wood.'"* — Earl
    Nightingale, *The Strangest Secret in the World*

    ## The Enabler of Financial Independence

    The next quadrant is income and completes the calculation of savings rate, helping us to determine how much
    we're able to save and invest. While our degree of control over our expenses is much greater, we still
    have control over our income, especially as we think many years into the future.

    ## A Posture of Gratefulness

    Whether you're self-employed, working for others, or own your own business, sometimes mustering the
    strength to show up to your job day after day can be challenging. However, if we're serious about our
    financial goals, we can take a posture of gratefulness for the work that enables us to work toward
    eventual freedom.

    > _When no buyers were near, he talked to me earnestly to impress upon me how valuable work would be
    > to me in the future: "Some men hate it. They make it their enemy. Better to treat it like a friend,
    > make thyself like it. Don't mind because it is hard. If thou thinkest about what a good house thou
    > build, then who cares if the beams are heavy and it is far from the well to carry the water for
    > the plaster. Promise me, boy, if thou get a master, work for him as hard as thou canst. If he does
    > not appreciate all thou do, never mind. Remember, work, well-done, does good to the man who does it.
    > It makes him a better man."_ (_The Richest Man in Babylon_, Clason)

    ## Choosing a Career

    As was covered in Lesson 4, the time in the middle between the start of the financial independence
    journey and your eventual achievement of the goal, is where the majority of your time will be spent.
    Because of this, it's worthwhile to think about what you want your life in this "middle place" to look like -
    especially, in the work that you do. Or, to share some wisdom from a friend who decided not to go back to
    school for another 10 years, "The life you spend working toward a goal is still your life."

    The blogger Marc Winn provides a helpful framework for ensuring that the income we earn is both
    sustainable and lucrative. Using a Venn diagram to explain the concept of _ikigai_, a Japanese
    word that roughly translates to "the reason you wake up in the morning", Winn talks about work in
    terms of identifying the intersection of (1) what you love, (2) what you are good at, (3) what the
    world needs, and (4) what can be paid for.

    If you have the flexibility to experiment with different careers that can nestle you into the
    intersection of these four areas, it may be worth exploring and experimenting with different paths that
    target the intersection of these four areas. However, for those who may not have
    the flexibility, finding a [good enough job](https://www.amazon.com/Good-Enough-Job-Reclaiming-Life/dp/059353896X)
    may be sufficient for your needs and goals. In an American culture where our job is coupled so closely
    to our identity, it may feel challenging to "settle" for a good enough job, but, if this choice aligns
    with your goals, then this is a choice worth celebrating!

    ## Augmenting Income by Being More Useful

    Earl Nightingale, a famous author and radio speaker from the 1900s, said: "If he wants more he
    must be of more service to those whom he receives his return. If he wants less he has only to
    reduce his service. This is the price you must pay for what you want" (_The Strangest Secret in the World_).
    While it is beyond the scope of this course to identify all the different ways that one could
    increase one's income, it's helpful to start with this principle: if you aim to be useful,
    you will eventually be rewarded. Modern author and thinker Cal Newport echoes this idea in writing:
    "By aiming to make money, you're aiming to be valuable.” (_So Good They Can't Ignore You_)

    However, just as it is necessary to determine the expenses and style of living that we can
    reasonably sustain, we should also consider our work-life so as to increase our chances of
    being able to stick with the work and, as a result, meet our financial goals by our time targets.
    For example, taking a job that requires 80 hours a week may pay well, but you may not want to
    continue that pace for more than a year or two. On the other hand, a job that pays less but
    has fewer hours or more flexibility may be a better fit if you're able to sustain it for a longer period.
    The same can be said for side-hustles and other forms of income: if it isn't sustainable, it
    may not serve you well in the long run. Therefore, for careers and earning income,
    it is essential to consider the quality of life during the life lived working towards our goal.

    ## Transmuting Income to Assets

    Before ending this lesson, it's important to remember:
    "Your level of income doesn't determine your level of wealth. If you're not building wealth, then you're
    depleting" (_Wealth Can't Wait_, Osborn). Income can be applied toward increasing expenses (buying that new car
    or upgrading your house) or increasing assets (purchasing stocks or real estate). One gives immediate
    gratification, while the other gives long-term security. If our goal is to achieve financial independence,
    prioritizing moving income into the assets quadrant should always be at the front of our mind. Making
    six-figures means very little if you don't know how to keep it and put it to work; instead,
    your measure of success should be your savings rate: how much you're able to keep and invest. It is
    this second number that will let you increase income effortlessly.
""")

tool_income_assessment()
