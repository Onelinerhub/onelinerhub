# How do I use Google Big Query as a database?
// plain

Google Big Query is a fully managed, serverless data warehouse that can be used as a database. It allows you to store and query massive datasets quickly, using a SQL-like syntax.

To use Big Query as a database, you first need to create a dataset. This can be done by using the `bq mk` command, like this:
```
bq mk my_dataset
```

Once you have created your dataset, you can create a table within it. This can be done using the `bq mk` command again, like this:
```
bq mk my_dataset.my_table
```

You can then use the `bq load` command to load data into your table. For example, if you have a CSV file called `my_data.csv`, you can load it into your table like this:
```
bq load --source_format=CSV my_dataset.my_table my_data.csv
```

You can then query your data using the `bq query` command. For example, to get the total number of records in your table, you can do this:
```
bq query --use_legacy_sql=false 'SELECT COUNT(*) FROM my_dataset.my_table'
```

The output of this query would look something like this:
```
+----------+
|   f0_    |
+----------+
| 100      |
+----------+
```

Once you have set up your dataset and loaded your data, you can use Big Query as a fully-featured database. You can find more information about using Big Query as a database in the [Big Query documentation](https://cloud.google.com/bigquery/docs/).

onelinerhub: [How do I use Google Big Query as a database?](https://onelinerhub.com/google-big-query/how-do-i-use-google-big-query-as-a-database)