# How do I use Google Big Query to encrypt data?
// plain

Google BigQuery supports data encryption at rest, which means that data stored in BigQuery is encrypted using AES-256 encryption. To use encryption, you must create a customer-managed encryption key (CMEK) in Cloud Key Management Service (KMS).

The following example shows how to use the BigQuery API to create a CMEK and use it to encrypt a dataset:

```
# Create a CMEK in Cloud KMS
gcloud kms keys create --location global --keyring my-keyring --purpose encryption my-cmek

# Create a BigQuery dataset with the CMEK
bq --location=US mk --encryption_key projects/my-project/locations/global/keyRings/my-keyring/cryptoKeys/my-cmek my_dataset
```

The command above will create a CMEK in Cloud KMS and a dataset in BigQuery using the CMEK. All data stored in the dataset will be encrypted using the CMEK.

The following parts are used in the example code:

- `gcloud kms keys create`: Creates a CMEK in Cloud KMS.
- `--location global`: Specifies the location of the Cloud KMS key.
- `--keyring my-keyring`: Specifies the name of the Cloud KMS keyring.
- `--purpose encryption`: Specifies that the key will be used for encryption.
- `my-cmek`: Specifies the name of the CMEK.
- `bq --location=US mk`: Creates a BigQuery dataset.
- `--encryption_key projects/my-project/locations/global/keyRings/my-keyring/cryptoKeys/my-cmek`: Specifies the CMEK that will be used to encrypt the dataset.
- `my_dataset`: Specifies the name of the dataset.

For more information, see the [BigQuery Encryption at Rest documentation](https://cloud.google.com/bigquery/docs/encryption-at-rest) and the [Cloud KMS documentation](https://cloud.google.com/kms/docs/).

onelinerhub: [How do I use Google Big Query to encrypt data?](https://onelinerhub.com/google-big-query/how-do-i-use-google-big-query-to-encrypt-data)