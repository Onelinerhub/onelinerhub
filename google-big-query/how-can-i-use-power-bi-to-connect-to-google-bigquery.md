# How can I use Power BI to connect to Google BigQuery?
// plain

Power BI can be used to connect to Google BigQuery by using the Google BigQuery connector. To use the connector, you will need to first create a project in the Google Cloud Platform and then create a service account with the necessary permissions to access BigQuery.

Once the service account is created, you will need to generate a JSON key file for the service account. This key file can then be used to authenticate the connection between Power BI and BigQuery.

Example code to connect to BigQuery using the Google BigQuery connector:

```
let
    Source = GoogleBigQuery.Database("project-id"),
    #"project-id" = "my-project-id"
in
    Source
```

## Code explanation

1. `let` - This is a keyword which introduces the code block.
2. `Source` - This is the name of the data source which will be connected to BigQuery.
3. `GoogleBigQuery.Database` - This is the connector which will be used to connect to BigQuery.
4. `project-id` - This is the ID of the project in Google Cloud Platform.

## Helpful links
1. [Google BigQuery Connector in Power BI](https://docs.microsoft.com/en-us/power-bi/connect-data/desktop-google-bigquery)
2. [Google Cloud Platform Documentation](https://cloud.google.com/docs/)

onelinerhub: [How can I use Power BI to connect to Google BigQuery?](https://onelinerhub.com/google-big-query/how-can-i-use-power-bi-to-connect-to-google-bigquery)