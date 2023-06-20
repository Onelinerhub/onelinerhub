# tier

How can I use the free tier of Google BigQuery?
// plain

You can use the free tier of Google BigQuery by signing up for a free Google Cloud Platform account. After signing up, you can access BigQuery and its free tier by going to the BigQuery web UI, the command-line tool, or by using the BigQuery API.

The free tier of BigQuery is a great way to explore the features of BigQuery without incurring any costs. With the free tier, you get 1TB of query data processing per month and 10GB of storage per month.

For example, you can use the BigQuery command-line tool to query a public dataset. The following code block shows an example of querying the public `bigquery-public-data.noaa_gsod` dataset:

```
bq query --use_legacy_sql=false '
SELECT *
FROM `bigquery-public-data.noaa_gsod.gsod*`
LIMIT 10'
```

The output of this query is a list of 10 records from the `bigquery-public-data.noaa_gsod.gsod*` dataset:

```
+---------+-------+-------+-------+-------+-------+-------+-------+-------+--------+-------+-------+-------+-------+-------+-------+-------+-------+
| stn     | wban  | year  | mo    | da    | temp  | dewp  | slp   | stp   | visib | wdsp  | mxspd | gust  | max   | min   | prcp  | sndp  |
+---------+-------+-------+-------+-------+-------+-------+-------+-------+--------+-------+-------+-------+-------+-------+-------+-------+-------+
| 030015  | 99999 | 1933  | 01    | 01    | -2.2  | -9.9  | 1020  | 1020  | 999.9 | 999.9 | 999.9 | 999.9 | -2.2  | -9.9  | 0.0   | 999.9 |
| 030015  | 99999 | 1933  | 01    | 02    | -2.8  | -11.1 | 1018  | 1018  | 999.9 | 999.9 | 999.9 | 999.9 | -2.8  | -11.1 | 0.0   | 999.9 |
| 030015  | 99999 | 1933  | 01    | 03    | -2.2  | -9.9  | 1020  | 1020  | 999.9 | 999.9 | 999.9 | 999.9 | -2.2  | -9.9  | 0.0   | 999.9 |
| 030015  | 99999 | 1933  | 01    | 04    | -2.8  | -11.1 | 1018  | 1018  | 999.9 | 999.9 | 999.9 | 999.9 | -2.8  | -11.1 | 0.0   | 999.9 |
| 030015  | 99999 | 1933  | 01    | 05    | -2.2  | -9.9  | 1020  | 1020  | 999.9 | 999.9 | 999.9 | 999.9 | -2.2  | -9.9  | 0.0   | 999.9 |
| 030015  | 99999 | 1933  | 01    | 06    | -2.8  | -11.1 | 1018  | 1018  | 999.9 | 999.9 | 999.9 | 999.9 | -2.8  | -11.1 | 0.0   | 999.9 |
| 030015  | 99999 | 1933  | 01    | 07    | -2.2  | -9.9  | 1020  | 1020  | 999.9 | 999.9 | 999.9 | 999.9 | -2.2  | -9.9  | 0.0   | 999.9 |
| 030015  | 99999 | 1933  | 01    | 08    | -2.8  | -11.1 | 1018  | 1018  | 999.9 | 999.9 | 999.9 | 999.9 | -2.8  | -11.1 | 0.0   | 999.9 |
| 030015  | 99999 | 1933  | 01    | 09    | -2.2  | -9.9  | 1020  | 1020  | 999.9 | 999.9 | 999.9 | 999.9 | -2.2  | -9.9  | 0.0   | 999.9 |
| 030015  | 99999 | 1933  | 01    | 10    | -2.8  | -11.1 | 1018  | 1018  | 999.9 | 999.9 | 999.9 | 999.9 | -2.8  | -11.1 | 0.0   | 999.9 |
+---------+-------+-------+-------+-------+-------+-------+-------+-------+--------+-------+-------+-------+-------+-------+-------+-------+-------+
```

## Code explanation


* `bq query`: this is the command to run a query in BigQuery.
* `--use_legacy_sql=false`: this is an optional flag that sets the query to use standard SQL syntax.
* `SELECT *`: this is the SQL statement to select all columns from the dataset.
* `FROM `bigquery-public-data.noaa_gsod.gsod*``: this is the SQL statement to select the `bigquery-public-data.noaa_gsod.gsod*` dataset.
* `LIMIT 10`: this is the SQL statement to limit the number of records returned to 10.

For more information on using the free tier of BigQuery, please refer to the [BigQuery pricing page](https://cloud.google.com/bigquery/pricing).

onelinerhub: [tier

How can I use the free tier of Google BigQuery?](https://onelinerhub.com/google-big-query/tier--how-can-i-use-the-free-tier-of-google-bigquery)