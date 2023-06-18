# How do I use Sphinx search to query a JSON array?
// plain

Sphinx Search is a powerful search engine that allows you to query JSON arrays. To use it, you need to create an index of the JSON array first. This can be done with the following code:

```
$index = sphinx_create_index('my_index');
sphinx_index_array($index, $json_array);
```

Once the index is created, you can use the `sphinx_query()` function to query the JSON array. For example, the following code will search for all entries with a `name` field containing the word "John":

```
$results = sphinx_query($index, 'John', array('name'));
```

The `$results` variable will contain an array with the search results.

- `sphinx_create_index()` creates a new index from the given name.
- `sphinx_index_array()` adds the entries in the given JSON array to the index.
- `sphinx_query()` performs a search and returns the results.

## Helpful links
- [Sphinx Search Documentation](http://sphinxsearch.com/docs/)
- [Sphinx Search API Reference](http://sphinxsearch.com/docs/manual-2.2.3.html#api-reference)

onelinerhub: [How do I use Sphinx search to query a JSON array?](https://onelinerhub.com/sphinxsearch/how-do-i-use-sphinx-search-to-query-a-json-array)