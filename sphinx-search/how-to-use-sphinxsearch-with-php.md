# How to use SphinxSearch with PHP?
// plain

SphinxSearch is a full-text search engine written in C++. It can be used with PHP to provide fast and powerful search capabilities.

To use SphinxSearch with PHP, you need to install the [Sphinx PHP extension](https://github.com/sphinxsearch/sphinx/tree/master/api/libsphinxclient).

Once the extension is installed, you can use the following code to connect to the SphinxSearch server:

```php
$sphinx = new SphinxClient();
$sphinx->SetServer('localhost', 9312);
```

You can then use the `Query()` method to execute a search query:

```php
$result = $sphinx->Query('search query');
```

The `$result` variable will contain an array of results, with each result containing the document ID and the relevance score.

## Helpful links

- [SphinxSearch Documentation](http://sphinxsearch.com/docs/)
- [Sphinx PHP Extension](https://github.com/sphinxsearch/sphinx/tree/master/api/libsphinxclient)

onelinerhub: [How to use SphinxSearch with PHP?](https://onelinerhub.com/sphinx-search/how-to-use-sphinxsearch-with-php)