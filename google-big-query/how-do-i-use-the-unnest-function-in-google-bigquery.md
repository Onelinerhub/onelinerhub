# How do I use the UNNEST function in Google BigQuery?
// plain

The UNNEST function in Google BigQuery is used to expand an array into a set of rows. It can be used to expand multiple arrays at once.

For example, the following query uses the UNNEST function to expand two arrays, `arr1` and `arr2`, into two sets of rows:

```
SELECT *
FROM UNNEST(arr1, arr2)
```

The output from this query would look like this:

```
Row arr1  arr2
1   1     a
2   2     b
3   3     c
```

## Code explanation


1. `SELECT *` - Selects all columns from the table.
2. `FROM UNNEST(arr1, arr2)` - Uses the UNNEST function to expand the two arrays, `arr1` and `arr2`, into two sets of rows.
3. `arr1` and `arr2` - The two arrays to be expanded.

## Helpful links

- [Google BigQuery Documentation - UNNEST](https://cloud.google.com/bigquery/docs/reference/standard-sql/arrays#unnest)
- [Google BigQuery Documentation - Arrays](https://cloud.google.com/bigquery/docs/reference/standard-sql/arrays)

onelinerhub: [How do I use the UNNEST function in Google BigQuery?](https://onelinerhub.com/google-big-query/how-do-i-use-the-unnest-function-in-google-bigquery)