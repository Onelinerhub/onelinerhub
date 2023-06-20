# How do I use a JSON service account with Google Big Query?
// plain

1. To use a JSON service account with Google Big Query, you need to create a service account and download its JSON key file.
2. After creating the service account, you must grant the service account the necessary permissions to access Big Query.
3. To authenticate with Big Query, you must set the environment variable `GOOGLE_APPLICATION_CREDENTIALS` to the path of the JSON key file.
4. You can then use the `bigquery` library in Python to authenticate with Big Query. For example:
```
from google.cloud import bigquery

client = bigquery.Client.from_service_account_json('path/to/service_account.json')
```
5. After authenticating with Big Query, you can use the client object to run queries and other operations. For example:
```
query_job = client.query("SELECT * FROM `bigquery-public-data.usa_names.usa_1910_2013` LIMIT 10")
results = query_job.result()

for row in results:
    print(row)
```
## Output example

```
Row(('Mary', 1910, 0.07248475199092562), {'name': 0, 'year': 1, 'number': 2})
Row(('Anna', 1910, 0.02637829011019772), {'name': 0, 'year': 1, 'number': 2})
Row(('Emma', 1910, 0.02512562814070352), {'name': 0, 'year': 1, 'number': 2})
Row(('Elizabeth', 1910, 0.023852320675105485), {'name': 0, 'year': 1, 'number': 2})
Row(('Minnie', 1910, 0.012989623885918001), {'name': 0, 'year': 1, 'number': 2})
Row(('Margaret', 1910, 0.012924851757187394), {'name': 0, 'year': 1, 'number': 2})
Row(('Ida', 1910, 0.012705821783236776), {'name': 0, 'year': 1, 'number': 2})
Row(('Alice', 1910, 0.009608037617924537), {'name': 0, 'year': 1, 'number': 2})
Row(('Bertha', 1910, 0.009142418793820666), {'name': 0, 'year': 1, 'number': 2})
Row(('Sarah', 1910, 0.008930357142857142), {'name': 0, 'year': 1, 'number': 2})
```

6. You can also use the `bq` command-line tool to authenticate with Big Query. For example:
```
bq --location=US --key_file=path/to/service_account.json mk my_dataset
```
7. For more information, see the [BigQuery authentication documentation](https://cloud.google.com/bigquery/docs/authentication) and the [BigQuery Python Client Library documentation](https://googleapis.dev/python/bigquery/latest/index.html).

onelinerhub: [How do I use a JSON service account with Google Big Query?](https://onelinerhub.com/google-big-query/how-do-i-use-a-json-service-account-with-google-big-query)