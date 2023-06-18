# How do I use the Sphinx search command line?
// plain

The Sphinx search command line can be used to quickly and easily search for documents or data in a database.

To use the Sphinx search command line, you must first install the Sphinx software. After installation, open the command line and type the following command:

```
searchd --config /usr/local/etc/sphinx.conf
```

This will start the search daemon, which will listen for requests from the command line.

Once the search daemon is running, you can start searching for documents or data using the following command:

```
indexer --all
```

This command will index all the documents or data in the database.

Once all the documents or data have been indexed, you can start searching using the following command:

```
search -i index_name "search query"
```

The `index_name` is the name of the index that you want to search, and the `search query` is the keyword or phrase that you want to search for.

For example, the following command will search for documents or data containing the phrase "sphinx search":

```
search -i index_name "sphinx search"
```

The output of the command will be a list of documents or data matching the search query.

## Helpful links

- [Sphinx Documentation](http://sphinxsearch.com/docs/current.html)
- [Searchd Command Line Tool](http://sphinxsearch.com/docs/current.html#searchd-command-line-tool)
- [Indexer Command Line Tool](http://sphinxsearch.com/docs/current.html#indexer-command-line-tool)
- [Search Command Line Tool](http://sphinxsearch.com/docs/current.html#search-command-line-tool)

onelinerhub: [How do I use the Sphinx search command line?](https://onelinerhub.com/sphinxsearch/how-do-i-use-the-sphinx-search-command-line)