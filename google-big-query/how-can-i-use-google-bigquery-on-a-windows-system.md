# How can I use Google BigQuery on a Windows system?
// plain

Google BigQuery is a serverless, highly scalable, and cost-effective cloud data warehouse. It can be used on a Windows system by following the steps below:

1. Download and install the Google Cloud SDK for Windows from [here](https://cloud.google.com/sdk/docs/quickstart-windows).

2. Open a command prompt and enter the following command to install the BigQuery command-line tool:
```
gcloud components install bq
```
3. Initialize the gcloud environment by running the following command:
```
gcloud init
```
4. Create a BigQuery dataset by running the following command:
```
bq mk mydataset
```
5. Upload a CSV file to the dataset using the following command:
```
bq load --source_format=CSV mydataset.mytable gs://mybucket/mydata.csv myschema.json
```
6. Run a query on the dataset using the following command:
```
bq query --use_legacy_sql=false 'SELECT * FROM mydataset.mytable'
```
7. You can view the query results by running the following command:
```
bq view --format=prettyjson mydataset.mytable
```

The output of the above command will be a JSON representation of the query results.

onelinerhub: [How can I use Google BigQuery on a Windows system?](https://onelinerhub.com/google-big-query/how-can-i-use-google-bigquery-on-a-windows-system)