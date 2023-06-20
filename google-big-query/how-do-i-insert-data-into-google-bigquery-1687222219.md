# How do I insert data into Google BigQuery?
// plain

To insert data into Google BigQuery, you can use the `INSERT` statement. The following example shows how to insert a record into a table:

```
INSERT INTO mydataset.mytable (name, age)
VALUES ('John', 32)
```

This statement inserts the values `John` and `32` into the columns `name` and `age` of the table `mytable` in the dataset `mydataset`.

The `INSERT` statement can also be used to insert multiple records at once. The following example shows how to insert multiple records into a table:

```
INSERT INTO mydataset.mytable (name, age)
VALUES
('John', 32),
('Mary', 30),
('Bob', 27)
```

This statement inserts three records into the table `mytable` in the dataset `mydataset`.

You can also use the `LOAD` statement to insert data into BigQuery from a file. The following example shows how to load data from a CSV file into BigQuery:

```
LOAD DATA INPATH 'gs://mybucket/data.csv'
INTO mydataset.mytable
```

This statement loads the data from the file `data.csv` in the bucket `mybucket` into the table `mytable` in the dataset `mydataset`.

You can also use the BigQuery API to insert data into BigQuery. The following example shows how to insert data into BigQuery using the API:

```
# Imports the Google Cloud client library
from google.cloud import bigquery

# Instantiates a client
client = bigquery.Client()

# The name for the new dataset
dataset_id = 'mydataset'

# Prepares a reference to the new dataset
dataset_ref = client.dataset(dataset_id)

# Configures the dataset
dataset = bigquery.Dataset(dataset_ref)

# Creates the new dataset
dataset = client.create_dataset(dataset)

# The name for the new table
table_id = 'mytable'

# Prepares a reference to the new table
table_ref = dataset_ref.table(table_id)

# Configures the table schema
schema = [
    bigquery.SchemaField('name', 'STRING'),
    bigquery.SchemaField('age', 'INTEGER')
]

# Configures the table
table = bigquery.Table(table_ref, schema=schema)

# Creates the new table
table = client.create_table(table)

# The data to be inserted
rows = [
    ('John', 32),
    ('Mary', 30),
    ('Bob', 27)
]

# Inserts the data into the table
errors = client.insert_rows(table, rows)

# Prints the errors (if any)
print(errors)
```

This code snippet creates a new dataset and a new table with the specified schema. It then inserts the specified data into the table.

## Helpful links

- [BigQuery Documentation](https://cloud.google.com/bigquery/docs/)
- [BigQuery API Documentation](https://cloud.google.com/bigquery/docs/reference/libraries)

onelinerhub: [How do I insert data into Google BigQuery?](https://onelinerhub.com/google-big-query/how-do-i-insert-data-into-google-bigquery-1687222219)