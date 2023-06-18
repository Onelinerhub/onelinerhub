# How can I use the Sphinx Search API in PHP?
// plain

The Sphinx Search API can be used in PHP to search through large data sets quickly and efficiently. The API is available as a PHP extension, and can be installed using the following command:
```
pecl install sphinx
```

Once installed, the API can be used to create a connection to the Sphinx server and execute a query. The following example code creates a connection to the Sphinx server, executes a query, and prints the results:

```
<?php
// Create connection
$conn = new SphinxClient();
$conn->setServer("localhost", 9312);

// Execute query
$result = $conn->query("my query");

// Print results
print_r($result);
?>
```

The output of this code will be an array containing the results of the query, including the total number of matches, the time taken to execute the query, and the list of matches.

The Sphinx Search API also provides a range of other options, including the ability to set filters, sort results, and limit the number of results returned. For more information about the Sphinx Search API and its features, please refer to the [official documentation](http://sphinxsearch.com/docs/).

onelinerhub: [How can I use the Sphinx Search API in PHP?](https://onelinerhub.com/sphinxsearch/how-can-i-use-the-sphinx-search-api-in-php)