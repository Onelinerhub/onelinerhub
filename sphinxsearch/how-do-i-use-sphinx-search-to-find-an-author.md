# How do I use Sphinx Search to find an author?
// plain

Sphinx Search is a full-text search engine that can be used to quickly and easily search for authors. To use Sphinx Search to find an author, you first need to create an index of the data you want to search. Then, you can use the SphinxQL query language to search the index.

For example, to find an author with the name "John Smith", you can use the following query:

```
SELECT * FROM authors WHERE name = 'John Smith';
```

This query will return all the records from the authors index where the name is "John Smith".

The parts of the query are as follows:

* `SELECT` - specifies the columns to return from the index
* `FROM` - specifies the index to search
* `WHERE` - specifies the condition that must be met for a record to be returned

Here are some useful links for learning more about Sphinx Search:

* [Sphinx Documentation](http://sphinxsearch.com/docs/current.html)
* [SphinxQL Reference](http://sphinxsearch.com/docs/current.html#sphinxql-reference)

onelinerhub: [How do I use Sphinx Search to find an author?](https://onelinerhub.com/sphinxsearch/how-do-i-use-sphinx-search-to-find-an-author)