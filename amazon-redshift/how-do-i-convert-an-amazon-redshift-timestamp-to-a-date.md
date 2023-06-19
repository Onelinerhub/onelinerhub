# How do I convert an Amazon Redshift timestamp to a date?
// plain

The Amazon Redshift `timestamp` data type stores a date and time. To convert it to a `date` data type, you can use the `date_trunc` function. This function truncates the timestamp to the specified date part, in this case `day`.

## Example code

```
SELECT date_trunc('day', timestamp_column)
FROM table_name;
```

The code will return the timestamp converted to a date.

## Code explanation

- `date_trunc('day', timestamp_column)`: This is the function used to convert the timestamp to a date. The first argument is the date part (here `day`) and the second argument is the timestamp column.

List of ## Helpful links
- [Amazon Redshift Documentation - Date and Time Functions](https://docs.aws.amazon.com/redshift/latest/dg/r_Date_and_time_functions.html)

onelinerhub: [How do I convert an Amazon Redshift timestamp to a date?](https://onelinerhub.com/amazon-redshift/how-do-i-convert-an-amazon-redshift-timestamp-to-a-date)