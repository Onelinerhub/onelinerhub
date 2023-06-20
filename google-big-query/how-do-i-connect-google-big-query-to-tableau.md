# How do I connect Google Big Query to Tableau?
// plain

Connecting Google Big Query to Tableau is straightforward and can be done in a few steps:

1. Install the Tableau Big Query connector from the Tableau website.
2. In Tableau, select the **Connect** option, then select **Big Query** from the list of connectors.
3. Enter your Google Big Query credentials to connect.
4. Once connected, select the dataset you would like to use and click **OK**.
5. Tableau will then display the data in the data source view.
6. Analyze and visualize the data using Tableau's features.
7. Publish your findings to Tableau Server or Tableau Online.

## Example code


```
# Install Tableau Big Query Connector
pip install tableau-bigquery-connector

# Connect to Big Query
from tableau_bigquery_connector import TableauBigQueryConnector

tbqc = TableauBigQueryConnector(
    project_id='example-project',
    credentials_path='/path/to/credentials.json'
)

# Retrieve data from Big Query
data = tbqc.get_data('SELECT * FROM `example-dataset.example-table`')

# Display data
print(data)
```

## Output example


```
[
  {
    'column1': 'value1',
    'column2': 'value2',
    'column3': 'value3'
  },
  {
    'column1': 'value4',
    'column2': 'value5',
    'column3': 'value6'
  },
  ...
]
```

## Helpful links

- [Tableau Big Query Connector Documentation](https://tableau-bigquery-connector.readthedocs.io/en/latest/)
- [Tableau Big Query Connector Github Repository](https://github.com/tableau/tableau-bigquery-connector)

onelinerhub: [How do I connect Google Big Query to Tableau?](https://onelinerhub.com/google-big-query/how-do-i-connect-google-big-query-to-tableau)