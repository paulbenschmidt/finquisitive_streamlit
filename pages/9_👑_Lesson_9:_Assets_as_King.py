import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

from helper.page_setup import setup_page


setup_page()

st.write("""
    # Assets as King

    _Being rich is about having money. You can have a job and be very rich. The
    problem with this is that the money stops coming to you when you stop working
    for it. Financial wealth, by contrast, is about owning assets, such as businesses
    or real estate, that generate money for you._ - Gary Keller, _The Millionaire Real Estate Investor_

    ## Wealthy Money
    The final quadrant of assets is the cornerstone of building wealth. This is where all the
    money we've saved gets put to work by investment. In _The Millionaire Real Estate Investor_, Gary Keller
    talks about the four different categories of money:
    1. **Dead** money earns interest below the inflation rate
    2. **Safe** money earns interest at the inflation rate
    3. **Healthy** money earns interest well above the inflation rate
    4. **Wealthy** money earns interest well above that of healthy money

    In the last 20 years,
    [inflation rates in the United States](https://www.usinflationcalculator.com/inflation/historical-inflation-rates/)
    have a median of 2.3%, being as high as 8% in 2022 and as low as -0.4% in 2009. The United
    States Federal Reserve has a [target of 2%](https://www.federalreserve.gov/faqs/economy_14400.htm),
    so for our four categories of money above that means that:
    - dead money would earn less than 2%
    - safe money would earn around 2%
    - healthy money would earn somewhere between 5-10%
    - wealthy money would earn above 10%

    ## Different Classes of Assets

    When people think about investing, the most common asset that comes to mind is stocks.
    However, there are plenty of other asset classes that are worth knowing about in order
    to diversify our returns and minimize the likelihood of a crash in our investments due
    to relying on only one asset class. These asset classes include:
    1. **Equities or stocks**, where you essentially buy a portion of a company or companies
    2. **Fixed income securities**, such as bonds, where you serve as a bank of sorts investing
         a sum of money in exchange for regular payments of principal and interest to pay off
         your investment over time
    3. **Commodities**, where you own physical objects like real estate or precious metals
    4. **Cash or cash equivalents**, such as foreign currencies or even cryptocurrency

    These classes have many different types of assets within them as well as various strategies
    that help to increase return on investment or decrease risk. That said, it is generally true
    that the assets that will provide the greatest return are those that will require having
    a special advantage of some kind. This special advantage is what keeps others from joining
    in and neutralize the ability to earn above-average profits. This means that if you want to
    have "wealthy money" that earns well above 10%, it will likely require some work on your
    part; however, if you're not interested in this, there are plenty of strategies, such as
    stock market index funds, that allow you to still earn well above the inflation rate.

    > I think mutual funds are an absolutely outstanding way to invest. I believe that every
    > person should own their own home, own real estate, and have an individual stock account
    > or own mutual funds. Those are the only ways you can make any substantial income above
    > your salary. (_Market Wizards_, Schwager)

    ## Risk

    This brings us to our next point: risk. It can be scary to think about saving all of
    your money and then risk losing it by investing in something that decreases in value or crashes altogether.
    However, since inflation is **guaranteed** in the United States, money that is not earning
    interest is **guaranteed** to decrease in value. Which would you rather have: a guaranteed
    loss or a potential loss?

    > The person who takes no chances, generally has to take whatever is left when others are
    > through choosing. Over-caution is as bad as under-caution. Both are extremes to be
    > guarded against. Life itself is filled with the element of chance. (_Think and Grow Rich_, Napoleon Hill)

    American investor and philanthropist Jack Bogle was stumped by this very problem when
    he created index funds in 1976. While failing to create a strategy that would consistently
    outperform the market, he instead chose to *decrease* the cost associated with managing
    stocks and *decrease* the risk associated with owning individual stocks. By making the asset
    the whole of the financial market, Bogle created an investment vehicle that was built on the
    entire American economy. This is why index funds have been such a great way to invest: if
    you believe that the American economy will continue growing over time, then investing in an
    index fund is a great way to benefit from that growth!

    If you're still unconvinced, listen to what Morgan Housel says in _Same As Ever_:
    > Real GDP per capita increased eightfold in the last hundred years. America of the 1920s
    > had the same real per-capita GDP as Turkmenistan does today. Our growth over the last
    > century has been unbelievable. But GDP growth averages about 3 percent per year, which is
    > easy to ignore in any given year, decade, or lifetime. Americans over age fifty have seen
    > real GDP per person at least double since they were born. But people don't remember the
    > world when they were born. They remember the last few months, when progress is always
    > invisible.

    ## Staying in the Game

    It would be an incomplete conversation about risk without talking about time horizons.
    "Investing has the same benefits as running a casino: The odds are stacked in your favor
    if you are patient and willing to endure the occasional setback." (_Naked Economics_, Wheelan)

    In the U.S. markets, the historical odds of making money over a one day period are
    50/50, 68% in one-year periods, 88% in 10-year periods, and 100% in 20-year periods so far.
    The longer you're able to stay in the game and hold your investments, the greater chance you
    have of benefiting from time. (_The Psychology of Money_, Housel).

    Not only does this benefit you from the standpoint of risk, but it also allows your
    investments to compound and grow over time when things are going well. For example, if you
    bought a \$100,000 investment house each year by putting \$10,000 down and achieved only a
    modest 5 percent rate of return on the total value of the assets, you'd be a millionaire
    in less than a decade. (_The Millionaire Real Estate Investor_, Keller)

    ## The Hunt

    As we covered earlier, the difference between healthy money and wealthy money is getting
    a greater return; however, finding these greater returns in a way that doesn't increase
    risk is the tricky part. For those who want to be wealthy, this is where the art and
    practice of investing takes place. In the words of Gary Keller:

    > Investors are defined by their expectation for financial gain and the process they
    > follow to minimize financial risk. They make it their practice to study and know
    > market value, and then they go out to find assets priced below that value. They
    > don't count on appreciation to bail them out; they make their money going in. Like
    > a bargain hunter, they find as much joy in the search for a bargain as in the
    > transaction itself. (_The Millionaire Real Estate Investor_, Keller)

    The work involved to do this well won't appeal to most, and may not even appeal to you: that's
    ok! It's easy to see the wealthy like Warren Buffett and wish we had what they had,
    but when we peek behind the curtain and realize all the sacrifices they have made to make
    their life happen, whether that be in not spending time with family or not taking the time
    to enjoy the many other wonders in life, it's easier to be satisfied with smaller returns
    that require less effort.

    ## Conclusion

    This quadrant is the trickiest to master and requires the most work to do well. If you
    have the desire and persistence, you can shorten the time it takes to reach your goal
    by identifying investments. To see some examples, let's look at some examples of
    compounding comparisons.
""")

### TODO: Create tool to analyze assets:
# inputs - savings rates, ROI, starting point, target
