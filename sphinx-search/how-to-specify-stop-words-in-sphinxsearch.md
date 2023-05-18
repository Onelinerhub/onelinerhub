# How to specify stop words in SphinxSearch?
// plain

Stop words are words that are filtered out before or after processing of natural language data. In SphinxSearch, stop words can be specified by adding them to the `stopwords` configuration option in the `sphinx.conf` file.

For example, the following code block adds the words "the", "a", and "an" to the list of stop words:

```
stopwords = the, a, an
```

The `stopwords` option takes a comma-separated list of words that should be excluded from the search index. The words will be excluded from the index and will not be included in the search results.

In addition to the `stopwords` option, SphinxSearch also provides the `exclude` option, which can be used to exclude words from the search index. The `exclude` option takes a comma-separated list of words that should be excluded from the search index, but will still be included in the search results.

For more information about stop words and other configuration options in SphinxSearch, please refer to the [SphinxSearch documentation](http://sphinxsearch.com/docs/current.html).

onelinerhub: [How to specify stop words in SphinxSearch?](https://onelinerhub.com/sphinx-search/how-to-specify-stop-words-in-sphinxsearch)