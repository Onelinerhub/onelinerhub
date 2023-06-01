# How do I create a PHP tutorial using Elastic?
// plain

Creating a PHP tutorial using Elastic is relatively simple. First, you'll need to install and configure Elasticsearch. After that, you can use the following example code to index a document:

```php
$params = [
    'index' => 'my_index',
    'type' => 'my_type',
    'id' => 'my_id',
    'body' => [
        'title' => 'My first document',
        'content' => 'This is my first document in Elasticsearch'
    ]
];

$response = $client->index($params);
print_r($response);
```

This code will index a document with the title "My first document" and content "This is my first document in Elasticsearch". The output of this code should be a response containing the status of the operation.

To query the document we just indexed, we can use the following code:

```php
$params = [
    'index' => 'my_index',
    'type' => 'my_type',
    'id' => 'my_id'
];

$response = $client->get($params);
print_r($response);
```

This code will query the document with the ID "my_id" from the index "my_index" and type "my_type". The output of this code should be a response containing the document we indexed.

For more information on working with Elasticsearch in PHP, check out the [official documentation](https://www.elastic.co/guide/en/elasticsearch/client/php-api/current/index.html).

onelinerhub: [How do I create a PHP tutorial using Elastic?](https://onelinerhub.com/php-elastica/how-do-i-create-a-php-tutorial-using-elastic)