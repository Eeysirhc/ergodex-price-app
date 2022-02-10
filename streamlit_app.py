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
ticker_selection = token_prices.ticker.unique()



# TICKER SELECTOR BUTTONS
ticker = st.radio("Ticker selection:", ticker_selection)

# PROCESS DATA
## FILTER ON SPECIFIC PRICING
token_prices = token_prices[token_prices['ticker'] == ticker]
token_prices = token_prices[['global_index', 'price']]

## GRAB MOST RECENT PRICE POINT
token_latest = token_prices['price'].iloc[-1]
token_latest = round(token_latest, 5)


# PLOT CONFIG
base = alt.Chart(token_prices).encode(
	x='global_index',
	y='price',
	tooltip=['global_index', 'price'])

line = base.mark_line()
points = base.mark_point(filled=True, size=40)
chart = (line + points).interactive()

## PRICE
st.write('### ', ticker,  'Price: ', token_latest)

## FINAL GRAPH
st.altair_chart(chart, use_container_width=True)


st.write(
"""
## To-Do
* Automate datastream
* Clean up ticker selector
* Imrpove UI
* Flip y-axis for certain pairs (ex: erg/ergopad where "down" is actually good)
* Add more stuff (lol)
""")


