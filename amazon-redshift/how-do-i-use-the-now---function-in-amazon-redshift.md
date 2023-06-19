# How do I use the NOW() function in Amazon Redshift?
// plain

The NOW() function in Amazon Redshift is used to return the current timestamp as a timestamp with time zone. It takes no arguments and can be used in a SELECT statement, as shown in the example below:

```
SELECT NOW();
```

The output of the above statement would be the current timestamp with time zone, for example `2020-10-14 13:20:00.000000-07`.

The parts of the code are:
- `SELECT`: This is the keyword used to select the data from the table.
- `NOW()`: This is the function used to return the current timestamp with time zone.

## Helpful links
- [Amazon Redshift Documentation - NOW Function](https://docs.aws.amazon.com/redshift/latest/dg/r_NOW.html)

onelinerhub: [How do I use the NOW() function in Amazon Redshift?](https://onelinerhub.com/amazon-redshift/how-do-i-use-the-now---function-in-amazon-redshift)