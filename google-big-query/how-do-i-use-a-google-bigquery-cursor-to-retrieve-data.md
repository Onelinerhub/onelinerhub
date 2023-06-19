# How do I use a Google BigQuery cursor to retrieve data?
// plain

Google BigQuery allows you to use cursors to retrieve data from a table. A cursor is a pointer to the result set of a query. The cursor can be used to iterate through the results and fetch them one at a time.

For example, to use a cursor to retrieve data from a table, you can use the following code:

```
# Create a BigQuery client
from google.cloud import bigquery
client = bigquery.Client()

# Construct a BigQuery query
query = 'SELECT * FROM `my_dataset.my_table`'

# Create the query job
query_job = client.query(query)

# Create a BigQuery cursor
cursor = query_job.result(timeout=30)

# Iterate through the results and print them
for row in cursor:
    print(row)

# Output:
# {'column_1': value_1, 'column_2': value_2, ...}
# {'column_1': value_3, 'column_2': value_4, ...}
# ...
```

The code above:

1. Creates a BigQuery client.
2. Constructs a BigQuery query.
3. Creates a query job.
4. Creates a BigQuery cursor.
5. Iterates through the results and prints them.

For more information, please refer to the [Google BigQuery documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-manipulation-language#select).

onelinerhub: [How do I use a Google BigQuery cursor to retrieve data?](https://onelinerhub.com/google-big-query/how-do-i-use-a-google-bigquery-cursor-to-retrieve-data)