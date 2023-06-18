# How do I use the SphinxSearch indexer?
// plain

SphinxSearch is a full-text search engine designed to provide fast and relevant search results. It can be used to index and search data stored in a variety of databases, including MySQL, PostgreSQL, and SQLite.

To use the SphinxSearch indexer, you need to create an index configuration file. This file will define the data sources, index settings, and other parameters that SphinxSearch will use to index your data.

Once the configuration file is created, you can use the `indexer` command to build the index. The syntax for the indexer command is:

```
indexer [options] <indexname> [<indexname2> ...]
```

For example, if you have a configuration file named `myindex.conf`, you can build the index by running:

```
indexer --config myindex.conf
```

Once the index has been built, you can use the `search` command to query the index. The syntax for the search command is:

```
search [options] <indexname> <query>
```

For example, to query the index for the term "sphinxsearch", you can run:

```
search --index myindex "sphinxsearch"
```

## Helpful links

- [Sphinx Documentation](http://sphinxsearch.com/docs/current.html)
- [SphinxSearch Tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-sphinx-on-ubuntu-14-04)

onelinerhub: [How do I use the SphinxSearch indexer?](https://onelinerhub.com/sphinxsearch/how-do-i-use-the-sphinxsearch-indexer)