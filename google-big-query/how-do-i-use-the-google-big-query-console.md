# How do I use the Google Big Query Console?
// plain

### Using the Google BigQuery Console

Using the Google BigQuery Console is a great way to interact with your data. Here are the steps to get started:

1. Navigate to the [BigQuery Console](https://console.cloud.google.com/bigquery) and sign in with your Google Account.

2. Once you are signed in, you will see the list of datasets available to you. Select the dataset you would like to query.

3. Type the query into the query editor. For example:

```sql
SELECT * FROM `bigquery-public-data.usa_names.usa_1910_2013` WHERE name = 'John'
```

The above query will return all records from the USA Names dataset where the name is 'John'.

4. Click the 'Run Query' button to execute the query.

5. The query results will be displayed in the results panel.

6. You can save the query results by clicking the 'Save Results' button.

7. You can also save the query itself by clicking the 'Save Query' button.

For more information on using the BigQuery Console, please see the [BigQuery Documentation](https://cloud.google.com/bigquery/docs/).

onelinerhub: [How do I use the Google Big Query Console?](https://onelinerhub.com/google-big-query/how-do-i-use-the-google-big-query-console)