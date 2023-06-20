# How can I use Google Big Query with Mulesoft?
// plain

Google BigQuery can be used with Mulesoft to easily access and analyze large datasets. To do this, you will need to use the BigQuery Connector provided by MuleSoft. The connector enables you to:
- Perform queries
- Retrieve data from BigQuery tables
- Insert data into BigQuery tables
- Stream data into BigQuery tables

## Example code

```
<bigquery:query config-ref="BigQuery_Configuration"
    query="SELECT * FROM [myproject:mydataset.mytable]
    WHERE mycolumn = 'myvalue'"/>
```

This example code will perform a query on the table `mytable` within the dataset `mydataset` in the project `myproject`, and will return all the records whose `mycolumn` value is `myvalue`.

You can find more information about the BigQuery Connector and how to use it in the [MuleSoft Documentation](https://docs.mulesoft.com/connectors/bigquery/bigquery-connector).

onelinerhub: [How can I use Google Big Query with Mulesoft?](https://onelinerhub.com/google-big-query/how-can-i-use-google-big-query-with-mulesoft)