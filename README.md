# DatabasesFinal415

## To build and run the application:
```bazaar
make user=[username] pass=[password] db=[dbname]
```
This command does the following:
1. Creates a new MySQL database for the application and setups the USDA tables in the database.
2. Creates a `config.ini` file needed for the application to connect to the database.
3. Installs the application's python package requirements with `pip`.
4. Starts the application.

## To setup the environment run:

```
pip install -r requirements.txt
```

## To run the app:

  ```
  python healthApp.py
  ```
  (runs on localhost:5000)

### Requirements:


  Create a *config.ini* file. EX:

  ```
  [database]
  db_user=root
  db_password=root
  db_dbname=project1
  ```
  Configure accordingly to your own environment's root password.

Code separated into *models.py*, *views.py*, *healthApp.py*.
All of the routes go into *views.py*
Models go into *models.py*
*healthApp.py* basically instantiates app, imports views and models.
