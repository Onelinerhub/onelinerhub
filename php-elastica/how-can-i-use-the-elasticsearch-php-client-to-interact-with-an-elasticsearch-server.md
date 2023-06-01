# How can I use the Elasticsearch PHP client to interact with an Elasticsearch server?
// plain

The Elasticsearch PHP client is a library that allows developers to interact with an Elasticsearch server from a PHP application. The client provides an API that supports the full range of Elasticsearch APIs, including indexing, searching, and managing cluster state.

To use the Elasticsearch PHP client, you need to include the library in your project. You can install the library using Composer:

```
composer require elasticsearch/elasticsearch
```

Once the library is installed, you can use it to interact with an Elasticsearch server. For example, to search for documents in an index, you can use the `search()` method:

```php
<?php

$client = new \Elasticsearch\Client();

$params = [
    'index' => 'my_index',
    'body' => [
        'query' => [
            'match' => [
                'title' => 'Elasticsearch'
            ]
        ]
    ]
];

$response = $client->search($params);

print_r($response);
```

This code would search the `my_index` index for documents with the word "Elasticsearch" in the `title` field. The `$response` variable would contain the response from the Elasticsearch server, which would look something like this:

```
Array
(
    [took] => 4
    [timed_out] =>
    [_shards] => Array
        (
            [total] => 5
            [successful] => 5
            [skipped] => 0
            [failed] => 0
        )

    [hits] => Array
        (
            [total] => 1
            [max_score] => 1.0
            [hits] => Array
                (
                    [0] => Array
                        (
                            [_index] => my_index
                            [_type] => _doc
                            [_id] => 1
                            [_score] => 1.0
                            [_source] => Array
                                (
                                    [title] => Elasticsearch
                                )
                        )
                )
        )
)
```

The Elasticsearch PHP client also provides methods for indexing documents, managing cluster state, and other tasks. For more information, see the [official documentation](https://www.elastic.co/guide/en/elasticsearch/client/php-api/current/index.html).

onelinerhub: [How can I use the Elasticsearch PHP client to interact with an Elasticsearch server?](https://onelinerhub.com/php-elastica/how-can-i-use-the-elasticsearch-php-client-to-interact-with-an-elasticsearch-server)