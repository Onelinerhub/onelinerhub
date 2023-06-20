# How do I update data in Google BigQuery?
// plain

Updating data in Google BigQuery is a straightforward process. The simplest way to do this is to use the `UPDATE` statement in BigQuery. This statement allows you to update existing records in a table or view.

Here is an example of the `UPDATE` statement in BigQuery:

```
UPDATE dataset.table
SET column1 = value1,
    column2 = value2
WHERE condition;
```

The `UPDATE` statement first specifies the dataset and table to update. Then, the `SET` clause specifies the columns to update and their new values. Finally, the `WHERE` clause specifies which records to update.

Here is an example of the `UPDATE` statement in action:

```
UPDATE dataset.table
SET column1 = 'Updated Value',
    column2 = 'Updated Value'
WHERE column1 = 'Old Value';
```

This statement will update the records in `dataset.table` where `column1` is equal to `Old Value`. The values of `column1` and `column2` will be set to `Updated Value`.

## Code explanation


* `UPDATE dataset.table` - This line specifies the dataset and table to update.
* `SET column1 = value1, column2 = value2` - This line specifies the columns to update and their new values.
* `WHERE condition` - This line specifies which records to update.

## Helpful links

* [BigQuery Documentation](https://cloud.google.com/bigquery/docs/)
* [UPDATE Statement](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-manipulation-language#update_statement)

onelinerhub: [How do I update data in Google BigQuery?](https://onelinerhub.com/google-big-query/how-do-i-update-data-in-google-bigquery)