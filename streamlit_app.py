##############################
# Author: eeysirhc
# Date written: 2022-02-09
# Last updated: 2022-02-15
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
token_prices = token_prices[['global_index', 'yx_ticker', 'yx_price', 'xy_ticker', 'xy_price']]

# RESHAPE DATA
token_prices_yx = token_prices[['global_index', 'yx_ticker', 'yx_price']]
token_prices_yx = token_prices_yx.rename(columns={'yx_ticker': 'ticker', 'yx_price': 'price'})
token_prices_xy = token_prices[['global_index', 'xy_ticker', 'xy_price']]
token_prices_xy = token_prices_xy.rename(columns={'xy_ticker': 'ticker', 'xy_price': 'price'})

token_final = pd.concat([token_prices_yx, token_prices_xy], axis=0)


## CREATE LIST OF TICKER SELECTION
ticker_selector = token_final[token_final['ticker'].notnull()]
ticker_selector = ticker_selector.ticker.unique()

user_selection = st.selectbox("", ticker_selector)


## GRAB MOST RECENT PRICE POINT
token_selection = token_final[token_final['ticker'] == user_selection]
price_pair = token_selection['price'].iloc[-1]
price_pair = round(price_pair, 5)


# PLOT CONFIG
base = alt.Chart(token_selection).encode(
	alt.X('global_index', axis=alt.Axis(title='Global Index')),
	alt.Y('price', axis=alt.Axis(title='Price')),
	tooltip=['global_index', 'price'])

line = base.mark_line()
points = base.mark_point(filled=True, size=40)
chart = (line + points).interactive()

## PRICE
st.write('### Price: ', price_pair)

## FINAL GRAPH
st.altair_chart(chart, use_container_width=True)




st.write(
"""
## To-Do
* Automate datastream
* Toggle to flip y-axis for certain pairs
""")

