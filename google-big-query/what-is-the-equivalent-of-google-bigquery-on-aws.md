# What is the equivalent of Google BigQuery on AWS?
// plain

The equivalent of Google BigQuery on AWS is Amazon Athena. Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. It allows you to quickly analyze large amounts of data stored in S3 without having to manage any infrastructure.

For example, you can use the following code to query a table in S3:

```
SELECT *
FROM my_table
WHERE my_column = 'my_value'
```

This query will return all rows from the table where the column `my_column` is equal to `my_value`.

Athena is serverless, so there is no infrastructure to manage. It is also highly scalable and can be used to query petabytes of data. It supports a variety of data formats, including CSV, JSON, ORC, Apache Parquet, and Avro.

Athena also integrates with other AWS services, such as Amazon QuickSight for visualizations and Amazon Glue for data cataloging.

Here are some ## Helpful links

- [Amazon Athena Documentation](https://docs.aws.amazon.com/athena/latest/ug/what-is.html)
- [Getting Started with Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/getting-started.html)
- [Athena Pricing](https://aws.amazon.com/athena/pricing/)

onelinerhub: [What is the equivalent of Google BigQuery on AWS?](https://onelinerhub.com/google-big-query/what-is-the-equivalent-of-google-bigquery-on-aws)