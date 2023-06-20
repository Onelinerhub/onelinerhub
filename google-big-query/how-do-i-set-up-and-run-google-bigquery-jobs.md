# How do I set up and run Google BigQuery jobs?
// plain

Setting up and running Google BigQuery jobs is relatively straightforward. To start, you'll need to create a project in the Google Cloud Platform Console. Once the project is created, you can create a BigQuery dataset and tables to store your data.

Once the dataset is created, you can run a query using the BigQuery query language. For example, the following code will query a table called `my_table` and return the first 10 rows:
```
SELECT *
FROM my_table
LIMIT 10
```

You can also use the BigQuery API to run jobs programmatically. For example, the following code will run a query job and return the results:
```
from google.cloud import bigquery

client = bigquery.Client()
query_job = client.query("SELECT * FROM my_table LIMIT 10")
results = query_job.result()

for row in results:
    print(row)
```

The code above consists of the following parts:

- `from google.cloud import bigquery`: imports the BigQuery library
- `client = bigquery.Client()`: creates a BigQuery client
- `query_job = client.query("SELECT * FROM my_table LIMIT 10")`: creates a query job to run the query
- `results = query_job.result()`: retrieves the results of the query job
- `for row in results: print(row)`: prints each row of the results

For more information, please refer to the [BigQuery documentation](https://cloud.google.com/bigquery/docs/).

onelinerhub: [How do I set up and run Google BigQuery jobs?](https://onelinerhub.com/google-big-query/how-do-i-set-up-and-run-google-bigquery-jobs)