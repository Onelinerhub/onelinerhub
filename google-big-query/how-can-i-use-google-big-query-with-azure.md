# How can I use Google Big Query with Azure?
// plain

Google BigQuery can be used with Azure in two ways:
1. Using Azure Data Factory. Data Factory is an Azure service that allows you to orchestrate and automate data movement and transformation. It can be used to move data from Google BigQuery to Azure data stores, such as Azure SQL Database or Azure Data Lake Store.

2. Using Azure Databricks. Databricks is an Apache Spark-based analytics platform that can be used to analyze data stored in Google BigQuery.

An example of how to use Azure Data Factory to move data from Google BigQuery to Azure SQL Database is shown below:

```
#Create a pipeline in Data Factory
az datafactory pipeline create --name mypipeline --resource-group myresourcegroup

#Add a copy activity to the pipeline
az datafactory activity copy create --name mycopyactivity --pipeline-name mypipeline \
  --resource-group myresourcegroup \
  --source-type GoogleBigQuery \
  --sink-type SqlDWSink \
  --sink-sql-connection-string "<Azure SQL Database connection string>"

#Run the pipeline
az datafactory pipeline run --name mypipeline --resource-group myresourcegroup
```

This will copy the data from Google BigQuery to Azure SQL Database.

## Helpful links
- [Azure Data Factory](https://azure.microsoft.com/en-us/services/data-factory/)
- [Azure Databricks](https://azure.microsoft.com/en-us/services/databricks/)

onelinerhub: [How can I use Google Big Query with Azure?](https://onelinerhub.com/google-big-query/how-can-i-use-google-big-query-with-azure)