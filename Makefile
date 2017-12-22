.PHONY: setupdb config install start all
all: setupdb config install start

setupdb:
	mysql -u $(user) -p$(pass) -e "CREATE DATABASE IF NOT EXISTS $(db);"
	mysql -u $(user) -p$(pass) $(db) < db/USDA_Schema.sql
	mysql -u $(user) -p$(pass) $(db) < db/USDA_data.sql
	mysql -u $(user) -p$(pass) $(db) < db/stored_procedures.sql
	# mysql -u $(user) -p$(pass) $(db) < db/permissions.sql

config:
	echo "[database]\ndb_user=$(user)\ndb_password=$(pass)\ndb_dbname=$(db)" | tee config.ini

install:
	pip install -r requirements.txt

start:
	python healthApp.py
