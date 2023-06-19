# How can I use Google BigQuery to access the Hacker News comments in the public data set?
// plain

Google BigQuery is a cloud-based data warehouse that allows users to store and query large datasets. It has a public dataset of Hacker News comments, which can be accessed using the following steps:

1. Create a BigQuery account if you don't have one already.
2. Log in to your BigQuery account and navigate to the [Hacker News public dataset](https://console.cloud.google.com/marketplace/details/the-psf/hacker-news).
3. Click on the "Select" button and then "Create dataset".
4. Enter the dataset name and click "Create dataset".
5. Once the dataset is created, click on the "Query Table" button to open the BigQuery query editor.
6. Enter the following query to view the Hacker News comments:

```
SELECT *
FROM `bigquery-public-data.hacker_news.comments`
LIMIT 10
```

This query will return the first 10 comments from the Hacker News comments table.

## Helpful links

- [BigQuery Documentation](https://cloud.google.com/bigquery/docs/)
- [Hacker News Public Dataset](https://console.cloud.google.com/marketplace/details/the-psf/hacker-news)

onelinerhub: [How can I use Google BigQuery to access the Hacker News comments in the public data set?](https://onelinerhub.com/google-big-query/how-can-i-use-google-bigquery-to-access-the-hacker-news-comments-in-the-public-data-set)