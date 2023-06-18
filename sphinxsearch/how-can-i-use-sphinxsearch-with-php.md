# How can I use SphinxSearch with PHP?
// plain

SphinxSearch is an open source full-text search engine that can be integrated with PHP. To use SphinxSearch with PHP, you will need to install the [php-sphinx](https://pecl.php.net/package/sphinx) library. Once installed, you can use the following code to connect to the SphinxSearch server and execute a search:

```php
<?php
$sphinx = new SphinxClient();
$sphinx->setServer("localhost", 9312);
$result = $sphinx->query("search_term");
if ($result === false) {
    echo "Query failed: " . $sphinx->getLastError();
} else {
    print_r($result);
}
?>
```

The code above will output an array containing the search results, including the total number of results, and an array of the matched documents.

1. `$sphinx = new SphinxClient()` creates a new SphinxClient object.
2. `$sphinx->setServer("localhost", 9312)` sets the host and port of the SphinxSearch server.
3. `$result = $sphinx->query("search_term")` executes the search query and returns the result.
4. `if ($result === false) {...}` checks if the query was successful.
5. `echo "Query failed: " . $sphinx->getLastError()` prints out the error message if the query failed.
6. `print_r($result)` prints out the search results.

## Helpful links

- [php-sphinx](https://pecl.php.net/package/sphinx)
- [SphinxSearch Documentation](http://sphinxsearch.com/docs/current.html)

onelinerhub: [How can I use SphinxSearch with PHP?](https://onelinerhub.com/sphinxsearch/how-can-i-use-sphinxsearch-with-php)