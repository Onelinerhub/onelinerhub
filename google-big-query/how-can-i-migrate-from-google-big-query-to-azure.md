# How can I migrate from Google Big Query to Azure?
// plain

Migrating from Google Big Query to Azure is relatively straightforward, and can be done in a few simple steps.

1. Export your Big Query data to a Google Cloud Storage bucket in CSV format.

```
bq extract --destination_format=CSV mydataset.mytable gs://mybucket/mytable.csv
```

2. Create an Azure Blob Storage account, and upload the CSV file to the new account.

3. Create a new Azure SQL Database, and create a new table to store the data from the CSV file.

4. Use the Bulk Copy Program (BCP) to copy the data from the CSV file into the new table.

```
bcp mytable in mytable.csv -S servername -d mydatabase -U username -P password -c
```

5. Query the new table to verify that the data has been successfully migrated.

You can find more information about migrating from Google Big Query to Azure in the [Azure documentation](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-migrate-from-bigquery).

onelinerhub: [How can I migrate from Google Big Query to Azure?](https://onelinerhub.com/google-big-query/how-can-i-migrate-from-google-big-query-to-azure)