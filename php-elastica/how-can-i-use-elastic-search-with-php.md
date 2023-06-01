# How can I use Elastic Search with PHP?
// plain

Elasticsearch can be used with PHP by using the official Elasticsearch client library for PHP. This library allows you to communicate with an Elasticsearch cluster from your PHP code.

Example code for connecting to an Elasticsearch cluster in PHP:
```
<?php
require 'vendor/autoload.php';

$hosts = [
    'localhost:9200'
];

$client = Elasticsearch\ClientBuilder::create()
                    ->setHosts($hosts)
                    ->build();

$params = [
    'index' => 'my_index',
    'type'  => 'my_type',
    'id'    => 'my_id',
    'body'  => ['testField' => 'abc']
];

$response = $client->index($params);

print_r($response);
```

## Output example

```
Array
(
    [_index] => my_index
    [_type] => my_type
    [_id] => my_id
    [_version] => 1
    [result] => created
    [_shards] => Array
        (
            [total] => 2
            [successful] => 1
            [failed] => 0
        )

    [created] => 1
)
```

The code above:
- `require 'vendor/autoload.php';`: Loads the Elasticsearch client library
- `$hosts = [ 'localhost:9200' ];`: Sets the address of the Elasticsearch cluster
- `$client = Elasticsearch\ClientBuilder::create()->setHosts($hosts)->build();`: Creates a connection to the Elasticsearch cluster
- `$params = [ 'index' => 'my_index', 'type'  => 'my_type', 'id'    => 'my_id', 'body'  => ['testField' => 'abc'] ];`: Sets the parameters for the index request
- `$response = $client->index($params);`: Sends an index request to the Elasticsearch cluster
- `print_r($response);`: Prints the response from the Elasticsearch cluster

For more information on using Elasticsearch with PHP, see the official [documentation](https://www.elastic.co/guide/en/elasticsearch/client/php-api/current/index.html).

onelinerhub: [How can I use Elastic Search with PHP?](https://onelinerhub.com/php-elastica/how-can-i-use-elastic-search-with-php)