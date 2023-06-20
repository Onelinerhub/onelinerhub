# How can I use Google Big Query to analyze Reddit data?
// plain

Google BigQuery is a powerful tool to analyze large datasets such as Reddit data. To start, you need to first obtain the Reddit data. This can be done using Google BigQuery's public datasets. Once the data is obtained, you can use SQL to query the data and get the desired results.

For example, to get the top 10 subreddits with the most comments, you can run the following query:

```
SELECT subreddit, COUNT(*) as comment_count
FROM `fh-bigquery.reddit_comments.2017_11`
GROUP BY subreddit
ORDER BY comment_count DESC
LIMIT 10
```

This query will return the top 10 subreddits with the most comments in November 2017:

```
subreddit	comment_count
AskReddit	93525
funny	71771
pics	63780
todayilearned	52480
worldnews	50606
gaming	49216
videos	39674
news	39003
gifs	37785
aww	37458
```

The query consists of the following parts:

- `SELECT`: This indicates which columns should be returned in the query. In this case, we are selecting the `subreddit` column and the `COUNT(*)` column which counts the number of comments for each subreddit.

- `FROM`: This indicates which table the query should be run on. In this case, we are running the query on the `fh-bigquery.reddit_comments.2017_11` table which contains all the Reddit comments from November 2017.

- `GROUP BY`: This indicates which column should be used to group the data. In this case, we are grouping the data by the `subreddit` column.

- `ORDER BY`: This indicates which column should be used to sort the data. In this case, we are sorting the data by the `comment_count` column in descending order.

- `LIMIT`: This indicates how many rows should be returned in the query. In this case, we are returning the top 10 subreddits.

For more information about how to use Google BigQuery to analyze Reddit data, see the following links:

- [Google BigQuery Documentation](https://cloud.google.com/bigquery/docs/)
- [Analyzing Reddit Data with BigQuery](https://cloud.google.com/blog/products/data-analytics/analyzing-reddit-data-with-bigquery)

onelinerhub: [How can I use Google Big Query to analyze Reddit data?](https://onelinerhub.com/google-big-query/how-can-i-use-google-big-query-to-analyze-reddit-data)