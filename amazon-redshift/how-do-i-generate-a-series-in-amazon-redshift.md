# How do I generate a series in Amazon Redshift?
// plain

Generating a series in Amazon Redshift is done using the `generate_series` function. This function allows you to generate a series of values based on a start and end value, as well as an interval.

For example, this code will generate a series of numbers between 1 and 10, with an interval of 2:

```
SELECT *
FROM generate_series(1, 10, 2);
```

The output of this code will be:

```
1
3
5
7
9
```

The syntax of the `generate_series` function is as follows:

`generate_series(start, end, interval)`

- `start`: The start of the series
- `end`: The end of the series
- `interval`: The interval between each number in the series

You can also generate a series of dates using the `generate_series` function. For example, this code will generate a series of dates between two dates, with an interval of one day:

```
SELECT *
FROM generate_series('2020-01-01', '2020-01-10', '1 day');
```

The output of this code will be:

```
2020-01-01
2020-01-02
2020-01-03
2020-01-04
2020-01-05
2020-01-06
2020-01-07
2020-01-08
2020-01-09
2020-01-10
```

For more information about the `generate_series` function, please see the [Amazon Redshift documentation](https://docs.aws.amazon.com/redshift/latest/dg/r_GENERATE_SERIES.html).

onelinerhub: [How do I generate a series in Amazon Redshift?](https://onelinerhub.com/amazon-redshift/how-do-i-generate-a-series-in-amazon-redshift)