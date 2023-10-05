import pandas as pd 
import streamlit as st 
import plotly.express as px 
import matplotlib.pyplot as plt
dataset = pd.read_excel('sales.xlsx')
st.set_page_config(page_title="Restaurant Sales",layout="wide")
st.sidebar.title("Restaurant Dashboard")
st.sidebar.header("Filter By:")
category=st.sidebar.multiselect("Filter By Category:",
                                 options=dataset["Category"].unique(),
                                 default=dataset["Category"].unique())

selection_query=dataset.query(
    "Category==@category"
)  

st.dataframe(selection_query)

st.title("Restaurant Dashboard")
total_profit=(selection_query["Profit"].sum())
avg_rating=round((selection_query["Avg_Rating"].mean()),2)

first_column,second_column=st.columns(2)

with first_column:
    st.markdown("### Total Profit:")
    st.subheader(f'{total_profit}$')

with second_column:
    st.markdown("### AVG Products Rating")
    st.subheader(f'{avg_rating}')


st.markdown("---")
profit_by_category=(selection_query.groupby(by=["Category"]).sum()[["Profit"]])
profit_by_category_barchart=px.bar(profit_by_category,
                            x="Profit",
                            y=profit_by_category.index,
                            title="profit By Category",
                            color_discrete_sequence=["#17f50c"],
                            )

profit_by_category_barchart.update_layout(plot_bgcolor="rgba(0,0,0,0)",xaxis=(dict(showgrid=False)))

print(profit_by_category)  

profit_by_category_piechart=px.pie(profit_by_category,names=profit_by_category.index,values="Profit",title="profit % By Category",
hole=0.3,color=profit_by_category.index,color_discrete_sequence=px.colors.sequential.RdPu_r)

left_column,right_column=st.columns(2)
left_column.plotly_chart(profit_by_category_barchart,use_container_width=True)
right_column.plotly_chart(profit_by_category_piechart,use_container_width=True)


hide= """
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
"""
st.markdown(hide,unsafe_allow_html=True)