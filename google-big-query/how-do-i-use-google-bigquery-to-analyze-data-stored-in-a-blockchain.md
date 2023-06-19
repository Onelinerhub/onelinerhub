# How do I use Google BigQuery to analyze data stored in a blockchain?
// plain

Google BigQuery is a powerful tool for analyzing data stored in a blockchain. It allows users to query the data stored in the blockchain in order to gain insights and uncover trends.

Example code using BigQuery to analyze data stored in a blockchain:

```
SELECT *
FROM `bigquery-public-data.crypto_bitcoin.transactions`
WHERE block_timestamp > '2020-01-01'
```

This code will query the Bitcoin blockchain and return all transactions that occurred after January 1, 2020.

## Code explanation


- `SELECT *`: This is the command to select all columns from the table.
- `FROM `bigquery-public-data.crypto_bitcoin.transactions`: This is the table to query.
- `WHERE block_timestamp > '2020-01-01'`: This is the condition to filter the results, only returning transactions that occurred after January 1, 2020.

## Helpful links

- [Google BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- [Bitcoin Blockchain on BigQuery](https://cloud.google.com/bigquery/public-data/crypto-bitcoin)

onelinerhub: [How do I use Google BigQuery to analyze data stored in a blockchain?](https://onelinerhub.com/google-big-query/how-do-i-use-google-bigquery-to-analyze-data-stored-in-a-blockchain)