# How can I use a PHP Elastic Query Builder to create an effective search query?
// plain

PHP Elastic Query Builder is an open source library that helps developers to easily create and execute complex search queries against Elasticsearch. It supports a wide range of query types, including full-text search, match query, multi-match query, term query, range query, and more.

To use the PHP Elastic Query Builder to create an effective search query, you need to define the query parameters such as the index, type, and query type. For example, the following code snippet shows how to create a multi-match query using the PHP Elastic Query Builder:

```
<?php

$params = [
    'index' => 'my_index',
    'type' => 'my_type',
    'body' => [
        'query' => [
            'multi_match' => [
                'query' => 'search term',
                'fields' => ['title', 'content']
            ]
        ]
    ]
];

$query = new \Elastica\Query($params);
$resultSet = $client->search($query);

```

The code above will create a multi-match query which searches for the term “search term” in the fields “title” and “content” of the index “my_index” and type “my_type”.

## Code explanation


- `$params`: An array containing the index, type, and body of the query.
- `'index' => 'my_index'`: The index to search in.
- `'type' => 'my_type'`: The type to search in.
- `'body' => [ … ]`: The body of the query, containing the query type and parameters.
- `'multi_match' => [ … ]`: The query type, in this case a multi-match query.
- `'query' => 'search term'`: The search term to be searched for.
- `'fields' => ['title', 'content']`: The fields to search in.
- `$query = new \Elastica\Query($params)`: Create a new query object using the parameters.
- `$resultSet = $client->search($query)`: Execute the query and get the results.

For more information about the PHP Elastic Query Builder, please refer to the [official documentation](https://www.elastic.co/guide/en/elasticsearch/client/php-api/current/_query_builder.html).

onelinerhub: [How can I use a PHP Elastic Query Builder to create an effective search query?](https://onelinerhub.com/php-elastica/how-can-i-use-a-php-elastic-query-builder-to-create-an-effective-search-query)