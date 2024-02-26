import datetime as dt

import streamlit as st

from helper.page_setup import setup_page

CURRENT_YEAR = dt.datetime.now().year

setup_page()

st.write(f"""
    # Putting It Together

    _"Most of our failures are in races for which others enter us. Most of our successes come from
    races we ourselves want to enter. We fail to win most races because we enter too many of the
    wrong ones: their races, not ours."_ Richard Koch in _The 80-20 Principle_

    ## What Is Your Race?

    As we wrap up, it's essential to remember our personal end goal: why are we on this journey?
    Is it to provide greater opportunity for our future family? Is it to explore life to the
    fullest by financially supporting our ambitions? Is it to start a business, volunteer, or
    spend more time on a hobby? This is your decision and is the north star that guides you in your
    financial choices.

    > "But while we can see how much money other people spend on cars, homes, clothes, and vacations,
    > we don't get to see their goals, worries, and aspirations. A young lawyer aiming to be a partner
    > at a prestigious law firm might need to maintain an appearance that I, a writer who can work in
    > sweatpants, have no need for. But when his purchases set my own expectations, I'm wandering down
    > a path of potential disappointment because I'm spending the money without the career boost he's
    > getting. We might not even have different styles. We're just playing a different game.
    > It took me years to figure this out.... few things matter more with money than understanding
    > your own time horizon and not being persuaded by the actions and behaviors of people playing
    > different games than you are. (Morgan Housel, _The Psychology of Money_)

    Earlier, we talked about growth and the length of our journey in years that it would take
    to reach our financial goal. For some of us, it may only be a few years; for others, it
    may be a few decades. Wherever you are in that journey, remember to have grace. In
    _The Psychology of Money_, Morgan Housel writes, "It should surprise no one that many
    of us are bad at saving and investing for retirement. We're not crazy. We're all just newbies."
    The 401(k) was created {CURRENT_YEAR - 1978} years ago; the Roth IRA was created
    {CURRENT_YEAR - 1998} years ago. We haven't had very much practice!

    Whether it's spending too much in a month or making a bad investment that results in
    losses, know that as long as you continue learning and growing, you _will_ come out
    ahead with a long enough time horizon.

    In closing, remember that the life you live in pursuit of a goal is still your life, so
    make your goal _and_ the journey it takes to get there worthwhile! As you pursue your goal,
    you'll...
    - learn more about yourself, others, and the world
    - grow in your skills and abilities
    - change in your values and beliefs

    Think about the life you want and the person you want to be, and begin building
    and working toward this today. Take what you've learned about savings rates, understanding
    debts, the see-saw of risk and return, and the power of time. Wealth is one tool of many
    to make your life the way you want it to be.

    Thanks for letting us be a small part of your life; we hope to see you around FinQuisitive!
""")
