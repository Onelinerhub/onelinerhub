# How can I use Knime to connect to Google BigQuery?
// plain

Knime can be used to connect to Google BigQuery using the Google BigQuery Connector node. This connector node can be found in the Big Data Connectors section of the node repository.

The Google BigQuery Connector node can be used to read from and write to BigQuery tables. To use the node, a Google Cloud Platform project must be created and configured with the proper credentials.

## Example code

```
# create a Google BigQuery Connector node
node = KNIME.createNode('org.knime.bigdata.connector.gcp.bigquery.BigQueryConnectorNodeFactory');

# set the Google Cloud Platform project ID
node.setProjectId('[PROJECT_ID]');

# set the BigQuery table name
node.setTableName('[TABLE_NAME]');
```

The Google BigQuery Connector node also allows for the configuration of other BigQuery parameters, such as the query, the query type, the query parameters, the query result type, the query result limit, and the query result timeout.

The output of the node is a table that contains the query result.

## Helpful links
- [Google BigQuery Connector Node](https://www.knime.com/node/bigdata/connector/gcp/bigquery)
- [Google BigQuery Documentation](https://cloud.google.com/bigquery/docs)

onelinerhub: [How can I use Knime to connect to Google BigQuery?](https://onelinerhub.com/google-big-query/how-can-i-use-knime-to-connect-to-google-bigquery)