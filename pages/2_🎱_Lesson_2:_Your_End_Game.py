import streamlit as st

from helper.page_setup import setup_page


setup_page()

st.markdown("# Your End Game")

st.write("\"_If you don’t know where you are going, every road will get you nowhere._\" — Henry Kissinger")

st.markdown("## Dream-Driven Financial Planning")
st.write("""
    Antoine de Saint-Exupéry, writer, pioneering aviator, and author of _The Little Prince_, once said: “If you want to
    build a ship, don’t drum up the men to gather wood, divide the work, and give orders. Instead, teach them to yearn for
    the vast and endless sea.” If he was a financial advisor today, he might say something like: “If you want to become
    wealthy and financially independent, don’t focus on budgeting, giving employers your best days, or relying only on
    others for financial growth. Instead, teach them to yearn for their best life.”

    In the last section, we started with a 5,000-ft approach where we compared our financial situations to those of the
    national average. While it's useful to know where we stand, if all we do is compare ourselves to "some sort of average"
    we're going to end up with "some sort of average" results, which are likely not what we're after.

    According to Earl Nightingale, a mid-1900s author, "Success is the progressive realization of a worthy ideal."
    According to this definition, what makes someone successful?
    1. a worthy ideal (goal)
    2. and the progressive realization of that goal (effort)

    This can't be overstated: when defining a successful life, **you are the one who gets to define what this
    worthy ideal is**; others don't get to do this for you. Do you want to become the best dad or mom you can be?
    Do you want to experience more of the world
    through travel? Do you want to be the best plumber in the world? Do you want to become a monk, an author, or a
    professional gamer? To be successful, we must first have an idea of what we want.

    To look at this same idea through the lens of physics, in _The Great Mental Models, Vol. 2_, a book of principles
    that explains how the world works at a fundamental level, the principle Velocity emerges: a measurement of both speed
    and direction. They write: "To get to a goal, we cannot just focus on being fast, but need to be aware of the
    direction we want to go" (p. 123).

    Wealth, on its own, is useless; it only has value when it is applied towards a purpose. It is like a Swiss-army
    knife that, when used appropriately, can do a lot to help us increase our happiness and decrease our unhappiness
    as we use it to "progressively realize our goal".

    Another way of looking at it is: money is a "personality multiplier". Whoever you are, money will make you more of
    that. If you're generous, you will become more generous. If you are a worrier, you will worry more. If you are a
    happy, chances are you will become even happier.

    Because of this, money does not and cannot replace the hard work of finding your purpose, the reason for waking up
    in the morning. But it can help you get there.
""")

# TODO (optional): Do we want to include this section?
# with st.expander("A Digression: Money and Happiness"):
#     st.write("""
#         If you've ever head that money doesn't make you happier, I would encourage you to read this
#         [article "Does more money correlate with greater happiness?"](https://penntoday.upenn.edu/news/does-more-money-correlate-greater-happiness-Penn-Princeton-research)
#         that "suggests that for most people larger incomes are associated with greater happiness".

#         Earlier, I described money like a Swiss-army knife because, the way that I see it, money enables people to do
#         things they want to do, to have greater agency and freedom. My favorite description for money is "personality
#         multiplier", and it goes like this: money will make you more of what you already are. If you're generous,
#         you will become more generous. If you are a worrier, you will worry more. If you are a happy person, chances
#         are you will become even happier.

#         So earning money does not and cannot replace the hard work of finding your why, your purpose; however, if you
#         know how to use it as a tool, it can help you in that journey.
#     """)

st.divider()

st.write("""
    If money wasn't an issue, what would you do with your life? What would you do with your time? What would your
    relationships look like?

    Before we get into financial strategies, it's helpful to anchor ourselves in a clear vision of what we
    want out of this life. The journey to financial independence is a long one, and it's much easier to stay on track
    when we know why we're doing it.

    Take a few minutes to think about your life as it currently is. What activities or relationships bring you the most
    joy? What are some things you'd like to learn or experience? Record these below or in a journal and use them as a
    guide as we move forward. These can change over time; as life changes, we may grow excited about new things or
    realize that we don't value the things we once did, so don't worry about getting it perfect.
""")

key = "your_goal_text_area"
if key not in st.session_state:
    st.session_state[key] = ""
st.session_state[key] = st.text_area(
    "If money wasn't an issue, what would your life look like?", value=st.session_state[key]
)

with st.container(border=True):
    col1, col2 = st.columns([3,1]) # Cheat to get the page links to be on the right side
    col1.page_link("pages/1_🐣_Lesson_1:_Where_Are_You_Now.py" , label="Lesson 1: Where Are You Now?", icon="⬅️")
    col2.page_link("pages/3_💸_Lesson_3:_Sponsoring_Your_Dream.py" , label="Lesson 3: Sponsoring Your Dream", icon="➡️")

### TODO (optional): Do we want to include this section?
# st.write("""
#     If you take the time to plot out your life in weeks, it's sobering to see everything fit into a single page. The
#     blog [Wait But Why](https://waitbutwhy.com/2014/05/life-weeks.html) provides a series of visualization that
#     illustrate this (as well as a few famous folks like Tiger Woods and Albert Einstein).

#     In order to make this life count, we have to do the hard work of
# """)

