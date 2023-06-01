# How can I use a PHP Elastic Client to interact with an Elasticsearch cluster?
// plain

Using the PHP Elastic Client, you can interact with an Elasticsearch cluster by performing various operations such as indexing, searching, and deleting documents.

For example, you can create an index and add a document to it using the following code block:

```
<?php

require 'vendor/autoload.php';

$client = Elasticsearch\ClientBuilder::create()->build();

// Create an index
$params = [
    'index' => 'my_index',
    'body' => [
        'settings' => [
            'number_of_shards' => 3,
            'number_of_replicas' => 2
        ]
    ]
];

$response = $client->indices()->create($params);

// Add a document
$params = [
    'index' => 'my_index',
    'type' => 'my_type',
    'id' => 'my_id',
    'body' => [
        'title' => 'My document',
        'content' => 'This is my document'
    ]
];

$response = $client->index($params);

echo $response['result'];

// Output: created
```

The code block above will create an index named `my_index` with 3 shards and 2 replicas, and add a document to it with title `My document` and content `This is my document`.

In addition, you can also use the PHP Elastic Client to perform more operations such as searching, deleting, and updating documents.

## Helpful links

- [PHP Elastic Client](https://www.elastic.co/guide/en/elasticsearch/client/php-api/current/index.html)
- [Creating an Index](https://www.elastic.co/guide/en/elasticsearch/client/php-api/current/_index_operations.html#_create_an_index)
- [Adding a Document](https://www.elastic.co/guide/en/elasticsearch/client/php-api/current/_index_documents.html#_index_a_document)

onelinerhub: [How can I use a PHP Elastic Client to interact with an Elasticsearch cluster?](https://onelinerhub.com/php-elastica/how-can-i-use-a-php-elastic-client-to-interact-with-an-elasticsearch-cluster)