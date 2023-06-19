# How can I use the Google BigQuery Connector to access data?
// plain

The Google BigQuery Connector is a powerful tool that allows users to access data stored in Google BigQuery from a variety of programming languages. To use the connector, you must first install the appropriate client library for your language of choice. For example, if you're using Python, you can install the BigQuery Python client library with the following command:

```
pip install --upgrade google-cloud-bigquery
```

Once the client library is installed, you can use it to connect to BigQuery and execute queries. Here is an example of a query written in Python that retrieves data from a BigQuery table:

```
from google.cloud import bigquery

client = bigquery.Client()
query = """
    SELECT *
    FROM `bigquery-public-data.samples.shakespeare`
    WHERE word_count > 10
"""
query_job = client.query(query)

for row in query_job:
    print(row)

```

## Code explanation

1. `from google.cloud import bigquery` - imports the BigQuery client library.
2. `client = bigquery.Client()` - creates a BigQuery client object.
3. `query = """ SELECT * ... """` - defines the query to be executed.
4. `query_job = client.query(query)` - executes the query.
5. `for row in query_job: ...` - iterates over the results of the query.

For more information on using the Google BigQuery Connector, please refer to the [official documentation](https://cloud.google.com/bigquery/docs/reference/libraries).

onelinerhub: [How can I use the Google BigQuery Connector to access data?](https://onelinerhub.com/google-big-query/how-can-i-use-the-google-bigquery-connector-to-access-data)