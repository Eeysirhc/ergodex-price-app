#!/bin/bash
# Author: https://github.com/Bombbird2001

PGPASSWORD=ergodex psql -h localhost -p 5432 -d ergodex -U ergodex -f price-data.sql

PGPASSWORD=ergodex psql -h localhost -p 5432 -d ergodex -U ergodex -f etl-price-data.sql