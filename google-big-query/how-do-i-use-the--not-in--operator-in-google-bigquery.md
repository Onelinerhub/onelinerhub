# How do I use the "not in" operator in Google BigQuery?
// plain

The "not in" operator is used in Google BigQuery to filter out results that don't match a certain criteria. It works by excluding results that appear in a specified list.

For example, the following code block will return all the books from the `bigquery-public-data.hacker_news.stories` table that are not written by authors with the names "Paul Graham", "Robert C. Martin" and "Steve McConnell":

```
SELECT title
FROM `bigquery-public-data.hacker_news.stories`
WHERE author NOT IN ("Paul Graham", "Robert C. Martin", "Steve McConnell")
```

The code block consists of the following parts:

* `SELECT title`: This part specifies the columns from the table that should be returned.
* `FROM `bigquery-public-data.hacker_news.stories`: This part specifies the table to query from.
* `WHERE author NOT IN ("Paul Graham", "Robert C. Martin", "Steve McConnell")`: This part specifies the criteria for the query. It excludes all results that match any of the names in the list.

For more information about the "not in" operator, see the [BigQuery documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators#not_in).

onelinerhub: [How do I use the "not in" operator in Google BigQuery?](https://onelinerhub.com/google-big-query/how-do-i-use-the--not-in--operator-in-google-bigquery)