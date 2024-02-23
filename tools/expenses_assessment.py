import pandas as pd
import streamlit as st

from helper.vars import assets_data_editor, expenses_data_editor, income_data_editor, liabilities_data_editor


def tool_expenses_assessment():
    # TODO: Finish this tool
    st.markdown("# Expenses Assessments")

    st.write("""
        As we analyze our spending patterns, we're playing for the long game: finding the balance between meeting
        today's needs by spending our money on the things that bring us joy while also meeting future needs by
        investing a sufficient amount of money to reach our financial targets. To do both of these well, we have
        to have a clear picture of what we want in the future and a disciplined lifestyle in the present to work
        towards this in the present.
    """)
    options = st.multiselect(
        "Rank the spend categories in the order of importance to you (you don't have to rank all of them):",
        ["Education", "Entertainment", "Family", "Fitness", "Food", "Gifts", "Housing", "Personal Care", "Pets", "Shopping", "Travel"],
        []
    )
    counter = 0
    ranked_options = []
    for option in options:
        counter += 1
        option = f"{counter}. {option}"
        ranked_options.append(option)

    output = ""
    for option in ranked_options:
        output += option + "\n"
    st.write(output)

    st.write("""
        Using our ranked categories, let's now analyze our expenses for the past month to see how spending patterns
        align with our current, personal priorities.
    """)

    expenses = st.data_editor(
        pd.DataFrame(data= [["", "", 0]], columns=["Category", "Name", "Amount"]),
        column_config={
            "Category": st.column_config.SelectboxColumn(
                label="Category (Dropdown)",
                help="The category of expense",
                options=ranked_options,
                required=True,
                width="large",
            ),
            "Name": st.column_config.TextColumn(
                label="Name",
                help="The name of expense",
                required=False,
                width="medium",
            ),
            "Amount": st.column_config.NumberColumn(
                format="$%d",
                default=0,
                required=True,
                width="medium",
            )
        },
        num_rows="dynamic",
    )
    if expenses["Amount"].sum() != 0:
        expenses_summary = expenses[["Category", "Amount"]].groupby("Category").sum()
        expenses_summary = expenses_summary.rename(columns={"Amount": "Total Amount"})
        expenses_summary.sort_values("Total Amount", ascending=False, inplace=True)
        expenses_summary.reset_index(inplace=True)
        expenses_summary.set_index("Category", inplace=True)
        expenses_summary["% of Total"] = expenses_summary["Total Amount"] / expenses_summary["Total Amount"].sum()
        expenses_summary["% of Total"] = expenses_summary["% of Total"].astype(float).map("{:.1%}".format)
        expenses_summary["Total Amount"] = expenses_summary["Total Amount"].astype(float).map("${:,.2f}".format)

        st.dataframe(data=expenses_summary, use_container_width=True, hide_index=None)

        st.write("""
            With your distribution of priorities in mind, reflect on your spending habits for the past month.
            What are some of the first things that come to mind? Are you prioritizing your values in your spending?
            Are you spending more than you'd like in any category?
        """)
        key = "expenses_reflection_text_area"
        if key not in st.session_state:
            st.session_state[key] = ""
        st.session_state[key] = st.text_area(
            "Expenses Reflection",
            value=st.session_state[key]
        )
