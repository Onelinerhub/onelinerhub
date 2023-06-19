# How do I use Amazon Redshift Zone Maps to improve query performance?
// plain

Zone Maps are a feature of Amazon Redshift that allows the user to improve query performance by selectively skipping blocks of data that are not necessary for the query. Zone Maps are created by the system and are stored as part of the table metadata.

For example, if you wanted to query a table with a large number of rows, but only wanted to retrieve the rows with a specific value in a column, you could use a Zone Map to skip the blocks that do not contain that value.

## Example code

```sql
SELECT *
FROM my_table
WHERE my_column = 'my_value'
USING ZONE MAP;
```

The above code would use a Zone Map to skip any blocks that do not contain the value 'my_value' in the column 'my_column'.

Zone Maps can be created manually, or they can be created automatically by setting the `enable_zm` configuration parameter to `on`.

Zone Maps can also be used to improve query performance when joining two or more tables. By using Zone Maps, the system can quickly determine which blocks of data are needed for the join, and which can be skipped.

## Helpful links

- [Amazon Redshift Documentation - Zone Maps](https://docs.aws.amazon.com/redshift/latest/dg/cm-c-zm.html)
- [Amazon Redshift Documentation - Working with Zone Maps](https://docs.aws.amazon.com/redshift/latest/dg/cm-c-zm-working-with.html)

onelinerhub: [How do I use Amazon Redshift Zone Maps to improve query performance?](https://onelinerhub.com/amazon-redshift/how-do-i-use-amazon-redshift-zone-maps-to-improve-query-performance)