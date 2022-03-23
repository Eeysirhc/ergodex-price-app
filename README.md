# ErgoDEX: token price app

This is a simple token price charting app which relies on extracting liquidity pool data and generating a CSV file from the ErgoDEX backend.

## Quick Start

### Launch the `ergodex-stats` indexer

Pull the repo and follow the instructions [here](https://github.com/bazuaal/ergodex-stats) on how to setup the docker containers to store the ErgoDEX statistics into a local PostgreSQL database.

### Execute automation job

The following command will fire off the entire pipeline job for users on...

Mac:

`python3 run_updater.py`

PC:

`placeholder`

This along with the docker container will need to remain active for this app to work.

