/***************************
Author: eeysirhc
Date written: 2022-02-11
Last updated: 2022-04-02
Objective: ETL script to take price_data and dump into CSV

To run from terminal using default credentials
PGPASSWORD=ergodex psql -h localhost -p 5432 -d ergodex -U ergodex -f etl-price-data.sql
***************************/

\copy (select timestamp, yx_ticker, yx_price, xy_ticker, xy_price from price_data) to 'price-data.csv' with csv header ;

;

