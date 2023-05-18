# How to use the SphinxSearch indexer command?
// plain

The SphinxSearch indexer command is used to create and manage indexes for full-text search. It can be used to create, update, and delete indexes.

## Example

```
indexer --config /etc/sphinx/sphinx.conf --all
```

## Output example

```
Sphinx 2.2.11-id64-release (r5161)
Copyright (c) 2001-2017, Andrew Aksyonoff
Copyright (c) 2008-2017, Sphinx Technologies Inc (http://sphinxsearch.com)

using config file '/etc/sphinx/sphinx.conf'...
indexing index 'test1'...
collected 2 docs, 0.0 MB
sorted 0.0 Mhits, 100.0% done
total 2 docs, 64 bytes
total 0.001 sec, 64500 bytes/sec, 1720.00 docs/sec
```

## Code explanation

- `indexer`: the command to run the indexer
- `--config`: the option to specify the configuration file
- `/etc/sphinx/sphinx.conf`: the path to the configuration file
- `--all`: the option to index all indexes specified in the configuration file

## Helpful links
- [SphinxSearch Documentation](http://sphinxsearch.com/docs/current.html)
- [SphinxSearch Indexer Command](http://sphinxsearch.com/docs/current.html#indexer)

onelinerhub: [How to use the SphinxSearch indexer command?](https://onelinerhub.com/sphinx-search/how-to-use-the-sphinxsearch-indexer-command)