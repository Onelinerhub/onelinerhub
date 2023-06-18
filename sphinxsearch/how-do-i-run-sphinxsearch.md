# How do I run SphinxSearch?
// plain

SphinxSearch is a full-text search engine that can be used to search large databases. It is written in C++ and can be used on Linux, Mac OS X, and Windows.

To run SphinxSearch, you will need to install the software on your machine. The installation instructions can be found [here](http://sphinxsearch.com/docs/current.html#installation).

Once SphinxSearch is installed, you can start the search daemon by running the following command:

```
$ searchd --config /path/to/sphinx.conf
```

The `--config` flag is used to specify the path to the configuration file for SphinxSearch. This file contains the settings for the search engine, such as the data source, indexing settings, and search settings.

Once the search daemon is running, you can use the search command-line client to perform searches:

```
$ search --config /path/to/sphinx.conf <query>
```

The `search` command will search the database specified in the configuration file and return the results.

You can also use the SphinxQL API to perform queries programmatically. The API is a SQL-like language for querying the SphinxSearch database. Documentation for the API can be found [here](http://sphinxsearch.com/docs/current.html#sphinxql-reference).

onelinerhub: [How do I run SphinxSearch?](https://onelinerhub.com/sphinxsearch/how-do-i-run-sphinxsearch)