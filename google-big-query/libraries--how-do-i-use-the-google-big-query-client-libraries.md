# libraries

How do I use the Google Big Query client libraries?
// plain

The Google Big Query client libraries allow you to access and manage data stored in Big Query from your application. To use the Google Big Query client libraries, you first need to install the client library. The following example shows how to install the Python client library:

```
pip install --upgrade google-cloud-bigquery
```

Once the client library is installed, you can then use the library to access and manage data stored in Big Query. For example, the following code shows how to query data from Big Query using the Python client library:

```
from google.cloud import bigquery

client = bigquery.Client()
query_job = client.query("SELECT * FROM `bigquery-public-data.usa_names.usa_1910_2013` LIMIT 1000")

for row in query_job:
    print(row)
```

The code above will output the first 1000 rows from the `usa_1910_2013` table in the `bigquery-public-data.usa_names` dataset.

The Google Big Query client libraries also allow you to create and delete datasets, tables, jobs, and other resources. For more information on using the Google Big Query client libraries, please refer to the [official documentation](https://cloud.google.com/bigquery/docs/reference/libraries).

onelinerhub: [libraries

How do I use the Google Big Query client libraries?](https://onelinerhub.com/google-big-query/libraries--how-do-i-use-the-google-big-query-client-libraries)