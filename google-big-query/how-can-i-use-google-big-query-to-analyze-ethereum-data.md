# How can I use Google Big Query to analyze Ethereum data?
// plain

Google Big Query allows you to analyze Ethereum data. You can use Big Query to query and analyze Ethereum transactions, blocks, and logs. The following is an example of a query that retrieves the first 10 blocks from the Ethereum Mainnet.

```
SELECT *
FROM `bigquery-public-data.crypto_ethereum.blocks`
ORDER BY number
LIMIT 10
```

The output of this query is a table with the following fields:

- `number`: The block number
- `hash`: The block hash
- `parent_hash`: The hash of the parent block
- `nonce`: The nonce of the block
- `sha3_uncles`: The SHA3 of the uncles in the block
- `logs_bloom`: The bloom filter for the logs of the block
- `transactions_root`: The root of the transactions trie of the block
- `state_root`: The root of the state trie of the block
- `miner`: The address of the miner of the block
- `difficulty`: The difficulty of the block
- `total_difficulty`: The total difficulty of the block
- `size`: The size of the block
- `extra_data`: The extra data of the block
- `gas_limit`: The gas limit of the block
- `gas_used`: The gas used by the block
- `timestamp`: The timestamp of the block

You can use Big Query to analyze Ethereum data in more detail by combining the `blocks` table with other tables in the `crypto_ethereum` dataset. For example, you can join the `blocks` table with the `transactions` table to retrieve all the transactions in a given block.

## Helpful links

- [Google Big Query Documentation](https://cloud.google.com/bigquery/docs)
- [Crypto Ethereum Dataset Documentation](https://cloud.google.com/bigquery/public-data/crypto-ethereum)

onelinerhub: [How can I use Google Big Query to analyze Ethereum data?](https://onelinerhub.com/google-big-query/how-can-i-use-google-big-query-to-analyze-ethereum-data)