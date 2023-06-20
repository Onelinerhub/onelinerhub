# How do I rename a column in Google BigQuery?
// plain

Renaming a column in Google BigQuery is a simple process. The following example code shows how to rename a column from `old_name` to `new_name`:

```
ALTER TABLE my_table
RENAME COLUMN old_name TO new_name;
```

No output is generated from this command.

The code consists of two parts:
1. `ALTER TABLE my_table`: This part of the code specifies the table to be altered.
2. `RENAME COLUMN old_name TO new_name;`: This part of the code renames the column `old_name` to `new_name`.

For more information about renaming columns in BigQuery, please see the [official documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-manipulation-language#rename_column).

onelinerhub: [How do I rename a column in Google BigQuery?](https://onelinerhub.com/google-big-query/how-do-i-rename-a-column-in-google-bigquery)