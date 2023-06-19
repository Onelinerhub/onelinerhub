# How can I use Google BigQuery to analyze Bitcoin data?
// plain

Google BigQuery is a cloud-based data warehouse that allows users to analyze large datasets in a matter of seconds. It can be used to analyze Bitcoin data by querying the Bitcoin blockchain. The blockchain is stored in a public dataset on BigQuery, which can be accessed by anyone with a Google account.

To query the Bitcoin blockchain data, you can use the following example code:

```
SELECT block_timestamp, block_height, tx_hash
FROM `bigquery-public-data.bitcoin_blockchain.blocks`
LIMIT 10
```

This code will return the timestamp, block height, and transaction hash of the first 10 blocks in the blockchain.

The code consists of the following parts:
- `SELECT`: a keyword that specifies which columns to include in the query
- `block_timestamp`, `block_height`, `tx_hash`: the columns to include in the query
- `FROM`: a keyword that specifies the source of the data
- `bigquery-public-data.bitcoin_blockchain.blocks`: the public dataset on BigQuery that stores the Bitcoin blockchain
- `LIMIT 10`: a keyword that limits the number of results returned to 10

For more information on how to use BigQuery to analyze Bitcoin data, see the [BigQuery documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/bitcoin_blockchain).

onelinerhub: [How can I use Google BigQuery to analyze Bitcoin data?](https://onelinerhub.com/google-big-query/how-can-i-use-google-bigquery-to-analyze-bitcoin-data)