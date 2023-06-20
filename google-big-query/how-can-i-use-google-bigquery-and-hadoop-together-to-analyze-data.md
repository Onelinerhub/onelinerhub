# How can I use Google BigQuery and Hadoop together to analyze data?
// plain

Google BigQuery and Hadoop can be used together to analyze data by using BigQuery to transfer data to Hadoop and then running analytics on the data. For example, you can use the following code to transfer data from BigQuery to Hadoop:

```
#!/bin/bash

# Use bq command line tool to export data from BigQuery
bq extract --destination_format=NEWLINE_DELIMITED_JSON <your_table> gs://<your_bucket>/<your_file>.json

# Use the hadoop fs command to move data from Google Cloud Storage to the Hadoop Distributed File System
hadoop fs -copyFromLocal gs://<your_bucket>/<your_file>.json <your_file>.json

# Use hadoop streaming to run analytics on the data
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -file <your_mapper>.py -mapper <your_mapper>.py -file <your_reducer>.py -reducer <your_reducer>.py -input <your_file>.json -output <your_output>
```

## Code explanation

- `bq extract`: exports data from BigQuery
- `hadoop fs`: moves data from Google Cloud Storage to the Hadoop Distributed File System
- `hadoop streaming`: runs analytics on the data

## Helpful links
- [Google BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- [Hadoop Documentation](https://hadoop.apache.org/docs/stable/index.html)

onelinerhub: [How can I use Google BigQuery and Hadoop together to analyze data?](https://onelinerhub.com/google-big-query/how-can-i-use-google-bigquery-and-hadoop-together-to-analyze-data)