# Outrider

## Purpose
This project is a central machine and resource tracker for systems,
databases,  and other operational infrastructure. It will focus on providing
a unified interface to the Chef configuration management system and Amazon's
public cloud.

## Setup
Ensure you have a python environment setup using 2.7 and `pip` available on the
system. You'll also need PostgreSQL installed and a database which is dedicated
to outrider.

Once you've got the prerequisites setup, clone this project, and then do the
following:

* `pip install -r requirements.txt`
* `cp config/settings.example.yml config/settings.development.yml`
* Edit config/settings.development.yml to match the setup you've got with PostgreSQL
* Start the server with `python server.py`

## Database
This project uses [alembic](http://alembic.readthedocs.org/) to handle database
migrations. It will be installed when you `pip install -r`, but you'll need to
perform an initial migration once the database has been configured. This
command will need to be run after the initial setup and after each subsequent
update of the code:

```
PYTHONPATH=. alembic upgrade head
```

## License

This project is licensed under Apache 2.0. For the full text of the license,
check out the `LICENSE` file included (which should always be redistributed)
with this project.
