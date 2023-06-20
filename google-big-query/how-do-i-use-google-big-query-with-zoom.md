# How do I use Google Big Query with Zoom?
// plain

Google BigQuery is a powerful cloud-based data warehouse service that allows users to store and query large amounts of data. It can be used with Zoom to analyze user data, such as meeting attendance, duration, and participant demographics. To use BigQuery with Zoom, you will need to set up a connection between the two services.

1. Set up a Google Cloud Platform (GCP) project and enable the BigQuery API.
2. Create a BigQuery dataset for your Zoom data.
3. Generate a Zoom API key and secret.
4. Configure the Zoom API to allow access to your BigQuery dataset.
5. Use the BigQuery API to access your Zoom data and query it.

Example code block:
```
SELECT
  user_id,
  start_time,
  end_time
FROM
  `mydataset.mytable`
WHERE
  start_time > '2020-01-01'
  AND end_time < '2020-12-31'
```

## Output example

```
user_id  start_time    end_time
123      2020-02-01    2020-02-15
456      2020-04-01    2020-04-30
```

## Helpful links
- [Google Cloud Platform Documentation](https://cloud.google.com/docs)
- [Zoom API Documentation](https://marketplace.zoom.us/docs/api-reference/zoom-api)
- [BigQuery Documentation](https://cloud.google.com/bigquery/docs)

onelinerhub: [How do I use Google Big Query with Zoom?](https://onelinerhub.com/google-big-query/how-do-i-use-google-big-query-with-zoom)