# How can I use timestamps in Google Big Query?
// plain

Google Big Query supports the use of timestamps to store and query date and time values. A timestamp is a type of data that records when a certain event occurred, and is stored in a format that is easy to read and understand.

## Example code

```
# Standard SQL
SELECT *
FROM `bigquery-public-data.samples.natality`
WHERE timestamp > '2016-01-01'
```

In the above example, the `timestamp` column is used to filter the data to only include records that occurred after January 1, 2016.

## Code explanation

- `SELECT *`: This is a SQL statement that specifies which columns to select from the table.
- `FROM `bigquery-public-data.samples.natality`: This is the table name.
- `WHERE timestamp > '2016-01-01'`: This is the condition used to filter the data, in this case only records with a timestamp after January 1, 2016 will be returned.

For more information about timestamps in Google Big Query, please refer to the [Google Big Query Documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#timestamp-type).

onelinerhub: [How can I use timestamps in Google Big Query?](https://onelinerhub.com/google-big-query/how-can-i-use-timestamps-in-google-big-query)