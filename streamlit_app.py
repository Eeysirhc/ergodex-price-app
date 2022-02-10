##############################
# Author: eeysirhc
# Date written: 2022-02-09
# Last updated: 2022-02-10
# Objective: bare bones streamlit app to visualize ErgoDEX liquidity pair prices
##############################

import streamlit as st
import pandas as pd
import altair as alt 


st.write(
"""
# ErgoDEX: token prices
""")

# LOAD DATA
token_prices = pd.read_csv("price-data.csv")

## REMOVE NULLS
token_prices = token_prices[token_prices['ticker'].notnull()]

## CREATE LIST OF TICKER SELECTION
y_ticker = token_prices.y_ticker.unique()
x_ticker = token_prices.x_ticker.unique()

col1, col2 = st.columns(2)

# TICKER SELECTOR BUTTONS
## PAIR 1
y_value = col1.radio("Pair 1", y_ticker)

## PAIR 2
x_value = col2.radio("Pair 2", x_ticker)


# COMPUTE PRICING DATA
token_final = token_prices[token_prices['y_ticker'] == y_value]
token_final = token_final[token_final['x_ticker'] == x_value]
token_final['price'] = token_final['y_amount'] / token_final['x_amount']

## GRAB MOST RECENT PRICE POINT
price_pair = token_final['price'].iloc[-1]
price_pair = round(price_pair, 5)


# PLOT CONFIG
base = alt.Chart(token_final).encode(
	x='global_index',
	y='price',
	tooltip=['global_index', 'price'])

line = base.mark_line()
points = base.mark_point(filled=True, size=40)
chart = (line + points).interactive()

## PRICE
st.write('### ', y_value, '/', x_value,  'Price: ', price_pair)

## FINAL GRAPH
st.altair_chart(chart, use_container_width=True)




st.write(
"""
## To-Do
* Automate datastream
* Error handling for invalid token pairs
* Toggle to flip y-axis for certain pairs
""")

