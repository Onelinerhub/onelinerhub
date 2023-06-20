# What is Google Big Query?
// plain

Google BigQuery is a fully managed, serverless data warehouse that enables scalable analysis over petabytes of data. It is a powerful Big Data analytics platform designed to process very large data sets quickly and cost-effectively. BigQuery is a serverless, highly scalable, and cost-effective data warehouse designed for business agility. It supports a wide range of client libraries and applications, including SQL, Python, Java, and Node.js.

## Example code

```
SELECT *
FROM `bigquery-public-data.samples.natality`
WHERE year > 2000
LIMIT 10
```

## Output example


```
Row	year	weight_pounds	mother_age	plurality	gestation_weeks
1	2001	7.5	26	Single(1)	38
2	2001	7.5	33	Single(1)	38
3	2001	7.5	30	Single(1)	38
4	2001	7.5	38	Single(1)	38
5	2001	7.5	29	Single(1)	38
6	2001	7.5	38	Twins(2)	37
7	2001	7.5	20	Single(1)	38
8	2001	7.5	22	Single(1)	38
9	2001	7.5	25	Single(1)	38
10	2001	7.5	25	Single(1)	38
```

## Code explanation

1. SELECT - retrieves data from the specified table.
2. FROM - specifies the table to retrieve data from.
3. WHERE - specifies a condition to filter the data.
4. LIMIT - limits the number of rows returned.

## Helpful links
- [Google BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- [BigQuery Quickstart](https://cloud.google.com/bigquery/docs/quickstarts)
- [BigQuery Samples](https://cloud.google.com/bigquery/docs/samples)

onelinerhub: [What is Google Big Query?](https://onelinerhub.com/google-big-query/what-is-google-big-query-1687229517)