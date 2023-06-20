# How do I create and use Google BigQuery datasets?
// plain

Creating and using Google BigQuery datasets is a simple process.

1. First, create a project in the [Google Cloud Console](https://console.cloud.google.com/).

2. Then, in the BigQuery section, create a new dataset.

3. You can now upload or stream data into the dataset. For example, to upload a CSV file, you can use the following code:

```
# Standard SQL
CREATE OR REPLACE TABLE your_dataset.your_table

# Legacy SQL
CREATE TABLE your_dataset.your_table

# Uploading the CSV
WITH data AS (
  SELECT * FROM
    CSV_LOAD('gs://your_bucket/your_file.csv',
            FORMAT='CSV',
            AUTODETECT=TRUE)
)
INSERT INTO your_dataset.your_table
SELECT * FROM data
```

4. Once the data is uploaded, you can query it using Standard SQL or Legacy SQL.

5. You can also export the data in CSV, JSON, or Avro formats. For example, to export a table in CSV format, you can use the following code:

```
# Standard SQL
SELECT * FROM your_dataset.your_table
  INTO OUTFILE 'gs://your_bucket/your_file.csv'
  FORMAT CSV

# Legacy SQL
SELECT * FROM your_dataset.your_table
  INTO OUTFILE 'gs://your_bucket/your_file.csv'
  FIELDS TERMINATED BY ','
  ENCLOSED BY '"'
  ESCAPED BY '\\'
  LINES TERMINATED BY '\n'
```

6. Finally, you can delete the dataset when you no longer need it.

7. For more information, you can refer to the [BigQuery documentation](https://cloud.google.com/bigquery/docs/).

onelinerhub: [How do I create and use Google BigQuery datasets?](https://onelinerhub.com/google-big-query/how-do-i-create-and-use-google-bigquery-datasets)