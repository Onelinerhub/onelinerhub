# How to create a delta index in SphinxSearch?
// plain

Creating a delta index in SphinxSearch is a two-step process.

1. Create a main index and a delta index.

```
index main
{
    type = plain
    path = /var/data/main
}

index delta
{
    type = delta
    path = /var/data/delta
    # main index to which delta index will be merged
    # after indexing
    # mandatory
    main = main
}
```

2. Merge the delta index with the main index.

```
indexer --merge main delta --merge-dst-range deleted 0 0
```

The `--merge` option tells Sphinx to merge the delta index with the main index. The `--merge-dst-range` option tells Sphinx to mark all documents in the delta index as deleted in the main index.

## Helpful links

- [SphinxSearch Documentation](http://sphinxsearch.com/docs/current.html)
- [Creating a Delta Index](http://sphinxsearch.com/docs/current.html#conf-index-delta)

onelinerhub: [How to create a delta index in SphinxSearch?](https://onelinerhub.com/sphinx-search/how-to-create-a-delta-index-in-sphinxsearch)