# How can I use Google Big Query to analyze data from the GDELT project?
// plain

Google BigQuery is a powerful tool for analyzing large datasets. It can be used to analyze data from the GDELT project, which is a global database of news and events.

To use BigQuery to analyze GDELT data, you first need to create a dataset and load the GDELT data into it. This can be done using the BigQuery web UI or the command line.

Once the data is loaded, you can use SQL queries to analyze it. For example, the following query will count the number of events that occurred in the United States in 2019:
```
SELECT COUNT(*)
FROM `gdelt-bq.gdeltv2.events`
WHERE Actor1CountryCode = 'US'
AND Year = 2019
```
The output of this query would be the number of events that occurred in the United States in 2019.

You can also use BigQuery to join GDELT data with other datasets. For example, the following query will join GDELT data with the World Bank population data to find the number of events that occurred in countries with a population of more than 10 million:
```
SELECT COUNT(*)
FROM `gdelt-bq.gdeltv2.events` AS g
JOIN `bigquery-public-data.world_bank_intl_education.country_series` AS w
ON g.Actor1CountryCode = w.country_code
WHERE w.population > 10000000
```

The output of this query would be the number of events that occurred in countries with a population of more than 10 million.

For more information on using BigQuery to analyze GDELT data, see the [GDELT BigQuery Documentation](https://blog.gdeltproject.org/gdelt-bigquery-documentation/).

onelinerhub: [How can I use Google Big Query to analyze data from the GDELT project?](https://onelinerhub.com/google-big-query/how-can-i-use-google-big-query-to-analyze-data-from-the-gdelt-project)