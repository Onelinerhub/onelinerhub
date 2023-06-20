# How do I start using Google Big Query?
// plain

1. First, create a Google Cloud Platform account and enable BigQuery. You can do this by going to the [Google Cloud Platform Console](https://console.cloud.google.com/).

2. Once you have your account created, you can go to the [BigQuery Console](https://console.cloud.google.com/bigquery) and start querying your data.

3. To query data, you can use the standard SQL syntax. For example, you can use the following query to select all the records from a table called "users":
```
SELECT * FROM `project.dataset.users`;
```

4. If you want to save the query results, you can use the `--destination_table` flag. For example, to save the results of the above query to a table called "users_copy":
```
SELECT * FROM `project.dataset.users`
--destination_table project.dataset.users_copy;
```

5. You can also use the BigQuery API to programmatically interact with BigQuery. The API supports a variety of languages, including Python, Node.js, Java, and Go.

6. To get started with the BigQuery API, you can use the [Quickstart guide](https://cloud.google.com/bigquery/docs/quickstarts).

7. For more information about BigQuery, you can check out the [BigQuery Documentation](https://cloud.google.com/bigquery/docs/).

onelinerhub: [How do I start using Google Big Query?](https://onelinerhub.com/google-big-query/how-do-i-start-using-google-big-query)