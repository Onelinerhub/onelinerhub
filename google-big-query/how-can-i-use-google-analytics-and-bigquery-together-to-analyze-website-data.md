# How can I use Google Analytics and BigQuery together to analyze website data?
// plain

Google Analytics and BigQuery can be used together to analyze website data in a few different ways.

First, you can export the Google Analytics data to BigQuery and then use SQL queries to analyze the data. For example, the following query will return the total number of pageviews for a website in the last 30 days:

```
SELECT
  date,
  SUM(totals.pageviews) AS pageviews
FROM
  `ga_sessions_*`
WHERE
  _TABLE_SUFFIX BETWEEN FORMAT_DATE('%Y%m%d',DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY))
  AND FORMAT_DATE('%Y%m%d',CURRENT_DATE())
GROUP BY
  date
ORDER BY
  date ASC
```

## Output example

```
date        pageviews
2020-05-01  15000
2020-05-02  16000
2020-05-03  17000
2020-05-04  18000
...
```

Second, you can use BigQuery to create custom metrics and dimensions in Google Analytics. For example, the following query will create a custom metric that calculates the average pageviews per session:

```
SELECT
  date,
  AVG(totals.pageviews) AS avg_pageviews_per_session
FROM
  `ga_sessions_*`
GROUP BY
  date
ORDER BY
  date ASC
```

Once the custom metric is created, it can be used in Google Analytics to analyze the data.

- Export Google Analytics data to BigQuery: [Link](https://support.google.com/analytics/answer/3416091?hl=en)
- Create custom metrics and dimensions in Google Analytics with BigQuery: [Link](https://support.google.com/analytics/answer/3416092?hl=en)

onelinerhub: [How can I use Google Analytics and BigQuery together to analyze website data?](https://onelinerhub.com/google-big-query/how-can-i-use-google-analytics-and-bigquery-together-to-analyze-website-data)