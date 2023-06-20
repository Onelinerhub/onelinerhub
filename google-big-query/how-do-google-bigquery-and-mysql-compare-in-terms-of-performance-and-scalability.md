# How do Google BigQuery and MySQL compare in terms of performance and scalability?
// plain

Google BigQuery and MySQL are both popular relational database solutions, but they vary in terms of performance and scalability.

BigQuery is a serverless, highly scalable cloud-based solution that can process large amounts of data quickly. It is designed to handle petabyte-scale datasets with ease and can process complex queries in seconds. It also has automatic data replication and fault tolerance, so it is highly reliable.

MySQL, on the other hand, is an open-source, on-premise solution that is not as scalable as BigQuery. It can process smaller datasets, but it can take longer to process complex queries. It also requires manual data replication and fault tolerance, so it is not as reliable.

**Example Code:**
```
SELECT
  COUNT(*)
FROM
  `bigquery-public-data.samples.shakespeare`
```

**Output:**

`164656`

**Explanation:**

This example code uses BigQuery to count the number of records in the `bigquery-public-data.samples.shakespeare` table.

**## Helpful links**

- [BigQuery Documentation](https://cloud.google.com/bigquery/docs/)
- [MySQL Documentation](https://dev.mysql.com/doc/)

onelinerhub: [How do Google BigQuery and MySQL compare in terms of performance and scalability?](https://onelinerhub.com/google-big-query/how-do-google-bigquery-and-mysql-compare-in-terms-of-performance-and-scalability)