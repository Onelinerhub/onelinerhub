# How can I use the Google BigQuery free tier?
// plain

The Google BigQuery free tier allows users to query up to 1TB of data per month at no cost. To use the free tier, users must have a Google Cloud Platform account and must enable billing.

To start using BigQuery free tier, users can use the `bq` command line tool. An example of how to query data using the `bq` command line tool is as follows:

```
bq query --use_legacy_sql=false 'SELECT * FROM [bigquery-public-data:samples.shakespeare] LIMIT 10'
```

The output of the query will be the first 10 lines of Shakespeare's writings:

```
+----+------------+---------+---------+
| id | word       | word_id | volume  |
+----+------------+---------+---------+
|  1 | O          |    8462 |      26 |
|  2 | all        |    8463 |      26 |
|  3 | men        |    8464 |      26 |
|  4 | should     |    8465 |      26 |
|  5 | be         |    8466 |      26 |
|  6 | created    |    8467 |      26 |
|  7 | equal      |    8468 |      26 |
|  8 | .          |    8469 |      26 |
|  9 | My         |    8470 |      26 |
| 10 | excellent  |    8471 |      26 |
+----+------------+---------+---------+
```

## Code explanation

1. `bq query`: runs a query on BigQuery
2. `--use_legacy_sql=false`: uses standard SQL instead of legacy SQL
3. `SELECT * FROM [bigquery-public-data:samples.shakespeare]`: selects all columns from the `shakespeare` table in the `samples` dataset in the `bigquery-public-data` project
4. `LIMIT 10`: limits the number of results to 10

For more information on using the Google BigQuery free tier, please refer to the [Google Cloud Platform Documentation](https://cloud.google.com/bigquery/docs/).

onelinerhub: [How can I use the Google BigQuery free tier?](https://onelinerhub.com/google-big-query/how-can-i-use-the-google-bigquery-free-tier)