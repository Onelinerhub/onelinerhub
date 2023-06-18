# How do I use SphinxSearch with Postgres?
// plain

SphinxSearch is an open source full-text search engine that can be used with Postgres. It is a lightweight, fast, and powerful search engine that can be used to index and search large amounts of data quickly.

To use SphinxSearch with Postgres, you will need to install both Postgres and SphinxSearch on your system.

Once you have installed the two programs, you will need to create a configuration file for SphinxSearch. This file will contain all the necessary information for SphinxSearch to connect to Postgres.

You will then need to create a database in Postgres and create the necessary tables for SphinxSearch.

Once the database and tables have been created, you will need to use the `indexer` command to create the indexes for SphinxSearch.

For example:
```
indexer --config sphinx.conf --all
```

Once the indexes have been created, you can use the `search` command to search the indexed data.

For example:
```
search --config sphinx.conf "query"
```

## Helpful links
- [SphinxSearch](https://sphinxsearch.com/)
- [Postgres](https://www.postgresql.org/)

onelinerhub: [How do I use SphinxSearch with Postgres?](https://onelinerhub.com/sphinxsearch/how-do-i-use-sphinxsearch-with-postgres)