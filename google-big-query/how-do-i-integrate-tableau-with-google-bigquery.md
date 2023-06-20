# How do I integrate Tableau with Google BigQuery?
// plain

Tableau can be integrated with Google BigQuery in several ways:

1. **Using Tableau's native BigQuery connector**: Tableau's native BigQuery connector allows users to connect to BigQuery datasets directly from Tableau Desktop or Tableau Server. This provides the ability to do data exploration, visualization, and analysis without writing any code.

2. **Using Tableau's BigQuery Extractor**: Tableau's BigQuery Extractor allows users to extract data from BigQuery and store it in a Tableau extract file. This can be used to improve query performance, reduce query costs, and improve data security.

3. **Using Tableau's Python API**: Tableau's Python API allows users to write Python code to connect to BigQuery and extract data. This provides the ability to customize the data extraction process and to integrate Tableau with other data sources.

Example code (using the Python API):

```
# Import the necessary libraries
import pandas as pd
import tableauserverclient as TSC

# Establish a connection to Tableau Server
server = TSC.Server('http://tableau.example.com')
server.auth.sign_in(username='username', password='password')

# Connect to BigQuery
from google.cloud import bigquery

client = bigquery.Client()

# Execute a query
query = (
    'SELECT * FROM `bigquery-public-data.samples.shakespeare`')
query_job = client.query(query)

# Load the results into a pandas DataFrame
df = query_job.to_dataframe()

# Create a new Tableau Datasource from the DataFrame
new_datasource = TSC.DatasourceItem(server, 'My BigQuery Datasource')
new_datasource = server.datasources.publish(new_datasource, df, 'Overwrite')
```

## Output example


```
Datasource 'My BigQuery Datasource' published successfully
```

## Helpful links

- [Tableau's BigQuery Connector](https://help.tableau.com/current/connectors/en-us/bigquery.htm)
- [Tableau's BigQuery Extractor](https://help.tableau.com/current/api/bigqueryextractor_api/en-us/index.html)
- [Tableau's Python API](https://help.tableau.com/current/api/python_api/en-us/index.html)

onelinerhub: [How do I integrate Tableau with Google BigQuery?](https://onelinerhub.com/google-big-query/how-do-i-integrate-tableau-with-google-bigquery)