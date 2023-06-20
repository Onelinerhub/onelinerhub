# How do I find the Google BigQuery project ID?
// plain

Finding the Google BigQuery project ID is easy.

1. Log into the [Google Cloud Platform Console](https://console.cloud.google.com/).

2. In the left-hand menu, select **BigQuery**.

3. In the top-left corner, the project ID should be visible.

Alternatively, you can also use the `bq` command-line tool to find the project ID.

```
$ bq ls
Dataset                  Id
------------------------ -------------------------------
sample_dataset            my_project_id:sample_dataset
```

In the output of the `bq ls` command, the project ID is the first part of the dataset ID (`my_project_id` in the example above).

You can also retrieve the project ID programmatically using the [BigQuery client libraries](https://cloud.google.com/bigquery/docs/reference/libraries).

For example, in Python:

```python
from google.cloud import bigquery

client = bigquery.Client()
print(client.project)
```

```
my_project_id
```

onelinerhub: [How do I find the Google BigQuery project ID?](https://onelinerhub.com/google-big-query/how-do-i-find-the-google-bigquery-project-id)