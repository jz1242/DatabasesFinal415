.PHONY: all
all:
	mysql -u $(root) -p $(db) < db/USDA_schema.sql
	mysql -u $(root) -p $(db) < db/USDA_data.sql
	mysql -u $(root) -p $(db) < db/stored_procedures.sql
	mysql -u $(root) -p $(db) < db/permissions.sql

.PHONY: setupdb
setupdb:
	mysql -u $(root) -p $(db) < db/USDA_schema.sql
	mysql -u $(root) -p $(db) < db/USDA_data.sql
	mysql -u $(root) -p $(db) < db/stored_procedures.sql
	mysql -u $(root) -p $(db) < db/permissions.sql

.PHONY: run
run:
	python healthApp.py