# How do I use Google Big Query with Excel?
// plain

Using Google BigQuery with Excel is relatively straightforward. To get started, you'll need to install the Google BigQuery Excel Add-In, which can be found [here](https://developers.google.com/bigquery/docs/excel-add-in). Once installed, open Excel and you should see a new tab called "BigQuery" appear.

To connect to BigQuery, you'll need to authenticate with your Google account. To do this, click the "Connect" button on the BigQuery tab. You'll be prompted to log in with your Google account. Once you've logged in, you can start running queries directly from Excel.

For example, to query the public dataset `bigquery-public-data.usa_names.usa_1910_2013`, you could enter the following query into the "Query" box:

```
SELECT name, count
FROM `bigquery-public-data.usa_names.usa_1910_2013`
WHERE gender = 'M'
LIMIT 10
```

The resulting output would look like this:

```
name	count
John	9655
William	9532
James	5927
George	4454
Charles	4395
Robert	4261
Joseph	2657
Frank	2146
Edward	2090
Thomas	2060
```

The query statement consists of the following parts:

* `SELECT` - this specifies the columns from the dataset that you want to return in the result.
* `FROM` - this specifies the dataset from which you want to retrieve the data.
* `WHERE` - this is an optional clause that allows you to filter the data based on certain criteria.
* `LIMIT` - this is an optional clause that allows you to limit the number of results returned.

Once you have the results of your query, you can use Excel's built-in features to analyze and visualize the data.

For more information on using BigQuery with Excel, please refer to the [BigQuery documentation](https://developers.google.com/bigquery/docs/excel-add-in).

onelinerhub: [How do I use Google Big Query with Excel?](https://onelinerhub.com/google-big-query/how-do-i-use-google-big-query-with-excel)