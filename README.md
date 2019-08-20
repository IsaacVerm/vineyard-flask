# vineyard Flask

## Virtual environment

First create a [virtual environment](https://docs.python.org/3/tutorial/venv.html):

```
python3 -m venv venv
```

Activate this virtual environment:

```
source venv/bin/activate
```

Install the packages in `requirements.txt` (this file contains a list of packages with the version used):

```
pip install -r requirements.txt
```

To add more packages to `requirements.txt`:

```
pip install {package}
pip freeze > requirements.txt
```

## Test data

Seed test data:

```
cd sql
touch vineyard.db
sqlite3 vineyard.db < create-tables.sql
sqlite3 vineyard.db < insert-test-data.sql
```

Check state database and tables (after creation database):

```
sqlite3 vineyard.db
.database
.tables
```

Check if table contains something:

```
SELECT * FROM table;
```

Quit sqlite3 console:

```
.exit
```

## Service

### Run

Run Flask:

```
cd service;
env FLASK_APP=model-output-service.py flask run
```

### Endpoints design

#### Both html and json

To make the application more durable some endpoints (e.g. `/output/predictions`) can return either html (to display tables, ...) or straight json (to be used by a front-end framework) depending on what's specified in the `Accept` header. This way there's a backup if the front-end framework should fail and a simple table is displayed with the data.

#### Thresholds are query parameters

Thresholds could be specified in 2 ways:

- in a config file
- as parameters to the endpoints (because [filtering](https://medium.com/@fullsour/when-should-you-use-path-variable-and-query-parameter-a346790e8a6d))

We chose to have them as query parameters to the endpoints. This has some advantages:

* we can set them at a later point (e.g. in the UI)
* make testing easier since you can specify different test cases without having to change any hardcoded config

## Tests

API tests are written in Postman.

To run these tests:

```
cd tests;
newman run vineyard.postman_collection.json -e local.postman_environment.json
```

Make sure the service is running in the same environment as the tests. E.g. use environment local in Postman if you run the service on localhost.

Tests are based on the seeded test data in the `sql` folder.
