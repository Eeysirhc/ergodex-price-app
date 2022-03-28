##############################
# Author: eeysirhc
# Date written: 2022-02-09
# Last updated: 2022-03-28
# Objective: bare bones streamlit app to visualize ErgoDEX liquidity pair prices
##############################

import streamlit as st
import pandas as pd
import altair as alt 


st.write(
"""
# ErgoDEX: token prices
""")

st.write("[Leaderboard](https://share.streamlit.io/eeysirhc/ergo-tokens-board/main/app.py)")

# LOAD DATA
token_prices = pd.read_csv("price-data.csv")
token_prices = token_prices[['timestamp', 'yx_ticker', 'yx_price', 'xy_ticker', 'xy_price']]

# RESHAPE DATA
token_prices_yx = token_prices[['timestamp', 'yx_ticker', 'yx_price']]
token_prices_yx = token_prices_yx.rename(columns={'yx_ticker': 'ticker', 'yx_price': 'price'})
token_prices_xy = token_prices[['timestamp', 'xy_ticker', 'xy_price']]
token_prices_xy = token_prices_xy.rename(columns={'xy_ticker': 'ticker', 'xy_price': 'price'})

token_final = pd.concat([token_prices_yx, token_prices_xy], axis=0)
token_final['timestamp'] = pd.to_datetime(token_final['timestamp'])

## SHAPE DATA FOR CANDLESTICK CHARTS
token_candlestick = token_final.groupby(['ticker', pd.Grouper(key='timestamp', freq='240min')])\
         .agg(open=pd.NamedAgg(column='price', aggfunc='first'), 
              close=pd.NamedAgg(column='price', aggfunc='last'), 
              high=pd.NamedAgg(column='price', aggfunc='max'), 
              low=pd.NamedAgg(column='price', aggfunc='min'))\
         .reset_index()

## CREATE LIST OF TICKER SELECTION
ticker_selector = token_final.sort_values(by='ticker')
ticker_selector = ticker_selector[ticker_selector['ticker'].notnull()]
ticker_selector = ticker_selector.ticker.unique()

## CUSTOMER VARIABLES
user_selection = st.selectbox("", ticker_selector)

token_selection = token_final[token_final['ticker'] == user_selection].sort_values('timestamp', ascending=True)
token_selection_candlestick = token_candlestick[token_candlestick['ticker'] == user_selection].sort_values('timestamp', ascending=True)

## GRAB MOST RECENT PRICE POINT
price_pair = token_selection['price'].iloc[-1]
price_pair = round(price_pair, 5)


# PLOT CONFIG
## LINE CHART
base = alt.Chart(token_selection).encode(
	alt.X('timestamp', axis=alt.Axis(title='Date')),
	alt.Y('price', axis=alt.Axis(title='Price')),
	tooltip=['timestamp', 'price'])

line = base.mark_line()
points = base.mark_point(filled=True, size=10)
line_chart = (line + points).interactive()

## CANDLESTICK CHART
base = alt.Chart(token_selection_candlestick).encode(
    alt.X('timestamp', axis=alt.Axis(title='Date')),
    color=alt.condition("datum.open <= datum.close",
                        alt.value("#06982d"), alt.value("#ae1325"))
)

candlestick_chart = alt.layer(
    base.mark_rule().encode(alt.Y('low', title='Price',
                                    scale=alt.Scale(zero=False)), alt.Y2('high')),
    base.mark_bar().encode(alt.Y('open'), alt.Y2('close')),
).interactive()





## PRICE
st.write('### Price: ', price_pair)

## FINAL
st.altair_chart(line_chart, use_container_width=True)
st.write('4hr Candles')
st.altair_chart(candlestick_chart, use_container_width=True)



st.write(
"""
## Backlog
* [Like what you see?](https://explorer.ergoplatform.com/payment-request?address=9fGGAv2h8PJe4tbTUy5LD6FHS64i367Ctkm9ZPFfcZUB9mrFz3x&amount=0&description=) :)
* Toggle to flip y-axis for certain pairs
* [ERGO Seed Phrase #8](https://www.reddit.com/r/ergonauts/comments/t2n8yj/the_15_days_of_ergo_seed_phrases/): "Don't _____ Be Happy"
""")



