# How can I use PHP Elastica with Apex?
// plain

PHP Elastica is an open-source library for connecting to and manipulating data stored in an Elasticsearch cluster. It can be used with Apex to provide a powerful way to query and manipulate data stored in an Elasticsearch cluster.

An example of using PHP Elastica with Apex could be as follows:

```php
<?php

require_once 'vendor/autoload.php';

use Elastica\Client;

$client = new Client(array(
    'host' => 'localhost',
    'port' => 9200
));

$index = $client->getIndex('apex');
$type = $index->getType('users');

$query = new \Elastica\Query\MatchAll();

$results = $type->search($query);

$data = $results->getResults();

foreach ($data as $result) {
    echo $result->getData()['name'] . "\n";
}

```

## Output example


John
Jane

In this example, we used PHP Elastica to connect to an Elasticsearch cluster and query for all documents in the `users` type of the `apex` index. We then looped through the results and printed out the `name` field of each document.

The code consists of the following parts:

1. `require_once 'vendor/autoload.php';` - This loads the autoloader for the PHP Elastica library.

2. `use Elastica\Client;` - This imports the `Client` class from the PHP Elastica library.

3. `$client = new Client(array(...));` - This creates a new instance of the `Client` class with the configuration for connecting to the Elasticsearch cluster.

4. `$index = $client->getIndex('apex');` - This retrieves the `apex` index from the Elasticsearch cluster.

5. `$type = $index->getType('users');` - This retrieves the `users` type from the `apex` index.

6. `$query = new \Elastica\Query\MatchAll();` - This creates a query for retrieving all documents from the `users` type.

7. `$results = $type->search($query);` - This executes the query against the `users` type.

8. `$data = $results->getResults();` - This retrieves the results of the query.

9. `foreach ($data as $result) {...}` - This loop iterates through the results and prints out the `name` field of each document.

For more information on using PHP Elastica with Apex, see the [PHP Elastica documentation](https://www.elastic.co/guide/en/elasticsearch/client/php-api/current/index.html).

onelinerhub: [How can I use PHP Elastica with Apex?](https://onelinerhub.com/php-elastica/how-can-i-use-php-elastica-with-apex)