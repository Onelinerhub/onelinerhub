# How do I create and manage RT indexes using SphinxSearch?
// plain

SphinxSearch is a full-text search engine for databases and websites. It provides a powerful and efficient way to create and manage RT indexes.

RT indexes are used for real-time searches, which can be used to quickly find documents that match a given query. They are created using the `index` command in SphinxSearch. The command takes the following parameters:

- `name`: The name of the index
- `source`: The source from which the index will be built (e.g. a database table)
- `path`: The path where the index will be stored
- `rt`: A flag indicating that the index should be an RT index

For example, to create an RT index called `my_index` from a table called `my_table`, the following command can be used:

```
index my_index
{
    source = my_table
    path = /var/sphinx/data/my_index
    rt
}
```

Once the index is created, it can be managed with the `indexer` command. The command takes the following parameters:

- `name`: The name of the index
- `action`: The action to be performed (e.g. build, merge, rotate)

For example, to build the `my_index` index, the following command can be used:

```
indexer --buildstops my_index
```

This will build the index and create the necessary stopwords.

Finally, the index can be queried using the `search` command. The command takes the following parameters:

- `index`: The name of the index to query
- `query`: The query to be executed

For example, to search for documents containing the word "foo" in the `my_index` index, the following command can be used:

```
search my_index foo
```

This will search the index and return a list of documents that match the query.

## Helpful links
- [SphinxSearch Documentation](http://sphinxsearch.com/docs/current.html)
- [SphinxSearch Tutorial](http://sphinxsearch.com/docs/tutorial.html)

onelinerhub: [How do I create and manage RT indexes using SphinxSearch?](https://onelinerhub.com/sphinxsearch/how-do-i-create-and-manage-rt-indexes-using-sphinxsearch)