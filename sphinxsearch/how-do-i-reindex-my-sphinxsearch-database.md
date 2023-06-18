# How do I reindex my SphinxSearch database?
// plain

To reindex a SphinxSearch database, you need to run the `indexer` command. The command requires two parameters: the name of the index you wish to reindex, and the action to take. To reindex an existing index, the action should be `--rotate`.

For example, the following command will reindex the index named `myindex`:
```
indexer --rotate myindex
```

The output of the command will look something like this:
```
Sphinx 2.2.11-id64-release (r5654)
Copyright (c) 2001-2017, Andrew Aksyonoff
Copyright (c) 2008-2017, Sphinx Technologies Inc (http://sphinxsearch.com)

using config file '/usr/local/sphinx/etc/sphinx.conf'...
indexing index 'myindex'...
collected 0 docs, 0.0 MB
sorted 0.0 Mhits, 100.0% done
total 0 docs, 0 bytes
total 0.006 sec, 0 bytes/sec, 0.00 docs/sec
```

The command performs the following operations:

* Reads the Sphinx configuration file (`sphinx.conf`)
* Identifies the index to be reindexed (`myindex`)
* Rotates the index (i.e. reindexes it)
* Outputs the results of the operation

For more information about the `indexer` command, see the [Sphinx documentation](https://www.sphinxsearch.com/docs/current.html#indexer).

onelinerhub: [How do I reindex my SphinxSearch database?](https://onelinerhub.com/sphinxsearch/how-do-i-reindex-my-sphinxsearch-database)