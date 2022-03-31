/***************************
Author: eeysirhc
Date written: 2022-02-11
Objective: ETL script to take price_data and dump into CSV

To run from terminal using default credentials
PGPASSWORD=ergodex psql -h localhost -p 5432 -d ergodex -U ergodex -f etl-price-data.sql
***************************/

\copy (select * from price_data) to 'price-data.csv' with csv header ;

;

