import pandas as pd
import streamlit as st

from helper.vars import assets_data_editor, expenses_data_editor, income_data_editor, liabilities_data_editor


def tool_spending_assessment():
    # TODO: Finish this tool
    st.markdown("# Spending Assessments")

    st.write("""

    """)

    st.data_editor(
        pd.DataFrame(data= [["Other", "", 0, 5]], columns=["Category", "Name", "Amount", "Satisfaction Rating"]),
        column_config={
            "Category": st.column_config.SelectboxColumn(
                label="Category (Dropdown)",
                help="The category of expense",
                options=[
                    "Taxes",
                    "Housing",
                    "Transportation",
                    "Food",
                    "Restaurants",
                    "Entertainment",
                    "Other"
                ],
                required=True,
                width="medium",
            ),
            "Name": st.column_config.TextColumn(
                label="Name",
                help="The name of expense",
                required=True,
                width="medium",
            ),
            "Amount": st.column_config.NumberColumn(
                format="$%d",
                default=0,
                required=True,
                width="medium",
            ),
            "Satisfaction Rating": st.column_config.NumberColumn(
                help="On a scale of 1 to 10, how satisfied are you with the amount spent on this purchase?",
                default=5,
                required=True,
                width="medium",
            )

            # "Would you like to spend more, less, or the same in the next month?": st.column_config.SelectboxColumn(
            #     # help="On a scale of 1 to 10, how satisfied are you with the amount spent on this purchase?",\
            #     default=5,
            #     required=True,
            #     width="medium",
            # )
        },
        num_rows="dynamic",
    )

    # TODO: Ask user to think about the areas that they'd like to increase/decrease spending in based on their satisfaction rating
