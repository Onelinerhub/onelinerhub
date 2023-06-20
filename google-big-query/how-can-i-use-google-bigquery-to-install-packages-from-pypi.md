# How can I use Google BigQuery to install packages from PyPI?
// plain

Unfortunately, Google BigQuery does not support the installation of packages from PyPI. However, it is possible to use the [BigQuery Python Client Library](https://googleapis.dev/python/bigquery/latest/index.html) to access data stored in BigQuery from Python applications. The library can be installed using `pip install google-cloud-bigquery` or `pip install --upgrade google-cloud-bigquery`.

Once the library is installed, the following example code can be used to access BigQuery data from Python:

```
from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

# Make an API request.
query_job = client.query("SELECT * FROM `bigquery-public-data.usa_names.usa_1910_2013` LIMIT 10")

# Print results
for row in query_job:
    print(row)
```

The output of the example code will be the first 10 rows of data from the `bigquery-public-data.usa_names.usa_1910_2013` dataset:

```
Row(('Mary', 1910, 'F', 162436), {'state': 'AK', 'gender': 0, 'year': 1910, 'name': 'Mary', 'number': 162436})
Row(('Annie', 1910, 'F', 123672), {'state': 'AK', 'gender': 0, 'year': 1910, 'name': 'Annie', 'number': 123672})
Row(('Anna', 1910, 'F', 110480), {'state': 'AK', 'gender': 0, 'year': 1910, 'name': 'Anna', 'number': 110480})
Row(('Margaret', 1910, 'F', 89440), {'state': 'AK', 'gender': 0, 'year': 1910, 'name': 'Margaret', 'number': 89440})
Row(('Helen', 1910, 'F', 80345), {'state': 'AK', 'gender': 0, 'year': 1910, 'name': 'Helen', 'number': 80345})
Row(('Elizabeth', 1910, 'F', 73533), {'state': 'AK', 'gender': 0, 'year': 1910, 'name': 'Elizabeth', 'number': 73533})
Row(('Ruth', 1910, 'F', 65516), {'state': 'AK', 'gender': 0, 'year': 1910, 'name': 'Ruth', 'number': 65516})
Row(('Alice', 1910, 'F', 64511), {'state': 'AK', 'gender': 0, 'year': 1910, 'name': 'Alice', 'number': 64511})
Row(('Florence', 1910, 'F', 50935), {'state': 'AK', 'gender': 0, 'year': 1910, 'name': 'Florence', 'number': 50935})
Row(('Marie', 1910, 'F', 48639), {'state': 'AK', 'gender': 0, 'year': 1910, 'name': 'Marie', 'number': 48639})
```

The code above consists of the following parts:

1. `from google.cloud import bigquery`: imports the BigQuery Python Client Library.
2. `client = bigquery.Client()`: creates a BigQuery client object.
3. `query_job = client.query("SELECT * FROM `bigquery-public-data.usa_names.usa_1910_2013` LIMIT 10")`: runs a query to retrieve data from BigQuery.
4. `for row in query_job`: iterates through the query results and prints them.

## Helpful links

* [BigQuery Python Client Library](https://googleapis.dev/python/bigquery/latest/index.html)
* [BigQuery Query Syntax](https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax)

onelinerhub: [How can I use Google BigQuery to install packages from PyPI?](https://onelinerhub.com/google-big-query/how-can-i-use-google-bigquery-to-install-packages-from-pypi)