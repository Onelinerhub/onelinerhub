# How can I find the median value using PostgreSQL?
// plain

The median value of a set of numbers can be calculated using PostgreSQL by using the `percentile_cont` aggregate function. This function takes two arguments, the first being the column name of the values to be calculated, and the second being the percentile to be calculated. The median value is the 50th percentile, so the following example code can be used to calculate the median value of a column named `column_name`:

```sql
SELECT percentile_cont(0.5) WITHIN GROUP (ORDER BY column_name)
FROM table_name;
```

This will return the median value of the column `column_name` in the table `table_name`.

## Code explanation


* `percentile_cont` - This is the aggregate function used to calculate the percentile value.
* `column_name` - This is the column name of the values to be calculated.
* `0.5` - This is the percentile to be calculated.
* `table_name` - This is the table containing the values to be calculated.

For more information, see the [PostgreSQL documentation for percentile_cont](https://www.postgresql.org/docs/current/functions-aggregate.html).

onelinerhub: [How can I find the median value using PostgreSQL?](https://onelinerhub.com/postgresql/how-can-i-find-the-median-value-using-postgresql)