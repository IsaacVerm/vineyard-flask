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

## To do

Add tests from `vineyard`.