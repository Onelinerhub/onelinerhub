# How can I use Sphinx Search to create a wiki?
// plain

Sphinx Search can be used to create a wiki by indexing the wiki content and then providing a search interface. The following is an example of how to use Sphinx Search to index a wiki:

```
# create the index
indexer --config /etc/sphinxsearch/sphinx.conf --all

# start the searchd service
searchd --config /etc/sphinxsearch/sphinx.conf
```

The above code will create an index of the wiki content and start the searchd service, allowing users to search the indexed content.

To use the search interface, you can use SphinxQL or SphinxAPI. For example, to query the index using SphinxQL:

```
SELECT * FROM wiki WHERE MATCH('some search term');
```

This will return all documents from the wiki index that match the search term.

Parts of the code:

* `indexer`: creates the index
* `searchd`: starts the searchd service
* `SELECT`: queries the index using SphinxQL

## Helpful links

* [Sphinx Search Documentation](http://sphinxsearch.com/docs/)
* [SphinxQL Syntax](http://sphinxsearch.com/docs/current.html#sphinxql-syntax)
* [SphinxAPI Documentation](http://sphinxsearch.com/docs/current.html#api-reference)

onelinerhub: [How can I use Sphinx Search to create a wiki?](https://onelinerhub.com/sphinxsearch/how-can-i-use-sphinx-search-to-create-a-wiki)