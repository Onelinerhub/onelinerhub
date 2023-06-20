# How can I use Google Big Query to query JSON data?
// plain

Google BigQuery is a serverless, highly scalable, and cost-effective cloud data warehouse that enables you to query large datasets stored in JSON format. To query JSON data using BigQuery, you can use the `JSON_EXTRACT` function. This function allows you to extract values from a JSON string.

For example, to extract the `name` field from the following JSON string, you can use the following code:
```
SELECT JSON_EXTRACT(data, '$.name') AS name
FROM `mydataset.mytable`
```
The output of the above query would be:
```
name
John Doe
```

The `JSON_EXTRACT` function takes two parameters:
1. The JSON string to extract from
2. The path to the value to be extracted

The path is a string of dot-separated keys that identify the value to be extracted. In the above example, the path is `$.name`, which indicates that the value of the `name` field should be extracted.

For more information on the `JSON_EXTRACT` function, see the [BigQuery documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/json_functions).

onelinerhub: [How can I use Google Big Query to query JSON data?](https://onelinerhub.com/google-big-query/how-can-i-use-google-big-query-to-query-json-data)