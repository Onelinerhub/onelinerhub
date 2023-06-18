# How do I use Sphinx Search to find an exact phrase?
// plain

Sphinx Search is a powerful open-source full-text search engine that can be used to find exact phrases. To use Sphinx Search to find an exact phrase, you need to enclose the phrase in double quotation marks.

For example, the following code will search for the exact phrase "hello world":

```
$index->query("\"hello world\"");
```

This code will return the documents that contain the exact phrase "hello world".

## Code explanation


* `$index` - The name of the index to search.
* `query()` - The method used to send search queries to the Sphinx server.
* `"\"hello world\""` - The exact phrase to search for, enclosed in double quotation marks.

To learn more about Sphinx Search and how to use it to find exact phrases, you can check out the [Sphinx documentation](http://sphinxsearch.com/docs/current.html).

onelinerhub: [How do I use Sphinx Search to find an exact phrase?](https://onelinerhub.com/sphinxsearch/how-do-i-use-sphinx-search-to-find-an-exact-phrase)