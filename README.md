# ErgoDEX: token price app

This is a simple token price charting app which relies on extracting liquidity pool data and generating a CSV file from the ErgoDEX backend.

## Quick Start

### Launch the `ergodex-stats` indexer

Pull the repo and follow the instructions [here](https://github.com/bazuaal/ergodex-stats) on how to setup the docker containers to store the ErgoDEX statistics into a local PostgreSQL database.


### Create summary view

Login to your newly created databse and run the `price-data.sql` file which summarizes all the different tables into a single consolidated view.

### Run ETL pipeline

Assuming you left everything as default you can then execute the following command in your terminal:

`PGPASSWORD=ergodex psql -h localhost -p 5432 -d ergodex -U ergodex -f etl-price-data.sql`

The above accesses your database, retrieves the table data, then dumps a CSV file into your working directory.

### Launch app

Finally, make sure you have [Streamlit](https://streamlit.io/) installed then run:

`streamlit run streamlit_app.py`

