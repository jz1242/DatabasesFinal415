.PHONY: run
run:
	python healthApp.py

.PHONY: setupdb
setupdb:
	mysql -u $(user) -p$(pass) -e "CREATE DATABASE IF NOT EXISTS $(db);"
	mysql -u $(user) -p$(pass) $(db) < db/USDA_Schema.sql
	mysql -u $(user) -p$(pass) $(db) < db/USDA_data.sql
	mysql -u $(user) -p$(pass) $(db) < db/stored_procedures.sql
	mysql -u $(user) -p$(pass) $(db) < db/permissions.sql