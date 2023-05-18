# How to create a realtime index in SphinxSearch?
// plain

SphinxSearch supports realtime indexing, which allows for indexing and searching of data in realtime. To create a realtime index, you need to use the `indexer` command with the `--rotate` option.

```
indexer --rotate --config /etc/sphinxsearch/sphinx.conf
```

The `--rotate` option tells the indexer to rotate the index, which is necessary for realtime indexing. The `--config` option specifies the configuration file to use.

## Code explanation


- `indexer`: The command used to create the index.
- `--rotate`: The option used to rotate the index.
- `--config`: The option used to specify the configuration file.

## Helpful links

- [SphinxSearch Documentation](http://sphinxsearch.com/docs/current.html)
- [Realtime Indexing](http://sphinxsearch.com/docs/current.html#realtime-indexing)

onelinerhub: [How to create a realtime index in SphinxSearch?](https://onelinerhub.com/sphinx-search/how-to-create-a-realtime-index-in-sphinxsearch)