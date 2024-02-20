import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

from helper.page_setup import setup_page


setup_page()

st.write("""
    # Debt as a Tool

    _“God plays dice with the universe. But they're loaded dice. And the main objective is to find out by what
    rules they were loaded and how we can use them for our own ends.”_ - Joseph Ford

    ## Bad Debt vs. Good Debt

    Many people have different perspectives on debt. Personal finance guru Dave Ramsey is well-known
    for being a staunch advocate against debt:
    > If you owe any money to anyone for any reason—that's debt. Now that we've got that foundation,
    > let's talk about what you can do to get debt out of your life. Forever and ever.
    > ([_How to Pay Off Debt_](https://www.ramseysolutions.com/debt/how-to-pay-off-debt))

    On the other hand, Robert Kiyosaki, Japanese businessman and author of _Rich Dad, Poor Dad_, doesn't
    shy away from it:
    > Interviewer: "In one of your YouTube videos, you actually said that you're currently \$600 million in debt."
    >
    > Kiyosaki: (Shakes head and waits) "$1.2 billion."
    >
    > ([YouTube](https://www.youtube.com/watch?v=5pa-BWa4Ntc&ab_channel=djvlad))

    Which approach is right? To bridge the gap between these two ideas, it's essential to first
    understand how that debt is being used. For example, if you were get a loan in order to
    finance a new car, this debt would be traded for a vehicle; you borrow money in order to get
    a means of transportation. However, it's important to understand what is actually happening
    under the hood (😉). This car loan will be repaid back, often with interest, so that the
    loan *grows over time*, becoming more expensive the longer it goes without being paid off.
    Additionally, the vehicle that you purchased is also *depreciating* in value with every day
    that passes, especially on that first day when you drive it off the dealer's lot. In this
    case, money was borrowed to purchase something that goes *down in value over time*.

    Now, consider a second example: you have some savings and want to buy a rental property, but
    you don't have enough to cover the cost of the entire property. Therefore, you find a bank
    that's willing to lend you enough to purchase this property. Just as before, this loan
    comes with the expectation that you will make small payments, often for the next 30 years,
    to pay off the original loan (called principal) as well as the accrued interest; just as
    before, this loan *grows over time*, becoming more expensive the longer it goes without
    being paid off. However, the key difference is in what happens to the item purchased: in
    the case of the vehicle, it _decreases_ in value; in the case of the property, it _increases_
    in value. Not only that, but the property, if occupied, also puts money back into your property
    in the form of rent (or additional income). Therefore, in the case of the rental property, money
    was borrowed to purchase something that goes *up in value over time* while also (hopefully)
    putting some additional money in your pocket.

    This is the key difference between what is known as "bad debt" and "good debt".
    Bad debt is used to purchase things that decrease in value; good debt is used to
    purchase things that increase in value.

    As we covered in the Expenses quadrant, the United States is a culture of consumerism.
    It provides a financial system that makes it possible to use debt to make "bad debt"
    purchases in the form of credit cards, car loans, and even home mortgages. In some situations,
    this can be beneficial if you need but can't afford groceries for the week, paying the full
    college cost, or needing to replace a broken-down car quickly, but one should be cautious
    of letting short-term, urgent needs become long-term habits and patterns.
""")

# TODO: Create tool to analyze debt:
# Debt Name, Debt Amount, Interest Rate, Income Earned from Debt, Appreciation Earned from Debt, Net Annual Cost, Good/Bad Debt

# TODO: Add section below to introduction of tool
    # As part of this lesson, we're going to take a deep dive into our debts and analyze
    # each one to determine the best path forward to reaching our financial independence.
    # Every debt that we're able to get rid of is additional savings that can be re-directed
    # from paying off debts to purchasing assets, letting us get to our financial goal even sooner!
