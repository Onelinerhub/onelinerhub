# How do I use Google BigQuery Sandbox?
// plain

Google BigQuery Sandbox is a free, interactive environment for exploring and querying public datasets using BigQuery. It allows users to access a variety of public datasets and query them using standard SQL.

To use Google BigQuery Sandbox, users must first create a Google Cloud Platform (GCP) project. This can be done by visiting the Google Cloud Platform Console. Once the project is created, users can enable the BigQuery API.

Next, users must select the BigQuery Sandbox from the GCP Console. This will open the BigQuery Sandbox web UI. From here, users can select from a variety of public datasets and query them using standard SQL.

## Example code

```
SELECT
  name,
  SUM(number) as total_number
FROM
  `bigquery-public-data.usa_names.usa_1910_current`
GROUP BY
  name
ORDER BY
  total_number DESC
LIMIT
  10
```

## Output example

```
+---------+---------------+
|  name   | total_number  |
+---------+---------------+
| James   | 5074720       |
| John    | 5061897       |
| Robert  | 4788070       |
| Michael | 4265373       |
| Mary    | 4110637       |
| William | 4049134       |
| David   | 3527069       |
| Richard | 2553475       |
| Joseph  | 2529809       |
| Charles | 2443118       |
+---------+---------------+
```

## Code explanation

- SELECT: specifies which columns to include in the result set
- `bigquery-public-data.usa_names.usa_1910_current`: specifies the table to query
- SUM(): calculates the sum of the numbers in the specified column
- GROUP BY: groups the results by the specified column
- ORDER BY: orders the results by the specified column
- LIMIT: restricts the result set to the specified number of rows

## Helpful links
- [Google Cloud Platform Console](https://console.cloud.google.com/)
- [BigQuery Sandbox](https://console.cloud.google.com/bigquery?sq=sandbox)

onelinerhub: [How do I use Google BigQuery Sandbox?](https://onelinerhub.com/google-big-query/how-do-i-use-google-bigquery-sandbox)