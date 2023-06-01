# How can I use PHP to create an elastic query?
// plain

PHP can be used to create an elastic query by using the [Elasticsearch PHP Client](https://github.com/elastic/elasticsearch-php). This client provides an API for creating, updating, and deleting documents in an index. It also provides methods for executing search queries and retrieving search results.

For example, the following code can be used to create an elastic query:
```
<?php
$params = [
    'index' => 'my_index',
    'body' => [
        'query' => [
            'match' => [
                'title' => 'My Query'
            ]
        ]
    ]
];
$response = $client->search($params);
```

This code creates an elastic query that searches for documents in the `my_index` index with a title field matching the string `My Query`. The response from the query will be stored in the `$response` variable.

The code consists of the following parts:

1. The `$params` array contains the parameters for the query. It includes the index to search in and the body of the query.
2. The `$client` variable is an instance of the Elasticsearch PHP Client.
3. The `search` method is used to execute the query and retrieve the results.

For more information, please refer to the [Elasticsearch PHP Client documentation](https://www.elastic.co/guide/en/elasticsearch/client/php-api/current/index.html).

onelinerhub: [How can I use PHP to create an elastic query?](https://onelinerhub.com/php-elastica/how-can-i-use-php-to-create-an-elastic-query)