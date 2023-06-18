# How can I use SphinxSearch to rotate my index seamlessly?
// plain

SphinxSearch provides the ability to rotate your index seamlessly via its Delta-Indexing feature. Delta-Indexing allows you to create a new index from the changes in your source data, without having to re-index the entire dataset. This allows you to keep your search index up-to-date without having to take your search engine offline.

Here is an example of how to use Delta-Indexing to rotate your index:

```
# Create a main index
index main
{
    source = main_source
    path = /var/lib/sphinxsearch/data/main
    ...
}

# Create a delta index
index delta
{
    source = delta_source
    path = /var/lib/sphinxsearch/data/delta
    ...
    # Specify the main index as the parent index
    # for the delta index
    parent = main
}
```

Once the delta index is created, you can use the `indexer` command to update the main index with the changes in the delta index.

```
indexer --rotate --merge main delta
```

This command will merge the changes in the delta index into the main index, and then rotate the main index so that it is up-to-date.

## Code explanation


- `index main`: Creates a main index from a source data set.
- `index delta`: Creates a delta index from a source data set.
- `parent = main`: Specifies that the delta index is a child of the main index.
- `indexer --rotate --merge main delta`: Merges the changes in the delta index into the main index, and then rotates the main index so that it is up-to-date.

## Helpful links

- [SphinxSearch Documentation](https://sphinxsearch.com/docs/current.html)
- [Delta-Indexing in SphinxSearch](https://sphinxsearch.com/docs/current.html#conf-delta-index)

onelinerhub: [How can I use SphinxSearch to rotate my index seamlessly?](https://onelinerhub.com/sphinxsearch/how-can-i-use-sphinxsearch-to-rotate-my-index-seamlessly)