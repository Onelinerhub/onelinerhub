# How can I get started with a free trial of Google BigQuery?
// plain

Getting started with a free trial of Google BigQuery is easy.

1. Create a Google Cloud Platform account.
2. Go to the [BigQuery Console](https://console.cloud.google.com/bigquery) in the Google Cloud Platform Console.
3. Click the "Try it free" button.
4. Accept the terms of service.
5. Click the "Activate" button.
6. Once your account is activated, you can start using BigQuery.
7. To test out BigQuery, you can run a simple SQL query in the BigQuery Console. For example, the following query will return the top 10 most populous cities in the world:
```
SELECT name, population
FROM `bigquery-public-data.census_bureau_world_cities.world_cities`
ORDER BY population DESC
LIMIT 10
```

The output of this query should look like this:
```
+-----------------+------------+
|      name       | population |
+-----------------+------------+
| Shanghai        | 24150000   |
| Istanbul        | 13720000   |
| Karachi         | 12920000   |
| Mumbai          | 12690000   |
| Moscow          | 12500000   |
| São Paulo       | 12180000   |
| Beijing         | 11720000   |
| Guangzhou       | 11070000   |
| Delhi          | 11060000   |
| Shenzhen        | 10358000   |
+-----------------+------------+
```

By running this query, you can get a quick introduction to BigQuery and start exploring the data available in BigQuery.

onelinerhub: [How can I get started with a free trial of Google BigQuery?](https://onelinerhub.com/google-big-query/how-can-i-get-started-with-a-free-trial-of-google-bigquery)