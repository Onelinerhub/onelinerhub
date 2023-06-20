# How do Google BigQuery and Azure Data Lake compare in terms of performance and cost?
// plain

Google BigQuery and Azure Data Lake are two popular cloud-based data storage and analytics solutions. Both offer powerful features and scalability, but there are some key differences in terms of performance and cost.

In terms of performance, BigQuery is generally faster than Azure Data Lake. BigQuery has a powerful query engine that can quickly analyze and process large amounts of data. On the other hand, Azure Data Lake is more suitable for batch processing and is not as good at handling interactive queries.

In terms of cost, BigQuery is generally more expensive than Azure Data Lake. BigQuery charges based on usage, so the cost can quickly add up depending on the amount of data being processed. Azure Data Lake, on the other hand, has a flat rate for storage and a separate rate for processing, which can be more cost effective for larger data sets.

Below is an example of a query in BigQuery that calculates the total number of records in a table:

```
SELECT COUNT(*)
FROM my_table;
```

## Output example

```
100
```

The code is composed of three parts:
1. `SELECT COUNT(*)` - This selects the total number of records from the table
2. `FROM my_table` - This specifies the table to query
3. `;` - This indicates the end of the query

For more information about BigQuery and Azure Data Lake, you can refer to the following links:
- [BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- [Azure Data Lake Documentation](https://docs.microsoft.com/en-us/azure/data-lake-analytics/)

onelinerhub: [How do Google BigQuery and Azure Data Lake compare in terms of performance and cost?](https://onelinerhub.com/google-big-query/how-do-google-bigquery-and-azure-data-lake-compare-in-terms-of-performance-and-cost)