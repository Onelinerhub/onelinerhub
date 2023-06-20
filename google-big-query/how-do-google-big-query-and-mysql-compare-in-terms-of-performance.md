# How do Google Big Query and MySQL compare in terms of performance?
// plain

Google BigQuery and MySQL are both popular database systems that can be used to store and query large amounts of data. However, they have some key differences in terms of performance.

Google BigQuery is designed to be a highly-scalable, low-latency system that can handle large amounts of data quickly and efficiently. It is optimized for analyzing large datasets and is well-suited for distributed computing tasks. BigQuery also offers a number of features that make it easier to manage data, such as automatic data partitioning and columnar storage.

MySQL, on the other hand, is a relational database system that is designed for smaller datasets. It is optimized for transactions and is well-suited for applications that require frequent updates. MySQL also offers a wide range of features such as triggers and stored procedures.

In terms of performance, BigQuery is generally faster than MySQL for large datasets. It is optimized for distributed computing tasks and can process large amounts of data quickly. MySQL is better suited for smaller datasets and is optimized for transactions.

## Example code


```
SELECT COUNT(*)
FROM bigquery-public-data.samples.shakespeare
```

## Output example


```
1,811,357
```

## Code explanation


- `SELECT`: This keyword is used to select the columns that you want to retrieve from the table.
- `COUNT(*)`: This function is used to count the number of rows in the table.
- `FROM`: This keyword is used to specify the table from which you want to retrieve data.
- `bigquery-public-data.samples.shakespeare`: This is the name of the table from which you want to retrieve data.

## Helpful links

- [Google BigQuery](https://cloud.google.com/bigquery)
- [MySQL](https://www.mysql.com/)

onelinerhub: [How do Google Big Query and MySQL compare in terms of performance?](https://onelinerhub.com/google-big-query/how-do-google-big-query-and-mysql-compare-in-terms-of-performance)