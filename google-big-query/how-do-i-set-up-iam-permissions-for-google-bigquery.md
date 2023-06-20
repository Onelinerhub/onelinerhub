# How do I set up IAM permissions for Google BigQuery?
// plain

To set up IAM permissions for Google BigQuery, you first need to create a service account and grant it the necessary permissions.

1. Create a service account in the [Google Cloud Console](https://console.cloud.google.com/iam-admin/serviceaccounts).

2. Grant the service account the necessary IAM roles for BigQuery. For example, to grant a service account the BigQuery Data Viewer role, use the following command:

```
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member serviceAccount:SERVICE_ACCOUNT_EMAIL --role roles/bigquery.dataViewer
```

3. For each dataset, grant the service account the necessary BigQuery permissions. For example, to grant a service account the BigQuery Data Viewer role for a dataset, use the following command:

```
bq show --format=prettyjson --transfer_config PROJECT_ID:DATASET
```

The output should look like this:

```
{
  "destinationDataset": {
    "datasetId": "DATASET_ID",
    "projectId": "PROJECT_ID"
  },
  "name": "projects/PROJECT_ID/locations/US/transferConfigs/DATASET",
  "params": {
    "destination_dataset_id": "DATASET_ID"
  },
  "schedule": "every 24 hours",
  "state": "ENABLED",
  "updateTime": "2020-03-06T18:39:00.902Z"
}
```

4. Add the service account to the dataset's access list with the following command:

```
bq update --transfer_config PROJECT_ID:DATASET \
  --access_filter="(role:READER AND serviceAccount:SERVICE_ACCOUNT_EMAIL)"
```

5. Verify that the service account is added to the dataset's access list with the following command:

```
bq show --format=prettyjson --transfer_config PROJECT_ID:DATASET
```

The output should look like this:

```
{
  "destinationDataset": {
    "datasetId": "DATASET_ID",
    "projectId": "PROJECT_ID"
  },
  "name": "projects/PROJECT_ID/locations/US/transferConfigs/DATASET",
  "params": {
    "destination_dataset_id": "DATASET_ID"
  },
  "schedule": "every 24 hours",
  "state": "ENABLED",
  "updateTime": "2020-03-06T18:39:00.902Z",
  "access": [
    {
      "role": "READER",
      "serviceAccount": "SERVICE_ACCOUNT_EMAIL"
    }
  ]
}
```

The service account now has the necessary permissions to access the BigQuery dataset.

onelinerhub: [How do I set up IAM permissions for Google BigQuery?](https://onelinerhub.com/google-big-query/how-do-i-set-up-iam-permissions-for-google-bigquery)