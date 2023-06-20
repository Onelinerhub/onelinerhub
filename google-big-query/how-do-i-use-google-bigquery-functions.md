# How do I use Google BigQuery functions?
// plain

Google BigQuery functions allow you to perform various operations on your data. To use the functions, you must first create a BigQuery dataset.

## Example code

```
# Create a BigQuery dataset
bq mk mydataset
```

## Output example

```
Dataset 'mydataset' successfully created.
```

Once the dataset is created, you can use the BigQuery functions to perform various operations on the data. Here is a list of some of the operations you can perform:

1. **Select** - Select data from a table.

   Example code:
   ```
   # Select data from a table
   bq query --use_legacy_sql=false 'SELECT * FROM mydataset.mytable'
   ```
   Output:
   ```
   +--------+----------+
   |  Col1  |  Col2    |
   +--------+----------+
   |  1     |  Apple   |
   |  2     |  Orange  |
   |  3     |  Banana  |
   +--------+----------+
   ```

2. **Insert** - Insert data into a table.

   Example code:
   ```
   # Insert data into a table
   bq query --use_legacy_sql=false 'INSERT INTO mydataset.mytable (Col1, Col2) VALUES (4, "Lemon")'
   ```
   Output:
   ```
   Inserted 1 row(s) in 0.7s
   ```

3. **Update** - Update data in a table.

   Example code:
   ```
   # Update data in a table
   bq query --use_legacy_sql=false 'UPDATE mydataset.mytable SET Col2 = "Mango" WHERE Col1 = 2'
   ```
   Output:
   ```
   Updated 1 row(s) in 0.7s
   ```

4. **Delete** - Delete data from a table.

   Example code:
   ```
   # Delete data from a table
   bq query --use_legacy_sql=false 'DELETE FROM mydataset.mytable WHERE Col1 = 3'
   ```
   Output:
   ```
   Deleted 1 row(s) in 0.7s
   ```

These are just a few of the operations you can perform with Google BigQuery functions. For more information, please refer to the [BigQuery Documentation](https://cloud.google.com/bigquery/docs/).

onelinerhub: [How do I use Google BigQuery functions?](https://onelinerhub.com/google-big-query/how-do-i-use-google-bigquery-functions)