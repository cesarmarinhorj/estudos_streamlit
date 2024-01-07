import streamlit as st
import pandas as pd
import numpy as np
import random

st.title("DataFrames")

st.text("Random")
df1 = pd.DataFrame(np.random.randn(20, 10), columns=("col %d" % (i+1) for i in range(10)))
st.dataframe(df1)


st.text("Data")
data = {
    "Name": [
        "Braund, Mr. Owen Harris",
        "Allen, Mr. William Henry",
        "Bonnell, Miss. Elizabeth",
    ],
    "Age": [22, 35, 58],
    "Email": ["owen@br", "will@br", "liz@br"],
}
df2 = pd.DataFrame(data)
st.dataframe(df2)



data =     {
        "name": ["Roadmap", "Extras", "Issues"],
        "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
        "stars": [random.randint(0, 1000) for _ in range(3)],
        "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
    }

df3 = pd.DataFrame(data)
st.text("Custom")
st.dataframe(
    df3,
    column_config={
        "name": "App name",
        "stars": st.column_config.NumberColumn(
            "Github Stars",
            help="Number of stars on GitHub",
            format="%d ⭐",
        ),
        "url": st.column_config.LinkColumn("App URL"),
        "views_history": st.column_config.LineChartColumn(
            "Views (past 30 days)", y_min=0, y_max=5000
        ),
    },
    hide_index=True,
)
