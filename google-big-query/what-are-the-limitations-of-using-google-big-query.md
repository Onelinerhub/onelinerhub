# What are the limitations of using Google Big Query?
// plain

Google BigQuery is a powerful cloud-based database that can store and analyze large amounts of data quickly and efficiently. However, there are some limitations to using it.

1. Cost: BigQuery can be expensive, depending on the amount of data being stored and the number of queries being run.
2. Storage Limits: BigQuery has a storage limit of 10TB per project. If more data needs to be stored, additional projects will need to be created.
3. Query Limits: BigQuery has a limit of 20,000 queries per day and 10 queries per second. If more queries are needed, additional projects will need to be created.
4. Data Types: BigQuery only supports a limited set of data types, such as strings, integers, and floats. It does not support complex data types such as JSON or XML.
5. Data Transfer Limits: BigQuery has a limit of 10GB per data transfer, meaning that large datasets will need to be split into multiple transfers.
6. Query Language: BigQuery only supports SQL, so if another query language is needed, it will need to be translated into SQL.
7. Security: BigQuery does not support encryption or other security measures, so data must be secured in other ways.

## Example


```
SELECT *
FROM my_table
LIMIT 10
```

This query will return the first 10 rows from the table `my_table`.

## Helpful links

- [BigQuery Pricing](https://cloud.google.com/bigquery/pricing)
- [BigQuery Limits](https://cloud.google.com/bigquery/quotas)
- [BigQuery Data Types](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types)

onelinerhub: [What are the limitations of using Google Big Query?](https://onelinerhub.com/google-big-query/what-are-the-limitations-of-using-google-big-query)