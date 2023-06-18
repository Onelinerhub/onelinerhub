# How do I use Sphinx Search in batch mode?
// plain

Sphinx Search can be used in batch mode by using the `searchd` command. This command takes a configuration file as an argument and runs the indexing and searching process.

## Example code

```
searchd --config /path/to/sphinx.conf
```

This command will start the searchd daemon, which will read the configuration file `sphinx.conf` and then start the indexing and searching process.

The configuration file `sphinx.conf` contains the following sections:
- `source`: This section contains the data source information, such as the database type, database connection details, and the query to be used for indexing.
- `index`: This section contains the settings for the index, such as the name of the index, the type of index, and the fields to be indexed.
- `searchd`: This section contains the settings for the searchd daemon, such as the port number and the number of threads.

The output of the `searchd` command will be a message indicating that the searchd daemon has started.

## Helpful links
- [Sphinx Documentation](http://sphinxsearch.com/docs/current.html)
- [Sphinx Configuration File](http://sphinxsearch.com/docs/current.html#conf-overview)

onelinerhub: [How do I use Sphinx Search in batch mode?](https://onelinerhub.com/sphinxsearch/how-do-i-use-sphinx-search-in-batch-mode)