# ErgoDEX: token price app

This is a simple token price charting app which relies on extracting liquidity pool data and generating a CSV file from the ErgoDEX backend.

## Quick Start

### Get the `ergodex-stats` indexer

Follow the instructions [here](https://github.com/bazuaal/ergodex-stats) on how to get the set of docker containers up and running for the local PostgreSQL database.


### Create summary view

Run the `price-data.sql` file which summarizes all the different tables into a single view.

### Run ETL pipeline for CSV

Assuming you left everything as default you can then execute the following command in your terminal:

`PGPASSWORD=ergodex psql -h localhost -p 5432 -d ergodex -U ergodex -f etl-price-data.sql`




