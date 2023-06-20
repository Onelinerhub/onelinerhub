# How can I use Google BigQuery and Looker together to analyze data?
// plain

Google BigQuery and Looker are two powerful tools that can be used together to analyze data. BigQuery is a cloud-based data warehouse that allows you to store and query large datasets, while Looker is a data analytics platform that allows you to connect to BigQuery and explore your data.

Here is an example of how to use the two tools together:

1. Create a BigQuery dataset and upload your data.
2. Connect Looker to BigQuery by adding your BigQuery project ID and credentials to the Looker connection.
3. Create LookML models in Looker to explore the data in BigQuery.

```
SELECT *
FROM dataset.table
WHERE category = 'sales'
```

This example query will return all records from the table in the dataset where the category is set to 'sales'.

## Helpful links
- [Google BigQuery](https://cloud.google.com/bigquery)
- [Looker](https://looker.com/)

onelinerhub: [How can I use Google BigQuery and Looker together to analyze data?](https://onelinerhub.com/google-big-query/how-can-i-use-google-bigquery-and-looker-together-to-analyze-data)