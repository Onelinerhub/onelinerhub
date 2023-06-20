# How can I create a histogram in Google BigQuery?
// plain

Creating a histogram in Google BigQuery is easy and straightforward. The following example code will generate a histogram of the number of users per age group:

```
SELECT age_group, COUNT(*) AS num_users
FROM `users_table`
GROUP BY age_group
ORDER BY age_group ASC
```

This will generate the following output:

```
age_group  num_users
18-25        15
26-35        20
36-45        12
46-55        7
56-65        5
```

The code for creating a histogram consists of the following parts:

1. SELECT - This specifies the columns that will be used in the histogram. In this example, the age_group column is used.
2. FROM - This specifies the table from which the data will be taken. In this example, it is the `users_table`.
3. GROUP BY - This specifies how the data will be grouped. In this example, it is grouped by age_group.
4. ORDER BY - This specifies the order in which the data will be sorted. In this example, it is sorted by age_group in ascending order.

For more information on creating histograms in Google BigQuery, you can refer to the following links:

- [Google BigQuery Documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/aggregate_functions)
- [Google BigQuery Tutorial](https://cloud.google.com/bigquery/docs/tutorials/aggregating_data_in_bigquery)

onelinerhub: [How can I create a histogram in Google BigQuery?](https://onelinerhub.com/google-big-query/how-can-i-create-a-histogram-in-google-bigquery)