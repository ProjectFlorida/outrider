# CMDB

## Purpose
This project is a central machine and resource tracker for systems,
databases,  and other operational infrastructure. It will focus on providing
a unified interface to the Chef configuration management system and Amazon's
public cloud.

## Setup
Ensure you have a python environment setup using 2.7 and `pip` available on the
system. You'll also need PostgreSQL installed and a database which is dedicated
to the CMDB.

Once you've got the prerequisites setup, clone this project, and then do the
following:

* `pip install -r requirements.txt`
* `cp config/cmdb.example.yml config/cmdb.development.yml`
* Edit config/cmdb.development.yml to match the setup you've got with PostgreSQL
* Start the server with `python server.py`
