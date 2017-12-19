# DatabasesFinal415

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



Code separated into *models.py*, *views.py*, *healthApp.py*. 
All of the routes go into *views.py*
Models go into *models.py*
*healthApp.py* basically instantiates app, imports views and models.

