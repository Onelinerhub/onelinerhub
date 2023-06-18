# How do I create a Sphinx search index?
// plain

1. To create a Sphinx search index, the first step is to create a configuration file in the Sphinx directory. This file should contain the data source, index settings, and indexing options.

2. Next, run the `indexer` command to build the index. The command should include the name of the configuration file and the name of the index.

```
indexer --config <config_file_name> <index_name>
```

3. After the index is created, run the `searchd` command to start the search daemon. This command should also include the name of the configuration file.

```
searchd --config <config_file_name>
```

4. Finally, use the `search` command to query the index. This command should include the name of the index and the search query.

```
search <index_name> <search_query>
```

5. The output of the `search` command will be a list of documents that match the query.

6. To learn more about creating Sphinx search indexes, see the [Sphinx Documentation](http://sphinxsearch.com/docs/current.html).

7. Additionally, the [Sphinx Quick Start Guide](http://sphinxsearch.com/docs/current.html#quick-start-guide) provides a detailed overview of the process.

onelinerhub: [How do I create a Sphinx search index?](https://onelinerhub.com/sphinxsearch/how-do-i-create-a-sphinx-search-index)