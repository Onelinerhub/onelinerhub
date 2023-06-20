# How can I use Google Big Query with MicroStrategy?
// plain

Google Big Query (GBQ) is a powerful cloud-based data warehouse service that can be used to store, query, analyze, and visualize large datasets. MicroStrategy is a business intelligence platform that provides data visualization, reporting, and analytics capabilities.

Using GBQ with MicroStrategy allows users to access and analyze large datasets stored in GBQ from within the MicroStrategy platform. This provides users with a powerful combination of data storage and analysis capabilities.

To use GBQ with MicroStrategy, you need to configure the connection between the two platforms. This can be done by using the MicroStrategy Connector for Google Big Query, which is available as a free download from the Google Cloud Platform website. Once the connector is installed, you can configure the connection by entering the credentials for your Google Cloud Platform account.

Once the connection is configured, you can use the MicroStrategy platform to query and analyze data stored in GBQ. For example, the following code block shows how to query the GBQ table `my_table` and display the results in a chart:

```
SELECT *
FROM my_table
WHERE year = 2020
ORDER BY month
```

The above query will return a table of data with the month and year columns sorted in ascending order. This data can then be used to create a chart in MicroStrategy.

Overall, using GBQ with MicroStrategy provides users with a powerful combination of data storage and analysis capabilities. It can be used to query and analyze large datasets stored in GBQ and visualize the results in charts and reports.

## Helpful links
- [Google Cloud Platform website](https://cloud.google.com/)
- [MicroStrategy Connector for Google Big Query](https://www.microstrategy.com/products/connectors/google-bigquery)

onelinerhub: [How can I use Google Big Query with MicroStrategy?](https://onelinerhub.com/google-big-query/how-can-i-use-google-big-query-with-microstrategy)