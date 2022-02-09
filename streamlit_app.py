import streamlit as st
import pandas as pd
import altair as alt 


st.write(
"""
# ErgoDEX: token prices
""")


df = pd.read_csv("price-data.csv")
z = df.ticker.unique()

ticker = st.radio("Ticker selection:", z)

df = df[df['ticker'] ==  ticker]
df = df[['global_index', 'price']]


base = alt.Chart(df).encode(
	x='global_index',
	y='price',
	tooltip=['global_index', 'price'])

line = base.mark_line()
points = base.mark_point(filled=True, size=40)
chart = (line + points).interactive()




st.altair_chart(chart, use_container_width=True)

